from __future__ import annotations

import argparse
import json
from pathlib import Path

from kernel import OperatingKernel, seed_demo_kernel


def main() -> int:
    parser = argparse.ArgumentParser(description="Universal Enterprise operating-kernel reference slice")
    parser.add_argument("--db", default="kernel.sqlite3", help="SQLite database path")
    sub = parser.add_subparsers(dest="command", required=True)

    create = sub.add_parser("create-project")
    create.add_argument("title")
    create.add_argument("objective")
    create.add_argument("--owner", default="unassigned")
    create.add_argument("--scope", default="")

    sub.add_parser("seed-demo")

    packet = sub.add_parser("packet")
    packet.add_argument("project_id")
    packet.add_argument("--out", default="packets")

    events = sub.add_parser("events")
    events.add_argument("--project")

    verify = sub.add_parser("verify")
    verify.add_argument("--project")

    args = parser.parse_args()
    if args.command == "seed-demo":
        kernel, project_id = seed_demo_kernel(args.db)
        try:
            output_dir = Path("packets")
            md_path, json_path = kernel.export_continuation(project_id, output_dir)
            print(json.dumps({"project_id": project_id, "markdown": str(md_path), "json": str(json_path)}, indent=2))
        finally:
            kernel.close()
        return 0

    kernel = OperatingKernel(args.db)
    try:
        if args.command == "create-project":
            project = kernel.create_project(args.title, args.objective, owner=args.owner, scope=args.scope, actor="cli")
            print(json.dumps(project, indent=2))
        elif args.command == "packet":
            md_path, json_path = kernel.export_continuation(args.project_id, args.out)
            print(json.dumps({"markdown": str(md_path), "json": str(json_path)}, indent=2))
        elif args.command == "events":
            print(json.dumps(kernel.events(args.project), indent=2, ensure_ascii=False))
        elif args.command == "verify":
            print(json.dumps({"event_chain_valid": kernel.verify_event_chain()}, indent=2))
    finally:
        kernel.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
