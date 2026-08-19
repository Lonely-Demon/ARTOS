"""Local-first Universal Enterprise operating-kernel reference slice.

This module intentionally has no external side effects. It stores project state and
append-only events in SQLite and provides the minimum operational contract needed
for continuity, traceability, gates, and later worker integration.
"""
from __future__ import annotations

import hashlib
import json
import sqlite3
import threading
import uuid
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


EVIDENCE_STATES = {
    "verified",
    "measured_locally",
    "estimated",
    "design_inference",
    "hypothesis",
    "open",
    "excluded",
}

PHASES = [
    "frame",
    "problem_context",
    "decision_space",
    "requirements_direction",
    "canonical_output",
    "implementation",
    "verify_attack",
    "operate_learn",
]

PROJECT_TRANSITIONS = {
    "draft": {"active", "stopped"},
    "active": {"paused", "completed", "stopped"},
    "paused": {"active", "stopped"},
    "completed": set(),
    "stopped": set(),
}

WORK_PACKAGE_TRANSITIONS = {
    "proposed": {"scoped", "escalated"},
    "scoped": {"assigned", "returned", "escalated"},
    "assigned": {"in_progress", "returned", "escalated"},
    "in_progress": {"submitted", "returned", "escalated"},
    "submitted": {"reviewed", "returned", "escalated"},
    "reviewed": {"accepted", "returned", "escalated"},
    "accepted": {"closed"},
    "returned": {"scoped", "assigned", "in_progress", "escalated"},
    "escalated": {"scoped", "assigned", "in_progress", "closed"},
    "closed": set(),
}

DECISION_TRANSITIONS = {
    "open": {"options_mapped", "deferred", "reopened"},
    "options_mapped": {"recommendation", "deferred", "reopened"},
    "recommendation": {"under_review", "deferred", "reopened"},
    "under_review": {"accepted", "accepted_with_conditions", "rejected", "deferred", "reopened"},
    "accepted": {"reopened"},
    "accepted_with_conditions": {"reopened", "accepted"},
    "rejected": {"reopened"},
    "deferred": {"open", "options_mapped", "reopened"},
    "reopened": {"open", "options_mapped"},
}

GATE_TRANSITIONS = {
    "not_ready": {"packet_prepared"},
    "packet_prepared": {"review_in_progress", "pause", "stop"},
    "review_in_progress": {
        "proceed",
        "conditional_proceed",
        "loop_back",
        "descope",
        "pause",
        "stop",
    },
    "proceed": set(),
    "conditional_proceed": set(),
    "loop_back": set(),
    "descope": set(),
    "pause": {"packet_prepared"},
    "stop": set(),
}

ENTITY_TYPES = {
    "project",
    "objective",
    "factor",
    "evidence",
    "decision",
    "risk",
    "work_package",
    "claim",
    "gate",
    "capability",
    "artefact",
    "requirement",
    "handoff",
    "review",
    "external_validation",
}

RELATIONS = {
    "supports",
    "challenges",
    "derived_from",
    "affects",
    "produces",
    "verifies",
    "validates",
    "activates",
    "depends_on",
    "evaluates",
    "claims",
    "addresses",
    "supersedes",
    "related_to",
}


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def stable_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def object_hash(value: Any) -> str:
    return hashlib.sha256(stable_json(value).encode("utf-8")).hexdigest()


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:16]}"


class KernelError(ValueError):
    """Expected domain or contract violation."""


