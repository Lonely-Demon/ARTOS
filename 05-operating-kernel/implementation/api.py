"""Local-only HTTP adapter for the operating-kernel reference slice.

This API is intentionally unauthenticated and must bind to 127.0.0.1 only.
It is for local development and adapter experiments, not remote deployment.
"""
from __future__ import annotations

import os
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from kernel import KernelError, OperatingKernel


DEFAULT_DB = os.environ.get("KERNEL_DB", str(Path(__file__).parent / "kernel.sqlite3"))


def create_app(db_path: str = DEFAULT_DB) -> FastAPI:
    kernel = OperatingKernel(db_path)

    @asynccontextmanager
    async def lifespan(_app: FastAPI):
        yield
        kernel.close()

    app = FastAPI(title="Universal Enterprise Operating Kernel", version="0.1-reference", lifespan=lifespan)
    app.state.kernel = kernel

    @app.exception_handler(KernelError)
    async def kernel_error_handler(_, exc: KernelError):
        return JSONResponse(status_code=400, content={"error": str(exc), "type": "kernel_contract_error"})

    @app.get("/health")
    def health() -> dict[str, Any]:
        return {
            "status": "ok",
            "service": "operating-kernel-reference",
            "event_chain_valid": kernel.verify_event_chain(),
            "external_side_effects": False,
            "authority": "local-reference-only",
        }

    @app.post("/projects")
    def create_project(body: dict[str, Any]) -> dict[str, Any]:
        return kernel.create_project(
            body["title"],
            body["objective"],
            owner=body.get("owner", "unassigned"),
            scope=body.get("scope", ""),
            constraints=body.get("constraints", []),
            actor=body.get("actor", "api"),
        )

    @app.get("/projects/{project_id}")
    def get_project(project_id: str) -> dict[str, Any]:
        project = kernel.get("project", project_id)
        if not project:
            raise HTTPException(status_code=404, detail="Project not found")
        return project

    @app.get("/projects/{project_id}/packet")
    def get_packet(project_id: str) -> dict[str, Any]:
        markdown, data = kernel.continuation_packet(project_id)
        return {"markdown": markdown, "data": data}

    @app.get("/projects/{project_id}/events")
    def get_events(project_id: str) -> list[dict[str, Any]]:
        if not kernel.get("project", project_id):
            raise HTTPException(status_code=404, detail="Project not found")
        return kernel.events(project_id)

    @app.post("/entities/{entity_type}")
    def create_entity(entity_type: str, body: dict[str, Any]) -> dict[str, Any]:
        actor = body.pop("_actor", "api")
        return kernel.create(entity_type, body, actor=actor)

    @app.get("/projects/{project_id}/entities/{entity_type}")
    def list_entities(project_id: str, entity_type: str) -> list[dict[str, Any]]:
        if not kernel.get("project", project_id):
            raise HTTPException(status_code=404, detail="Project not found")
        return kernel.list_entities(entity_type, project_id=project_id)

    @app.post("/projects/{project_id}/links")
    def create_link(project_id: str, body: dict[str, Any]) -> dict[str, Any]:
        return kernel.link(
            project_id,
            body["src_type"],
            body["src_id"],
            body["relation"],
            body["dst_type"],
            body["dst_id"],
            actor=body.get("actor", "api"),
        )

    @app.post("/gates/{gate_id}/advance")
    def advance_gate(gate_id: str, body: dict[str, Any]) -> dict[str, Any]:
        return kernel.advance_gate(
            gate_id,
            body["decision"],
            authority=body["authority"],
            actor=body.get("actor", "api"),
            next_phase=body.get("next_phase"),
            loop_back_phase=body.get("loop_back_phase"),
            unresolved_conditions=body.get("unresolved_conditions", []),
            rationale=body.get("rationale", ""),
        )

    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("api:app", host="127.0.0.1", port=8787, reload=False)
