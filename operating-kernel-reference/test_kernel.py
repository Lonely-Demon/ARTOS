import json
import tempfile
import unittest
from pathlib import Path

from kernel import KernelError, OperatingKernel, seed_demo_kernel


class KernelAcceptanceTests(unittest.TestCase):
    def setUp(self):
        self.kernel = OperatingKernel(":memory:")
        self.project = self.kernel.create_project(
            "Acceptance project",
            "Verify the minimum operational contract.",
            owner="test",
            scope="Local state only",
        )
        self.project_id = self.project["id"]
        self.kernel.update("project", self.project_id, {"status": "active"}, actor="test")

    def tearDown(self):
        self.kernel.close()

    def test_create_and_resume_project(self):
        loaded = self.kernel.get("project", self.project_id)
        self.assertEqual(loaded["title"], "Acceptance project")
        self.assertEqual(loaded["current_phase"], "frame")
        self.assertGreaterEqual(len(self.kernel.events(self.project_id)), 2)

    def test_minimum_objects_and_traceability(self):
        objective = self.kernel.create(
            "objective",
            {
                "project_id": self.project_id,
                "statement": "Preserve traceability.",
                "success_condition": "Links are queryable.",
                "status": "open",
            },
        )
        evidence = self.kernel.create(
            "evidence",
            {
                "project_id": self.project_id,
                "proposition": "The link is stored.",
                "source": "test",
                "method": "unit test",
                "evidence_state": "measured_locally",
            },
        )
        claim = self.kernel.create(
            "claim",
            {
                "project_id": self.project_id,
                "statement": "Traceability works locally.",
                "scope": "This test",
                "evidence_state": "hypothesis",
                "permitted_wording": "The test suggests traceability works locally.",
            },
        )
        link1 = self.kernel.link(self.project_id, "evidence", evidence["id"], "supports", "claim", claim["id"])
        link2 = self.kernel.link(self.project_id, "objective", objective["id"], "addresses", "claim", claim["id"])
        self.assertEqual(link1["relation"], "supports")
        self.assertEqual(link2["relation"], "addresses")
        self.assertEqual(len(self.kernel.list_links(self.project_id)), 2)

    def test_invalid_transitions_are_rejected(self):
        work = self.kernel.create(
            "work_package",
            {"project_id": self.project_id, "objective": "Do work", "status": "proposed"},
        )
        with self.assertRaises(KernelError):
            self.kernel.update("work_package", work["id"], {"status": "closed"})
        with self.assertRaises(KernelError):
            self.kernel.update("project", self.project_id, {"status": "draft"})

    def test_claim_upgrade_requires_explicit_reason(self):
        claim = self.kernel.create(
            "claim",
            {
                "project_id": self.project_id,
                "statement": "A claim",
                "evidence_state": "hypothesis",
            },
        )
        with self.assertRaises(KernelError):
            self.kernel.update("claim", claim["id"], {"evidence_state": "verified"})
        updated = self.kernel.update(
            "claim",
            claim["id"],
            {"evidence_state": "measured_locally", "evidence_upgrade_reason": "Automated test evidence."},
        )
        self.assertEqual(updated["evidence_state"], "measured_locally")

    def test_gate_records_review_path_and_advances_project(self):
        gate = self.kernel.create(
            "gate",
            {
                "project_id": self.project_id,
                "phase": "frame",
                "criteria": ["Objective is stated"],
                "evidence_packet": [],
                "status": "not_ready",
            },
        )
        result = self.kernel.advance_gate(
            gate["id"],
            "conditional_proceed",
            authority="test-authority",
            next_phase="problem_context",
            unresolved_conditions=["Validate operating context"],
            rationale="Sufficient for bounded discovery.",
        )
        self.assertEqual(result["status"], "conditional_proceed")
        loaded_project = self.kernel.get("project", self.project_id)
        self.assertEqual(loaded_project["current_phase"], "problem_context")
        statuses = [event["payload"].get("after", {}).get("status") for event in self.kernel.events(self.project_id)]
        self.assertIn("packet_prepared", statuses)
        self.assertIn("review_in_progress", statuses)
        self.assertIn("conditional_proceed", statuses)

    def test_event_chain_and_projection_reconstruction(self):
        evidence = self.kernel.create(
            "evidence",
            {
                "project_id": self.project_id,
                "proposition": "Event history is reconstructable.",
                "source": "test",
                "method": "unit test",
                "evidence_state": "measured_locally",
            },
        )
        self.kernel.update("evidence", evidence["id"], {"limitations": "Local only"})
        self.assertTrue(self.kernel.verify_event_chain())
        projection = self.kernel.rebuild_projection(self.project_id)
        rebuilt = projection[("evidence", evidence["id"])]
        current = self.kernel.get("evidence", evidence["id"])
        self.assertEqual(rebuilt["limitations"], current["limitations"])

    def test_interrupted_transaction_rolls_back(self):
        with self.assertRaises(RuntimeError):
            with self.kernel.transaction():
                self.kernel.conn.execute(
                    "INSERT INTO entities(id, entity_type, payload_json, version, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)",
                    ("interrupted", "factor", "{}", 1, "now", "now"),
                )
                raise RuntimeError("simulated interruption")
        row = self.kernel.conn.execute("SELECT id FROM entities WHERE id = 'interrupted'").fetchone()
        self.assertIsNone(row)
        self.assertTrue(self.kernel.verify_event_chain())

    def test_continuation_packet_is_markdown_and_json(self):
        self.kernel.create(
            "factor",
            {
                "project_id": self.project_id,
                "statement": "An open question",
                "evidence_state": "open",
                "status": "open",
            },
        )
        with tempfile.TemporaryDirectory() as tmp:
            md_path, json_path = self.kernel.export_continuation(self.project_id, tmp)
            self.assertTrue(Path(md_path).exists())
            self.assertTrue(Path(json_path).exists())
            self.assertIn("Continuation Packet", Path(md_path).read_text())
            data = json.loads(Path(json_path).read_text())
            self.assertEqual(data["project"]["id"], self.project_id)
            self.assertIn("An open question", data["open_questions"])

    def test_tombstone_is_non_destructive(self):
        factor = self.kernel.create(
            "factor",
            {"project_id": self.project_id, "statement": "Retained history", "evidence_state": "open"},
        )
        self.kernel.delete_as_tombstone("factor", factor["id"], actor="test")
        self.assertIsNone(self.kernel.get("factor", factor["id"]))
        history = self.kernel.list_entities("factor", project_id=self.project_id, include_deleted=True)
        self.assertEqual(len(history), 1)
        self.assertTrue(history[0]["deleted"])
        self.assertTrue(any(e["event_type"] == "entity_tombstoned" for e in self.kernel.events(self.project_id)))


