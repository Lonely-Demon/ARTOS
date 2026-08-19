# Open-Source Harness Component Audit v0

**Date:** 2026-08-19
**Purpose:** Evaluate candidate open-source harnesses against the Universal Enterprise operating contract rather than selecting by popularity alone.

## Evidence boundary

This audit uses current public GitHub repository metadata and README material retrieved through the GitHub API on 2026-08-19. Repository popularity, activity, and README claims are signals of ecosystem maturity and declared capability; they are not proof of security, reliability, agent quality, or suitability for this architecture. No candidate has been installed, executed, penetration-tested, or independently benchmarked in this audit.

## Initial repository signals

| Candidate | Repository | Stars | Forks | License signal | Recent public activity | Declared role in this audit |
|---|---|---:|---:|---|---|---|
| DeerFlow | `bytedance/deer-flow` | 80,308 | 11,010 | MIT | Active on 2026-08-19 | Long-horizon research/execution harness |
| OpenManus | `FoundationAgents/OpenManus` | 58,013 | 10,072 | MIT | Active on 2026-08-16 | General agent and multi-agent experimentation |
| OpenHands | `OpenHands/OpenHands` | 84,470 | 11,000 | MIT | Active on 2026-08-19 | Coding/implementation worker |
| Hermes Agent | `NousResearch/hermes-agent` | 232,866 | 46,524 | MIT | Active on 2026-08-19 | Personal coordinator / agent environment candidate |
| OpenClaw | `openclaw/openclaw` | 386,776 | 81,262 | NOASSERTION in API metadata | Active on 2026-08-19 | Personal assistant / gateway candidate |

These metrics must not be treated as a ranking of enterprise suitability. High issue counts and high popularity may indicate adoption, scope, or maintenance burden as well as strength.

## DeerFlow

DeerFlow’s public README describes a long-horizon SuperAgent harness with research, coding, sandboxes, memories, tools, skills, subagents, a message gateway, scheduled tasks, browser control, and observability integrations. It therefore appears to be the strongest candidate for a **research/execution worker substrate** rather than the enterprise governance kernel.

The same README explicitly warns that high-privilege capabilities include system command execution, resource operations, and business-logic invocation, and that the default deployment model is a local trusted environment bound to loopback. It states that gateway administration is equivalent to code execution on the host and recommends additional authentication, network isolation, and allowlisting for non-local deployment. This is highly relevant: DeerFlow may be useful behind the operating kernel, but must not become the authority layer or be exposed directly as an unrestricted deployed enterprise service.

The integration stance is therefore: **candidate worker, not source of truth**. The kernel must own project state, approvals, evidence admission, scope, identity, policy, side-effect budgets, and continuity. DeerFlow would receive scoped work packages and return artefacts/evidence for review. Its own memory and sandbox facilities must be mapped to the kernel’s project-local memory and provenance rules before trust is granted.

## Initial decision

No candidate is selected as the universal coordinator at this stage. The reference kernel remains independent of any candidate. The next audit step is to inspect the remaining README claims, source layout, setup/deployment requirements, security boundaries, test coverage, and licensing notices, then create capability contracts and a weighted evaluation matrix. Installation will be considered only after the matrix identifies a bounded worker experiment that does not require exposing the kernel or granting unrestricted side effects.

## OpenHands Agent Canvas

OpenHands currently presents Agent Canvas as a self-hosted developer control center that can run OpenHands, Claude Code, Codex, Gemini, or other ACP-compatible agents across local, remote, cloud, Docker, VM, and company infrastructure backends. Its public README also describes automations triggered by schedules or webhooks and integrations with services such as Slack, GitHub, Linear, Notion, and Datadog.

This makes OpenHands the strongest candidate for a **software implementation and automation worker plane**. It should not own canonical requirements, evidence admission, approvals, or project-state truth. Its README explicitly warns that running without a sandbox grants the agent full filesystem access; even its Docker mode grants access to all projects under the configured project path. The kernel must therefore issue narrowly scoped work packages, use isolated workspaces, constrain repository paths, capture build/test provenance, and admit returned changes only through review and policy checks.

Provisional role: **coding/implementation worker plane**, subject to sandbox, repository, credential, and side-effect experiments.

## OpenManus

OpenManus describes itself as a simple open implementation of a general AI agent. Its current README provides browser automation through Browser Use MCP, local or cloud browser choices, a general agent, a data-analysis agent, and an unstable multi-agent flow. It is easy to experiment with and has MIT licensing, but the README’s own wording and configuration suggest a relatively direct agent runtime rather than a mature governance or enterprise coordination substrate.

Provisional role: **experimental general-purpose worker and browser/data-analysis capability**, not the primary coordinator or assurance layer. It may be useful for comparative experiments because its surface is simpler than the larger harnesses, but its multi-agent mode must be treated as experimental until tested.

## Hermes Agent

Hermes describes a personal agent with persistent memory, user modelling, self-created skills, multiple model providers, terminal backends including local/Docker/SSH/Singularity/Modal/Daytona/Vercel Sandbox, messaging gateways, scheduled automations, parallel subagents, and MCP integration. The README also points to command approval, DM pairing, and container isolation in its security documentation.

Hermes is the strongest candidate for a **personal interaction and coordination interface**, especially for continuity across local and remote conversations. However, its self-improving memory, skills, messaging gateway, scheduled execution, and secret migration features create a large trust surface. It should sit outside the canonical kernel and interact through scoped APIs or task packages. Its memory must not become the authoritative project memory until project isolation, provenance, conflict handling, deletion, and claim-admission tests pass.

Provisional role: **human-facing coordinator/interface candidate**, not the governance spine.

## OpenClaw

OpenClaw presents itself as a single-operator personal assistant with a Gateway serving sessions, tools, events, and channel connections. It supports tools, skills, plugins, messaging channels, companion apps, device nodes, and local or hosted model providers. Its README explicitly says inbound messages are untrusted and warns that tools run on the host for the main session unless sandboxing is configured; it directs users to security, exposure, and sandboxing guides before remote exposure or multi-user connections.

OpenClaw is therefore a **personal gateway and channel interface candidate**, not a universal enterprise coordinator. Its single-operator design aligns with a personal front door but not with multi-project authority, independent assurance, or specialist-cell governance. Its tool and plugin model would require strict wrapping and provenance controls.

## Provisional component map

| Enterprise capability | Candidate fit | Provisional use | Mandatory kernel boundary |
|---|---|---|---|
| Canonical project state, evidence, gates, authority | None of the candidates | Implement independently in the reference kernel | Kernel remains source of truth and approval authority |
| Long-horizon research and broad execution | DeerFlow | Scoped research/execution worker | Isolated task package, sandbox, evidence admission, no direct authority |
| Coding and implementation | OpenHands | Coding worker plane | Repository/workspace scoping, test/provenance capture, review before merge |
| Personal interaction and persistent user-facing continuity | Hermes | Coordinator/interface experiment | Project-local memory, permission boundary, no automatic claim admission |
| Personal channels and device gateway | OpenClaw | Optional front-door/channel experiment | Single-operator boundary, pairing/authentication, tool sandboxing |
| Simple general/browser/data-analysis experiments | OpenManus | Comparative worker experiment | Treat multi-agent mode as experimental; isolate browser and credentials |

## Current selection decision

The architecture will not be replaced by any candidate. The reference kernel remains the control plane. The first actual integration experiment should be **OpenHands or DeerFlow behind a scoped work-package adapter**, not Hermes or OpenClaw as the core. The choice between OpenHands and DeerFlow should be made by a bounded local experiment after documenting the adapter contract, not by repository popularity.
