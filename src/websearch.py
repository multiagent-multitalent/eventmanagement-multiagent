"""Simple online web search helpers for current research context."""

from __future__ import annotations

import json
import logging
import base64
from xml.etree import ElementTree
from html.parser import HTMLParser
from datetime import datetime, timezone
from typing import Any
from urllib.parse import parse_qs, unquote, urlencode, urlparse
from urllib.request import Request, urlopen

logger = logging.getLogger(__name__)

_DDG_ENDPOINT = "https://api.duckduckgo.com/"
_DDG_HTML_ENDPOINT = "https://html.duckduckgo.com/html/"
_BING_RSS_ENDPOINT = "https://www.bing.com/search"
_IRRELEVANT_DOMAINS = {
    "transfermarkt.de",
    "kicker.de",
    "weltfussball.de",
}


def _safe_str(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def _flatten_related_topics(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    flat: list[dict[str, Any]] = []
    for item in items:
        if "Topics" in item and isinstance(item["Topics"], list):
            flat.extend(_flatten_related_topics(item["Topics"]))
        else:
            flat.append(item)
    return flat


def _extract_final_url(raw_url: str) -> str:
    """Extract target URL from DuckDuckGo redirect links."""
    url = _safe_str(raw_url)
    if not url:
        return ""
    if url.startswith("//"):
        url = f"https:{url}"
    if "duckduckgo.com/l/?" not in url and "duckduckgo.com/y.js" not in url:
        return url
    try:
        parsed = urlparse(url)
        query_params = parse_qs(parsed.query)
        target = _safe_str(query_params.get("uddg", [""])[0])
        if not target:
            target = _safe_str(query_params.get("u", [""])[0])
        if not target:
            target = _safe_str(query_params.get("u3", [""])[0])

        target = unquote(target)
        if "bing.com/aclick" in target:
            nested = urlparse(target)
            nested_params = parse_qs(nested.query)
            nested_target = _safe_str(nested_params.get("u", [""])[0])
            if nested_target:
                target = unquote(nested_target)

        if target and target.startswith("aHR0"):
            try:
                padded = target + "=" * (-len(target) % 4)
                decoded = base64.b64decode(padded).decode("utf-8", errors="ignore")
                target = decoded or target
            except Exception:
                pass

        return target or url
    except Exception:
        return url


def _is_search_redirect_or_ad(url: str) -> bool:
    """Filter obvious tracking/ad redirect URLs from normalized search results."""
    lowered = _safe_str(url).lower()
    if not lowered:
        return True
    blocked_markers = [
        "duckduckgo.com/y.js",
        "duckduckgo.com/l/?",
        "bing.com/aclick",
    ]
    if any(marker in lowered for marker in blocked_markers):
        return True
    if not (lowered.startswith("http://") or lowered.startswith("https://")):
        return True
    return False


def _is_relevant_event_result(source: dict[str, str]) -> bool:
    """Keep only results that look relevant for venue/catering event research."""
    title = _safe_str(source.get("title", "")).lower()
    url = _safe_str(source.get("url", "")).lower()
    snippet = _safe_str(source.get("snippet", "")).lower()

    if not url:
        return False

    parsed = urlparse(url)
    host = parsed.netloc.lower().replace("www.", "")
    if host in _IRRELEVANT_DOMAINS:
        return False

    haystack = " ".join([title, url, snippet])
    relevant_markers = [
        "event",
        "eventlocation",
        "location",
        "venue",
        "konferenz",
        "kongress",
        "tagung",
        "meeting",
        "seminar",
        "catering",
        "cater",
        "hotel",
    ]
    return any(marker in haystack for marker in relevant_markers)


class _DuckDuckGoHtmlParser(HTMLParser):
    """Very small parser for DuckDuckGo HTML results."""

    def __init__(self) -> None:
        super().__init__()
        self.results: list[dict[str, str]] = []
        self._capture_title = False
        self._capture_snippet = False
        self._title_parts: list[str] = []
        self._snippet_parts: list[str] = []
        self._current_url = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {k: (v or "") for k, v in attrs}
        class_name = attrs_dict.get("class", "")

        if tag == "a" and "result__a" in class_name:
            self._capture_title = True
            self._title_parts = []
            self._snippet_parts = []
            self._current_url = _extract_final_url(attrs_dict.get("href", ""))
        elif tag in {"a", "div"} and "result__snippet" in class_name:
            self._capture_snippet = True

    def handle_data(self, data: str) -> None:
        text = _safe_str(data)
        if not text:
            return
        if self._capture_title:
            self._title_parts.append(text)
        if self._capture_snippet:
            self._snippet_parts.append(text)

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self._capture_title:
            self._capture_title = False
            title = " ".join(self._title_parts).strip()
            snippet = " ".join(self._snippet_parts).strip()
            if title and self._current_url:
                self.results.append(
                    {
                        "title": title[:180],
                        "url": self._current_url,
                        "snippet": (snippet or title)[:300],
                    }
                )
            self._title_parts = []
            self._snippet_parts = []
            self._current_url = ""
        elif tag in {"a", "div"} and self._capture_snippet:
            self._capture_snippet = False


def search_duckduckgo_html(query: str, max_results: int = 5, timeout: int = 12) -> list[dict[str, str]]:
    """Search DuckDuckGo HTML endpoint as fallback when Instant Answer has no local results."""
    q = _safe_str(query)
    if not q:
        return []

    params = urlencode({"q": q, "kl": "de-de"})
    request = Request(
        f"{_DDG_HTML_ENDPOINT}?{params}",
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "Accept-Language": "de-DE,de;q=0.9,en;q=0.8",
        },
    )

    try:
        with urlopen(request, timeout=timeout) as response:
            html = response.read().decode("utf-8", errors="ignore")
    except Exception as exc:  # pragma: no cover - network conditions vary
        logger.warning("DuckDuckGo HTML query failed for '%s': %s", q, exc)
        return []

    parser = _DuckDuckGoHtmlParser()
    parser.feed(html)

    deduped: list[dict[str, str]] = []
    seen_urls: set[str] = set()
    for item in parser.results:
        url = item["url"]
        if not url or _is_search_redirect_or_ad(url) or url in seen_urls:
            continue
        seen_urls.add(url)
        deduped.append(item)
        if len(deduped) >= max_results:
            break

    return deduped


def search_duckduckgo(query: str, max_results: int = 5, timeout: int = 10) -> list[dict[str, str]]:
    """Search DuckDuckGo Instant Answer API and return normalized result snippets."""
    q = _safe_str(query)
    if not q:
        return []

    params = urlencode({"q": q, "format": "json", "no_redirect": 1, "no_html": 1})
    request = Request(
        f"{_DDG_ENDPOINT}?{params}",
        headers={"User-Agent": "eventmanagement-multiagent/1.0"},
    )

    try:
        with urlopen(request, timeout=timeout) as response:
            payload = json.loads(response.read().decode("utf-8", errors="ignore"))
    except Exception as exc:  # pragma: no cover - network conditions vary
        logger.warning("DuckDuckGo query failed for '%s': %s", q, exc)
        return []

    results: list[dict[str, str]] = []

    abstract_text = _safe_str(payload.get("AbstractText"))
    abstract_url = _safe_str(payload.get("AbstractURL"))
    heading = _safe_str(payload.get("Heading")) or q
    if abstract_text and abstract_url:
        results.append({"title": heading, "url": abstract_url, "snippet": abstract_text})

    for item in payload.get("Results", []):
        title = _safe_str(item.get("Text"))
        url = _safe_str(item.get("FirstURL"))
        if title and url:
            results.append({"title": title[:180], "url": url, "snippet": title[:300]})

    related = _flatten_related_topics(payload.get("RelatedTopics", []))
    for item in related:
        text = _safe_str(item.get("Text"))
        url = _safe_str(item.get("FirstURL"))
        if text and url:
            results.append({"title": text[:180], "url": url, "snippet": text[:300]})

    deduped: list[dict[str, str]] = []
    seen_urls: set[str] = set()
    for item in results:
        url = item["url"]
        if url in seen_urls:
            continue
        seen_urls.add(url)
        deduped.append(item)
        if len(deduped) >= max_results:
            break

    if len(deduped) < max_results:
        fallback = search_duckduckgo_html(q, max_results=max_results * 2, timeout=timeout)
        for item in fallback:
            url = item["url"]
            if url in seen_urls:
                continue
            seen_urls.add(url)
            deduped.append(item)
            if len(deduped) >= max_results:
                break

    return deduped


def search_bing_rss(query: str, max_results: int = 5, timeout: int = 10) -> list[dict[str, str]]:
    """Search Bing RSS endpoint as secondary fallback.

    This endpoint is lightweight and usually returns stable result URLs even when
    HTML scraping on other providers is throttled.
    """
    q = _safe_str(query)
    if not q:
        return []

    params = urlencode({"q": q, "format": "rss", "setlang": "de"})
    request = Request(
        f"{_BING_RSS_ENDPOINT}?{params}",
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "Accept-Language": "de-DE,de;q=0.9,en;q=0.8",
        },
    )

    try:
        with urlopen(request, timeout=timeout) as response:
            xml_payload = response.read().decode("utf-8", errors="ignore")
    except Exception as exc:  # pragma: no cover - network conditions vary
        logger.warning("Bing RSS query failed for '%s': %s", q, exc)
        return []

    try:
        root = ElementTree.fromstring(xml_payload)
    except ElementTree.ParseError:
        return []

    results: list[dict[str, str]] = []
    seen_urls: set[str] = set()
    for item in root.findall("./channel/item"):
        title = _safe_str(item.findtext("title"))
        url = _safe_str(item.findtext("link"))
        snippet = _safe_str(item.findtext("description"))

        if not title or not url:
            continue
        if _is_search_redirect_or_ad(url):
            continue
        if url in seen_urls:
            continue

        seen_urls.add(url)
        results.append({"title": title[:180], "url": url, "snippet": (snippet or title)[:300]})
        if len(results) >= max_results:
            break

    return results