class OperatingKernel:
    def __init__(self, db_path: str | Path = ":memory:") -> None:
        self.db_path = str(db_path)
        if self.db_path != ":memory:":
            Path(self.db_path).parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.RLock()
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.conn.execute("PRAGMA journal_mode = WAL")
        self._init_schema()

    def close(self) -> None:
        self.conn.close()

    def _init_schema(self) -> None:
        self.conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS entities (
                id TEXT PRIMARY KEY,
                project_id TEXT,
                entity_type TEXT NOT NULL,
                status TEXT,
                payload_json TEXT NOT NULL,
                version INTEGER NOT NULL DEFAULT 1,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                deleted INTEGER NOT NULL DEFAULT 0
            );
            CREATE INDEX IF NOT EXISTS idx_entities_project_type
              ON entities(project_id, entity_type, deleted);
            CREATE TABLE IF NOT EXISTS links (
                id TEXT PRIMARY KEY,
                project_id TEXT NOT NULL,
                src_type TEXT NOT NULL,
                src_id TEXT NOT NULL,
                relation TEXT NOT NULL,
                dst_type TEXT NOT NULL,
                dst_id TEXT NOT NULL,
                created_at TEXT NOT NULL,
                UNIQUE(src_type, src_id, relation, dst_type, dst_id)
            );
            CREATE INDEX IF NOT EXISTS idx_links_project ON links(project_id);
            CREATE TABLE IF NOT EXISTS events (
                sequence INTEGER PRIMARY KEY AUTOINCREMENT,
                event_id TEXT UNIQUE NOT NULL,
                project_id TEXT,
                event_type TEXT NOT NULL,
                entity_type TEXT,
                entity_id TEXT,
                payload_json TEXT NOT NULL,
                actor TEXT NOT NULL,
                occurred_at TEXT NOT NULL,
                prior_hash TEXT,
                event_hash TEXT NOT NULL
            );
            CREATE INDEX IF NOT EXISTS idx_events_project ON events(project_id, sequence);
            """
        )
        self.conn.commit()

    @contextmanager
    def transaction(self):
        with self._lock:
            try:
                self.conn.execute("BEGIN IMMEDIATE")
                yield
                self.conn.commit()
            except Exception:
                self.conn.rollback()
                raise

    def _latest_event_hash(self) -> str | None:
        row = self.conn.execute(
            "SELECT event_hash FROM events ORDER BY sequence DESC LIMIT 1"
        ).fetchone()
        return row[0] if row else None

    def _emit_event(
        self,
        *,
        event_type: str,
        project_id: str | None,
        entity_type: str | None,
        entity_id: str | None,
        payload: dict[str, Any],
        actor: str,
    ) -> dict[str, Any]:
        occurred_at = now_iso()
        prior_hash = self._latest_event_hash()
        body = {
            "event_type": event_type,
            "project_id": project_id,
            "entity_type": entity_type,
            "entity_id": entity_id,
            "payload": payload,
            "actor": actor,
            "occurred_at": occurred_at,
            "prior_hash": prior_hash,
        }
        event_hash = object_hash(body)
        event = {
            "event_id": new_id("evt"),
            **body,
            "event_hash": event_hash,
        }
        self.conn.execute(
            """
            INSERT INTO events(event_id, project_id, event_type, entity_type,
                               entity_id, payload_json, actor, occurred_at,
                               prior_hash, event_hash)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                event["event_id"],
                project_id,
                event_type,
                entity_type,
                entity_id,
                stable_json(payload),
                actor,
                occurred_at,
                prior_hash,
                event_hash,
            ),
        )
        return event

    def _validate_type(self, entity_type: str) -> None:
        if entity_type not in ENTITY_TYPES:
            raise KernelError(f"Unsupported entity type: {entity_type}")

    def _project_id_for(self, entity_type: str, payload: dict[str, Any]) -> str | None:
        if entity_type == "project":
            return payload.get("id")
        project_id = payload.get("project_id")
        if not project_id:
            raise KernelError(f"{entity_type} requires project_id")
        if not self.get("project", project_id):
            raise KernelError(f"Project does not exist: {project_id}")
        return project_id

    def create_project(
        self,
        title: str,
        objective: str,
        *,
        owner: str = "unassigned",
        scope: str = "",
        constraints: list[str] | None = None,
        actor: str = "system",
    ) -> dict[str, Any]:
        project_id = new_id("prj")
        payload = {
            "id": project_id,
            "title": title,
            "objective": objective,
            "owner": owner,
            "scope": scope,
            "constraints": constraints or [],
            "current_phase": "frame",
            "status": "draft",
            "next_gate": None,
        }
        return self.create("project", payload, actor=actor)

    def create(
        self,
        entity_type: str,
        payload: dict[str, Any],
        *,
        actor: str = "system",
    ) -> dict[str, Any]:
        self._validate_type(entity_type)
        payload = dict(payload)
        entity_id = payload.setdefault("id", new_id(entity_type[:3]))
        project_id = self._project_id_for(entity_type, payload)
        if entity_type == "project":
            payload.setdefault("status", "draft")
            payload.setdefault("current_phase", "frame")
        if entity_type == "evidence":
            state = payload.get("evidence_state", "open")
            if state not in EVIDENCE_STATES:
                raise KernelError(f"Invalid evidence state: {state}")
        timestamp = now_iso()
        status = payload.get("status")
        with self.transaction():
            existing = self.conn.execute(
                "SELECT id FROM entities WHERE id = ?", (entity_id,)
            ).fetchone()
            if existing:
                raise KernelError(f"Entity already exists: {entity_id}")
            self.conn.execute(
                """
                INSERT INTO entities(id, project_id, entity_type, status,
                                     payload_json, version, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, 1, ?, ?)
                """,
                (entity_id, project_id, entity_type, status, stable_json(payload), timestamp, timestamp),
            )
            self._emit_event(
                event_type="entity_created",
                project_id=project_id,
                entity_type=entity_type,
                entity_id=entity_id,
                payload={"after": payload, "version": 1},
                actor=actor,
            )
        return self.get(entity_type, entity_id)  # type: ignore[return-value]

    def get(self, entity_type: str, entity_id: str) -> dict[str, Any] | None:
        self._validate_type(entity_type)
        row = self.conn.execute(
            """
            SELECT id, project_id, entity_type, status, payload_json, version,
                   created_at, updated_at, deleted
            FROM entities WHERE id = ? AND entity_type = ?
            """,
            (entity_id, entity_type),
        ).fetchone()
        if not row or row["deleted"]:
            return None
        payload = json.loads(row["payload_json"])
        payload.update(
            {
                "id": row["id"],
                "project_id": row["project_id"],
                "entity_type": row["entity_type"],
                "version": row["version"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"],
            }
        )
        return payload

    def list_entities(
        self,
        entity_type: str,
        *,
        project_id: str | None = None,
        include_deleted: bool = False,
    ) -> list[dict[str, Any]]:
        self._validate_type(entity_type)
        query = "SELECT id FROM entities WHERE entity_type = ?"
        params: list[Any] = [entity_type]
        if project_id is not None:
            query += " AND project_id = ?"
            params.append(project_id)
        if not include_deleted:
            query += " AND deleted = 0"
        query += " ORDER BY created_at, id"
        rows = self.conn.execute(query, params).fetchall()
        result = []
        for row in rows:
            if include_deleted:
                raw = self.conn.execute(
                    "SELECT payload_json, id, project_id, entity_type, version, created_at, updated_at, deleted FROM entities WHERE id = ?",
                    (row[0],),
                ).fetchone()
                if raw:
                    item = json.loads(raw[0])
                    item.update({"id": raw[1], "project_id": raw[2], "entity_type": raw[3], "version": raw[4], "created_at": raw[5], "updated_at": raw[6], "deleted": bool(raw[7])})
                    result.append(item)
            else:
                item = self.get(entity_type, row[0])
                if item:
                    result.append(item)
        return result

    def update(
        self,
        entity_type: str,
        entity_id: str,
        patch: dict[str, Any],
        *,
        actor: str = "system",
    ) -> dict[str, Any]:
        current = self.get(entity_type, entity_id)
        if not current:
            raise KernelError(f"Entity does not exist: {entity_type}/{entity_id}")
        project_id = current.get("project_id")
        if entity_type == "project" and "status" in patch:
            self._check_transition(PROJECT_TRANSITIONS, current.get("status", "draft"), patch["status"], "project")
        if entity_type == "work_package" and "status" in patch:
            self._check_transition(WORK_PACKAGE_TRANSITIONS, current.get("status", "proposed"), patch["status"], "work package")
        if entity_type == "decision" and "status" in patch:
            self._check_transition(DECISION_TRANSITIONS, current.get("status", "open"), patch["status"], "decision")
        if entity_type == "gate" and "status" in patch:
            self._check_transition(GATE_TRANSITIONS, current.get("status", "not_ready"), patch["status"], "gate")
        if entity_type == "claim" and "evidence_state" in patch:
            if patch["evidence_state"] not in EVIDENCE_STATES:
                raise KernelError("Invalid claim evidence state")
            if patch["evidence_state"] != current.get("evidence_state") and not patch.get("evidence_upgrade_reason"):
                raise KernelError("Claim evidence-state changes require evidence_upgrade_reason")
        merged = dict(current)
        for key, value in patch.items():
            if key not in {"id", "entity_type", "project_id", "version", "created_at", "updated_at"}:
                merged[key] = value
        new_version = int(current["version"]) + 1
        timestamp = now_iso()
        with self.transaction():
            self.conn.execute(
                """
                UPDATE entities SET status = ?, payload_json = ?, version = ?, updated_at = ?
                WHERE id = ? AND entity_type = ?
                """,
                (merged.get("status"), stable_json(merged), new_version, timestamp, entity_id, entity_type),
            )
            self._emit_event(
                event_type="entity_updated",
                project_id=project_id,
                entity_type=entity_type,
                entity_id=entity_id,
                payload={"before": current, "after": merged, "version": new_version, "patch": patch},
                actor=actor,
            )
        return self.get(entity_type, entity_id)  # type: ignore[return-value]

    @staticmethod
    def _check_transition(table: dict[str, set[str]], current: str, target: str, label: str) -> None:
        if target == current:
            return
        if target not in table.get(current, set()):
            raise KernelError(f"Invalid {label} transition: {current} -> {target}")

    def link(
        self,
        project_id: str,
        src_type: str,
        src_id: str,
        relation: str,
        dst_type: str,
        dst_id: str,
        *,
        actor: str = "system",
    ) -> dict[str, Any]:
        self._validate_type(src_type)
        self._validate_type(dst_type)
        if relation not in RELATIONS:
            raise KernelError(f"Unsupported relation: {relation}")
        src = self.get(src_type, src_id)
        dst = self.get(dst_type, dst_id)
        if not src or not dst:
            raise KernelError("Both link endpoints must exist")
        if src.get("project_id") != project_id or dst.get("project_id") != project_id:
            raise KernelError("Link endpoints must belong to the supplied project")
        link_id = new_id("lnk")
        created_at = now_iso()
        with self.transaction():
            try:
                self.conn.execute(
                    """
                    INSERT INTO links(id, project_id, src_type, src_id, relation,
                                      dst_type, dst_id, created_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (link_id, project_id, src_type, src_id, relation, dst_type, dst_id, created_at),
                )
            except sqlite3.IntegrityError as exc:
                raise KernelError("Link already exists") from exc
            link = {
                "id": link_id,
                "project_id": project_id,
                "src_type": src_type,
                "src_id": src_id,
                "relation": relation,
                "dst_type": dst_type,
                "dst_id": dst_id,
                "created_at": created_at,
            }
            self._emit_event(
                event_type="link_created",
                project_id=project_id,
                entity_type=None,
                entity_id=None,
                payload=link,
                actor=actor,
            )
        return link

    def list_links(self, project_id: str) -> list[dict[str, Any]]:
        rows = self.conn.execute(
            "SELECT id, project_id, src_type, src_id, relation, dst_type, dst_id, created_at FROM links WHERE project_id = ? ORDER BY created_at, id",
            (project_id,),
        ).fetchall()
        return [dict(row) for row in rows]

    def events(self, project_id: str | None = None) -> list[dict[str, Any]]:
        query = "SELECT * FROM events"
        params: list[Any] = []
        if project_id:
            query += " WHERE project_id = ?"
            params.append(project_id)
        query += " ORDER BY sequence"
        rows = self.conn.execute(query, params).fetchall()
        result = []
        for row in rows:
            item = dict(row)
            item["payload"] = json.loads(item.pop("payload_json"))
            result.append(item)
        return result

    def verify_event_chain(self) -> bool:
        previous: str | None = None
        for event in self.events():
            body = {
                "event_type": event["event_type"],
                "project_id": event["project_id"],
                "entity_type": event["entity_type"],
                "entity_id": event["entity_id"],
                "payload": event["payload"],
                "actor": event["actor"],
                "occurred_at": event["occurred_at"],
                "prior_hash": event["prior_hash"],
            }
            if event["prior_hash"] != previous or object_hash(body) != event["event_hash"]:
                return False
            previous = event["event_hash"]
        return True

    def rebuild_projection(self, project_id: str) -> dict[tuple[str, str], dict[str, Any]]:
        """Reconstruct entities from entity event payloads for integrity testing."""
        projection: dict[tuple[str, str], dict[str, Any]] = {}
        for event in self.events(project_id):
            if event["event_type"] not in {"entity_created", "entity_updated"}:
                continue
            entity_type = event["entity_type"]
            entity_id = event["entity_id"]
            after = event["payload"].get("after")
            if after is not None:
                projection[(entity_type, entity_id)] = after
        return projection

    def advance_gate(
        self,
        gate_id: str,
        decision: str,
        *,
        authority: str,
        actor: str = "system",
        next_phase: str | None = None,
        loop_back_phase: str | None = None,
        unresolved_conditions: list[str] | None = None,
        rationale: str = "",
    ) -> dict[str, Any]:
        gate = self.get("gate", gate_id)
        if not gate:
            raise KernelError(f"Gate does not exist: {gate_id}")
        if decision not in {"proceed", "conditional_proceed", "loop_back", "descope", "pause", "stop"}:
            raise KernelError(f"Unsupported gate decision: {decision}")
        if decision in {"proceed", "conditional_proceed"} and next_phase not in PHASES:
            raise KernelError("A proceed decision requires a valid next_phase")
        if decision == "loop_back" and loop_back_phase not in PHASES:
            raise KernelError("A loop_back decision requires a valid loop_back_phase")
        current_status = gate.get("status", "not_ready")
        # Final decisions are only valid after the packet and review states have
        # been recorded. The convenience method records those transitions rather
        # than allowing callers to bypass the gate lifecycle.
        if current_status == "not_ready":
            self.update("gate", gate_id, {"status": "packet_prepared"}, actor=actor)
            current_status = "packet_prepared"
        if current_status == "packet_prepared":
            self.update("gate", gate_id, {"status": "review_in_progress"}, actor=actor)
        updated_gate = self.update(
            "gate",
            gate_id,
            {
                "status": decision,
                "decision": decision,
                "authority": authority,
                "rationale": rationale,
                "unresolved_conditions": unresolved_conditions or [],
                "next_phase": next_phase,
                "loop_back_phase": loop_back_phase,
            },
            actor=actor,
        )
        project_id = gate["project_id"]
        project = self.get("project", project_id)
        assert project is not None
        project_patch: dict[str, Any] = {"next_gate": gate_id}
        if decision in {"proceed", "conditional_proceed"}:
            project_patch["current_phase"] = next_phase
            if project["status"] == "draft":
                project_patch["status"] = "active"
        elif decision == "loop_back":
            project_patch["current_phase"] = loop_back_phase
        elif decision == "descope":
            project_patch["status"] = "paused"
        elif decision == "pause":
            project_patch["status"] = "paused"
        elif decision == "stop":
            project_patch["status"] = "stopped"
        if project_patch.get("status") and project["status"] == "draft":
            # A gate cannot move a draft directly to paused/stopped through an invalid transition.
            project_patch["status"] = "active" if decision == "pause" else project_patch["status"]
        self.update("project", project_id, project_patch, actor=actor)
        return updated_gate

    def continuation_packet(self, project_id: str) -> tuple[str, dict[str, Any]]:
        project = self.get("project", project_id)
        if not project:
            raise KernelError(f"Project does not exist: {project_id}")
        sections: dict[str, list[dict[str, Any]]] = {
            kind: self.list_entities(kind, project_id=project_id)
            for kind in [
                "objective",
                "factor",
                "evidence",
                "decision",
                "risk",
                "work_package",
                "claim",
                "gate",
                "artefact",
                "handoff",
                "review",
            ]
        }
        event_list = self.events(project_id)[-25:]
        data = {
            "project": project,
            **sections,
            "links": self.list_links(project_id),
            "recent_events": event_list,
            "event_chain_valid": self.verify_event_chain(),
            "open_questions": [
                item["statement"] for item in sections["factor"] if item.get("evidence_state") == "open"
            ],
            "next_actions": [
                item.get("acceptance", "")
                for item in sections["work_package"]
                if item.get("status") not in {"closed", "accepted"}
            ],
        }
        lines = [
            f"# Continuation Packet — {project['title']}",
            "",
            f"**Project ID:** `{project_id}`",
            f"**Status:** `{project.get('status')}`",
            f"**Current phase:** `{project.get('current_phase')}`",
            f"**Owner:** {project.get('owner')}",
            "",
            "## Objective",
            project.get("objective", ""),
            "",
            "## Scope and constraints",
            project.get("scope", "") or "Not recorded.",
        ]
        constraints = project.get("constraints", [])
        if constraints:
            lines.extend(["", "Constraints:", *[f"- {item}" for item in constraints]])
        for title, key in [
            ("Objectives", "objective"),
            ("Factors and open questions", "factor"),
            ("Evidence", "evidence"),
            ("Decisions", "decision"),
            ("Risks", "risk"),
            ("Work packages", "work_package"),
            ("Claims", "claim"),
            ("Gates", "gate"),
        ]:
            lines.extend(["", f"## {title}"])
            items = data[key]
            if not items:
                lines.append("None recorded.")
                continue
            for item in items:
                label = item.get("title") or item.get("statement") or item.get("question") or item.get("phase") or item.get("id")
                status = item.get("status", "")
                lines.append(f"- **{label}** `{status}` — `{item.get('id')}`")
                if item.get("permitted_wording"):
                    lines.append(f"  - Permitted wording: {item['permitted_wording']}")
                if item.get("limitations"):
                    lines.append(f"  - Limitations: {item['limitations']}")
                if item.get("rationale"):
                    lines.append(f"  - Rationale: {item['rationale']}")
        lines.extend(["", "## Next actions"])
        if data["next_actions"]:
            lines.extend([f"- {action}" for action in data["next_actions"]])
        else:
            lines.append("No unclosed work-package acceptance actions recorded.")
        lines.extend(["", "## Known open questions"])
        if data["open_questions"]:
            lines.extend([f"- {question}" for question in data["open_questions"]])
        else:
            lines.append("No factors currently marked open.")
        lines.extend([
            "",
            "## Integrity and continuity",
            f"Event chain valid: `{data['event_chain_valid']}`",
            f"Recent events retained: `{len(event_list)}`",
            "",
            "## Limitations",
            "This packet is a generated project-state view. It does not establish substantive correctness, legal authority, domain validation, or real-world safety.",
        ])
        return "\n".join(lines) + "\n", data

    def export_continuation(self, project_id: str, directory: str | Path) -> tuple[Path, Path]:
        directory = Path(directory)
        directory.mkdir(parents=True, exist_ok=True)
        markdown, data = self.continuation_packet(project_id)
        md_path = directory / f"continuation-{project_id}.md"
        json_path = directory / f"continuation-{project_id}.json"
        md_path.write_text(markdown, encoding="utf-8")
        json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        return md_path, json_path

    def close_project(self, project_id: str, *, actor: str = "system") -> dict[str, Any]:
        return self.update("project", project_id, {"status": "completed"}, actor=actor)

    def delete_as_tombstone(self, entity_type: str, entity_id: str, *, actor: str = "system") -> None:
        current = self.get(entity_type, entity_id)
        if not current:
            raise KernelError(f"Entity does not exist: {entity_type}/{entity_id}")
        with self.transaction():
            self.conn.execute(
                "UPDATE entities SET deleted = 1, version = version + 1, updated_at = ? WHERE id = ?",
                (now_iso(), entity_id),
            )
            self._emit_event(
                event_type="entity_tombstoned",
                project_id=current.get("project_id"),
                entity_type=entity_type,
                entity_id=entity_id,
                payload={"before": current},
                actor=actor,
            )


def seed_demo_kernel(db_path: str | Path = ":memory:") -> tuple[OperatingKernel, str]:
    """Create a small deterministic example used by tests and the CLI demo."""
    kernel = OperatingKernel(db_path)
    project = kernel.create_project(
        "Kernel calibration project",
        "Test whether structured continuity and traceability improve a bounded software project.",
        owner="autonomous-reference",
        scope="Local-first reference implementation and retrospective project calibration.",
        constraints=["No external side effects", "No unsupported claims of real-world validation"],
        actor="seed",
    )
    project_id = project["id"]
    kernel.update("project", project_id, {"status": "active"}, actor="seed")
    objective = kernel.create(
        "objective",
        {
            "project_id": project_id,
            "statement": "Preserve project state across context loss.",
            "success_condition": "A continuation packet can reconstruct the next action without raw conversation replay.",
            "priority": "high",
            "status": "open",
        },
        actor="seed",
    )
    factor = kernel.create(
        "factor",
        {
            "project_id": project_id,
            "statement": "Structured records may add coordination burden.",
            "category": "cost",
            "consequence": "The workflow may be too heavy for small projects.",
            "evidence_state": "hypothesis",
            "treatment": "Measure burden during calibration.",
            "status": "open",
        },
        actor="seed",
    )
    evidence = kernel.create(
        "evidence",
        {
            "project_id": project_id,
            "proposition": "The kernel can store a resumable project state.",
            "source": "Reference implementation test",
            "method": "Automated integration test",
            "conditions": "SQLite local workspace",
            "evidence_state": "measured_locally",
            "limitations": "Does not establish usefulness in a real team.",
        },
        actor="seed",
    )
    decision = kernel.create(
        "decision",
        {
            "project_id": project_id,
            "question": "Where should the first kernel slice begin?",
            "options": ["Structured continuity", "Full multi-agent orchestration"],
            "selected_option": "Structured continuity",
            "rationale": "It reduces the risk of building an oversized system before calibration.",
            "rejected_alternatives": ["Full multi-agent orchestration: too broad for first proof."],
            "authority": "autonomous design decision",
            "status": "accepted",
        },
        actor="seed",
    )
    work = kernel.create(
        "work_package",
        {
            "project_id": project_id,
            "objective": "Implement and test the minimum kernel contract.",
            "question": "Can the reference kernel preserve traceable state?",
            "inputs": ["minimum-operational-contract-v0.2.md"],
            "exclusions": ["Remote execution", "Production multi-tenant security"],
            "evidence_contract": "Automated tests plus generated continuation packet.",
            "acceptance": "All minimum acceptance tests pass.",
            "owner": "autonomous-reference",
            "reviewer": "adversarial-test-suite",
            "status": "in_progress",
        },
        actor="seed",
    )
    claim = kernel.create(
        "claim",
        {
            "project_id": project_id,
            "statement": "The reference kernel preserves a traceable project state locally.",
            "scope": "This implementation and its automated tests.",
            "evidence_state": "measured_locally",
            "permitted_wording": "The local reference tests demonstrate state preservation under the tested conditions.",
            "limitations": "No external validation or multi-contributor test yet.",
            "status": "open",
        },
        actor="seed",
    )
    for src_type, src_id, relation, dst_type, dst_id in [
        ("objective", objective["id"], "addresses", "factor", factor["id"]),
        ("evidence", evidence["id"], "supports", "claim", claim["id"]),
        ("decision", decision["id"], "addresses", "work_package", work["id"]),
        ("work_package", work["id"], "produces", "evidence", evidence["id"]),
    ]:
        kernel.link(project_id, src_type, src_id, relation, dst_type, dst_id, actor="seed")
    return kernel, project_id
