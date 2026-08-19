import tempfile
import unittest

from fastapi.testclient import TestClient

from api import create_app


class LocalAPIContractTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(suffix=".sqlite3", delete=False)
        self.tmp.close()
        self.client = TestClient(create_app(self.tmp.name))

    def tearDown(self):
        self.client.close()

    def test_health_is_local_reference_only(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.json()["external_side_effects"])
        self.assertEqual(response.json()["authority"], "local-reference-only")

    def test_project_entities_links_packet_and_gate(self):
        project_response = self.client.post(
            "/projects",
            json={"title": "API project", "objective": "Test the local API", "owner": "test"},
        )
        self.assertEqual(project_response.status_code, 200)
        project = project_response.json()
        project_id = project["id"]
        objective = self.client.post(
            "/entities/objective",
            json={
                "project_id": project_id,
                "statement": "Keep the project resumable",
                "success_condition": "Packet can be generated",
                "status": "open",
            },
        ).json()
        evidence = self.client.post(
            "/entities/evidence",
            json={
                "project_id": project_id,
                "proposition": "The API stores evidence",
                "source": "test",
                "method": "API test",
                "evidence_state": "measured_locally",
            },
        ).json()
        claim = self.client.post(
            "/entities/claim",
            json={
                "project_id": project_id,
                "statement": "The API stores traceability state",
                "evidence_state": "hypothesis",
                "permitted_wording": "The API test demonstrates local storage.",
                "limitations": "Local only",
            },
        ).json()
        link = self.client.post(
            f"/projects/{project_id}/links",
            json={
                "src_type": "evidence",
                "src_id": evidence["id"],
                "relation": "supports",
                "dst_type": "claim",
                "dst_id": claim["id"],
            },
        )
        self.assertEqual(link.status_code, 200)
        gate = self.client.post(
            "/entities/gate",
            json={"project_id": project_id, "phase": "frame", "criteria": ["Objective exists"], "status": "not_ready"},
        ).json()
        advanced = self.client.post(
            f"/gates/{gate['id']}/advance",
            json={"decision": "proceed", "authority": "test", "next_phase": "problem_context"},
        )
        self.assertEqual(advanced.status_code, 200)
        packet = self.client.get(f"/projects/{project_id}/packet")
        self.assertEqual(packet.status_code, 200)
        self.assertIn("Continuation Packet", packet.json()["markdown"])
        listed = self.client.get(f"/projects/{project_id}/entities/objective")
        self.assertEqual(listed.status_code, 200)
        self.assertEqual(listed.json()[0]["id"], objective["id"])

    def test_invalid_cross_project_link_returns_contract_error(self):
        p1 = self.client.post("/projects", json={"title": "P1", "objective": "One"}).json()
        p2 = self.client.post("/projects", json={"title": "P2", "objective": "Two"}).json()
        f1 = self.client.post("/entities/factor", json={"project_id": p1["id"], "statement": "F1"}).json()
        f2 = self.client.post("/entities/factor", json={"project_id": p2["id"], "statement": "F2"}).json()
        response = self.client.post(
            f"/projects/{p1['id']}/links",
            json={"src_type": "factor", "src_id": f1["id"], "relation": "related_to", "dst_type": "factor", "dst_id": f2["id"]},
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["type"], "kernel_contract_error")


if __name__ == "__main__":
    unittest.main(verbosity=2)