def build_web_research_context(event_data: dict[str, Any], max_results_per_query: int = 4) -> dict[str, Any]:
    """Collect fresh web snippets for venue and catering research."""
    event = event_data.get("event", event_data)
    name = _safe_str(event.get("name", "Event"))
    city = _safe_str(event.get("city", "Deutschland"))
    attendees = _safe_str(event.get("attendees_expected", ""))
    topics = event.get("topics", [])
    if not isinstance(topics, list):
        topics = []

    queries = [
        f"{city} Eventlocation Konferenz {attendees} Personen",
        f"{city} Catering Business Event Angebot",
        f"{name} venue alternatives {city}",
    ]
    for topic in topics[:2]:
        topic_text = _safe_str(topic)
        if topic_text:
            queries.append(f"{city} Veranstaltung {topic_text} Konferenz")

    # Add broader fallback queries because very specific event names often yield no hits.
    broadened_queries = [
        f"{city} Eventlocation",
        f"{city} Konferenzraum mieten",
        f"{city} Business Catering",
        f"{city} Tagungshotel",
    ]

    all_queries = list(dict.fromkeys([*queries, *broadened_queries]))

    sources: list[dict[str, str]] = []
    for query in all_queries:
        ddg_results = search_duckduckgo(query, max_results=max_results_per_query)
        sources.extend(ddg_results)

        # If DDG produced no usable results for a query, try Bing RSS as backup.
        if not ddg_results:
            sources.extend(search_bing_rss(query, max_results=max_results_per_query))

    if not sources:
        # Last-resort pass: run Bing RSS for all queries to avoid empty context.
        for query in all_queries:
            sources.extend(search_bing_rss(query, max_results=max_results_per_query))

    deduped_sources: list[dict[str, str]] = []
    seen_urls: set[str] = set()
    for source in sources:
        url = source.get("url", "")
        if not url or url in seen_urls:
            continue
        if not _is_relevant_event_result(source):
            continue
        seen_urls.add(url)
        deduped_sources.append(source)
        if len(deduped_sources) >= 12:
            break

    lines = []
    for idx, source in enumerate(deduped_sources, 1):
        title = source.get("title", "Quelle")
        url = source.get("url", "")
        snippet = source.get("snippet", "")
        lines.append(f"{idx}. {title} | {url} | {snippet}")

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "queries": all_queries,
        "sources": deduped_sources,
        "context_text": "\n".join(lines),
    }
