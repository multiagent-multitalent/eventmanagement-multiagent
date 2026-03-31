import unittest

from src.config import load_event_config
from src.workflows.event_planning_graph import create_event_planning_graph, create_thread


class TestSystemSmoke(unittest.TestCase):
    def test_graph_runs_stage1_and_stage2(self) -> None:
        event_config = load_event_config()
        self.assertIn("event", event_config)

        workflow = create_event_planning_graph()
        thread_config = create_thread()

        initial_state = {
            "stage": 1,
            "status": "running",
            "event_data": event_config,
            "task_packages": [],
            "research_results": None,
            "user_decision": None,
            "planning_output": None,
            "content_output": None,
            "next_step": "Stage 1 starten",
            "error": None,
        }

        stage1 = workflow.invoke(initial_state, config=thread_config)
        self.assertEqual(stage1.get("status"), "waiting_for_user")
        research = stage1.get("research_results") or {}

        venue_options = research.get("venue_options") or []
        catering_options = research.get("catering_options") or []

        self.assertGreaterEqual(len(venue_options), 1)
        self.assertGreaterEqual(len(catering_options), 1)

        workflow.update_state(
            thread_config,
            {
                "user_decision": {
                    "selected_venue": venue_options[0]["name"],
                    "selected_catering": catering_options[0]["name"],
                    "notes": "Smoke test",
                },
                "status": "approved",
            },
        )

        final_state = workflow.invoke(None, config=thread_config)
        self.assertEqual(final_state.get("status"), "completed")
        self.assertIsNotNone(final_state.get("planning_output"))
        self.assertIsNotNone(final_state.get("content_output"))


if __name__ == "__main__":
    unittest.main()