class SeedDemoTests(unittest.TestCase):
    def test_seed_demo_is_self_consistent(self):
        kernel, project_id = seed_demo_kernel(":memory:")
        try:
            self.assertTrue(kernel.verify_event_chain())
            packet, data = kernel.continuation_packet(project_id)
            self.assertIn("Kernel calibration project", packet)
            self.assertEqual(data["project"]["id"], project_id)
            self.assertGreaterEqual(len(data["links"]), 4)
        finally:
            kernel.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.kernel = OperatingKernel(":memory:")
        self.project = self.kernel.create_project("Workflow project", "Exercise the operational flow.")
        self.project_id = self.project["id"]
        self.kernel.update("project", self.project_id, {"status": "active"}, actor="test")

    def tearDown(self):
        self.kernel.close()

    def test_work_package_handoff_review_and_gate(self):
        from workflow import (
            acknowledge_handoff,
            assign_work_package,
            create_handoff,
            create_work_package,
            prepare_gate,
            review_work_package,
            start_work_package,
            submit_work_package,
        )

        work = create_work_package(
            self.kernel,
            self.project_id,
            objective="Map the decision space",
            question="Which alternatives remain viable?",
            inputs=["project context"],
            exclusions=["Implementation"],
            evidence_contract="Sources and explicit unknowns",
            acceptance="Decision-space map produced",
            owner="unassigned",
            reviewer="independent-reviewer",
            actor="test",
        )
        work = assign_work_package(self.kernel, work["id"], owner="research-cell", actor="test")
        self.assertEqual(work["status"], "assigned")
        handoff = create_handoff(
            self.kernel,
            self.project_id,
            sender="integrator",
            receiver="research-cell",
            work_package_id=work["id"],
            context="Project context",
            objective="Map alternatives",
            inputs=["project state"],
            exclusions=["No implementation recommendation yet"],
            evidence_contract="Record source and uncertainty",
            expected_output="Landscape map",
            acceptance="All major alternatives and open questions visible",
            authority="integrator",
            actor="test",
        )
        acknowledged = acknowledge_handoff(
            self.kernel, handoff["id"], accepted=True, acknowledgement="Scope understood", actor="research-cell"
        )
        self.assertEqual(acknowledged["status"], "acknowledged")
        start_work_package(self.kernel, work["id"], actor="research-cell")
        submitted = submit_work_package(
            self.kernel, work["id"], output_ids=["artifact_landscape"], actor="research-cell"
        )
        self.assertEqual(submitted["status"], "submitted")
        reviewed = review_work_package(
            self.kernel,
            work["id"],
            accepted=True,
            findings=["Scope and evidence contract satisfied"],
            reviewer="independent-reviewer",
            actor="independent-reviewer",
        )
        self.assertEqual(reviewed["status"], "accepted")
        gate = prepare_gate(
            self.kernel,
            self.project_id,
            phase="decision_space",
            criteria=["Alternatives visible", "Unknowns recorded"],
            evidence_packet=["artifact_landscape"],
            actor="integrator",
        )
        result = self.kernel.advance_gate(
            gate["id"],
            "proceed",
            authority="project-owner",
            next_phase="requirements_direction",
            actor="project-owner",
        )
        self.assertEqual(result["decision"], "proceed")
        self.assertEqual(self.kernel.get("project", self.project_id)["current_phase"], "requirements_direction")

    def test_rejected_review_returns_work(self):
        from workflow import assign_work_package, create_work_package, review_work_package, start_work_package, submit_work_package

        work = create_work_package(
            self.kernel,
            self.project_id,
            objective="Test",
            question="Is the evidence sufficient?",
            inputs=[],
            exclusions=[],
            evidence_contract="Record limitations",
            acceptance="Reviewable output",
            owner="x",
            reviewer="y",
        )
        assign_work_package(self.kernel, work["id"], owner="x")
        start_work_package(self.kernel, work["id"])
        submit_work_package(self.kernel, work["id"], output_ids=[])
        returned = review_work_package(
            self.kernel,
            work["id"],
            accepted=False,
            findings=["Missing limitations"],
            reviewer="y",
        )
        self.assertEqual(returned["status"], "returned")



