from __future__ import annotations

import copy
import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_delivery_graph.py"
SPEC = importlib.util.spec_from_file_location("validate_delivery_graph", MODULE_PATH)
assert SPEC and SPEC.loader
validate_delivery_graph = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validate_delivery_graph)


class DeliveryGraphValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        artifact = self.root / "planning/delivery/stage.md"
        artifact.parent.mkdir(parents=True, exist_ok=True)
        artifact.write_text("# Stage\n", encoding="utf-8")
        self.graph = {
            "schema_version": "delivery-graph/v1",
            "nodes": [
                {
                    "id": "stage-1",
                    "type": "stage",
                    "title": "Stage 1",
                    "summary": "Foundation",
                    "status": "completed",
                    "path": "planning/delivery/stage.md",
                },
                {
                    "id": "decision-2",
                    "type": "decision",
                    "title": "Next decision",
                    "summary": "Shape the next stage",
                },
            ],
            "edges": [
                {"from": "stage-1", "to": "decision-2", "type": "carried_forward_to"}
            ],
        }

    def tearDown(self) -> None:
        self.temp.cleanup()

    def validate(self, graph: dict) -> list[str]:
        return validate_delivery_graph.validate_graph(graph, self.root)

    def test_valid_graph_passes(self) -> None:
        self.assertEqual([], self.validate(self.graph))

    def test_duplicate_node_id_fails(self) -> None:
        graph = copy.deepcopy(self.graph)
        graph["nodes"].append(copy.deepcopy(graph["nodes"][0]))
        self.assertTrue(any("duplicate node id" in error for error in self.validate(graph)))

    def test_missing_edge_endpoint_fails(self) -> None:
        graph = copy.deepcopy(self.graph)
        graph["edges"][0]["to"] = "missing"
        self.assertTrue(any("missing target node" in error for error in self.validate(graph)))

    def test_invalid_node_type_fails(self) -> None:
        graph = copy.deepcopy(self.graph)
        graph["nodes"][1]["type"] = "task"
        self.assertTrue(any("invalid node type" in error for error in self.validate(graph)))

    def test_invalid_edge_type_fails(self) -> None:
        graph = copy.deepcopy(self.graph)
        graph["edges"][0]["type"] = "depends_on"
        self.assertTrue(any("invalid edge type" in error for error in self.validate(graph)))

    def test_missing_required_field_fails(self) -> None:
        graph = copy.deepcopy(self.graph)
        del graph["nodes"][1]["summary"]
        self.assertTrue(any("missing required fields" in error for error in self.validate(graph)))

    def test_generated_site_path_fails(self) -> None:
        graph = copy.deepcopy(self.graph)
        graph["nodes"][1]["path"] = "_site/index.html"
        self.assertTrue(any("generated site output" in error for error in self.validate(graph)))


if __name__ == "__main__":
    unittest.main()