class WorkerContractTests(unittest.TestCase):
    def test_task_package_requires_explicit_boundaries(self):
        from worker_contract import TaskPackage, WorkerContractError

        task = TaskPackage(project_id="p", work_package_id="w", objective="x", context="y")
        with self.assertRaises(WorkerContractError):
            task.validate()
        bounded = TaskPackage(
            project_id="p",
            work_package_id="w",
            objective="x",
            context="y",
            evidence_contract="record sources",
            allowed_paths=["/workspace/project"],
            side_effect_budget={"network": "deny", "external_write": "deny", "filesystem": "scoped"},
        )
        bounded.validate()

    def test_worker_result_is_review_only(self):
        from worker_contract import TaskPackage, WorkerContractError, WorkerResult, validate_worker_return

        task = TaskPackage(
            project_id="p",
            work_package_id="w",
            objective="x",
            context="y",
            evidence_contract="record sources",
            allowed_paths=["/workspace/project"],
            side_effect_budget={"network": "deny", "external_write": "deny"},
        )
        result = WorkerResult(
            project_id="p",
            work_package_id="w",
            status="succeeded",
            summary="Completed bounded work.",
            reproducibility={"runner": "test", "inputs_hash": "abc"},
        )
        admitted = validate_worker_return(task, result)
        self.assertFalse(admitted["admission"]["canonical_state_write"])
        self.assertTrue(admitted["admission"]["requires_review"])
        with self.assertRaises(WorkerContractError):
            WorkerResult(
                project_id="p",
                work_package_id="w",
                status="succeeded",
                summary="Unsafe result",
                requested_claim_upgrades=["claim_1"],
                reproducibility={"runner": "test"},
            ).validate()


class AdversarialBoundaryTests(unittest.TestCase):
    def test_cross_project_link_is_rejected(self):
        kernel = OperatingKernel(":memory:")
        try:
            p1 = kernel.create_project("P1", "One")
            p2 = kernel.create_project("P2", "Two")
            f1 = kernel.create("factor", {"project_id": p1["id"], "statement": "F1"})
            f2 = kernel.create("factor", {"project_id": p2["id"], "statement": "F2"})
            with self.assertRaises(KernelError):
                kernel.link(p1["id"], "factor", f1["id"], "related_to", "factor", f2["id"])
        finally:
            kernel.close()

    def test_tombstone_remains_visible_to_historical_query(self):
        kernel = OperatingKernel(":memory:")
        try:
            project = kernel.create_project("P", "Keep history")
            factor = kernel.create("factor", {"project_id": project["id"], "statement": "Historical factor"})
            kernel.delete_as_tombstone("factor", factor["id"])
            history = kernel.list_entities("factor", project_id=project["id"], include_deleted=True)
            self.assertEqual(len(history), 1)
            self.assertTrue(history[0]["deleted"])
        finally:
            kernel.close()

    def test_proceeding_gate_activates_draft_project(self):
        kernel = OperatingKernel(":memory:")
        try:
            project = kernel.create_project("P", "Gate activation")
            gate = kernel.create("gate", {"project_id": project["id"], "phase": "frame", "status": "not_ready"})
            kernel.advance_gate(gate["id"], "proceed", authority="test", next_phase="problem_context")
            self.assertEqual(kernel.get("project", project["id"])["status"], "active")
        finally:
            kernel.close()
