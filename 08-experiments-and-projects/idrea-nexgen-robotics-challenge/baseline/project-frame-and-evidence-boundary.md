# IDREA Project Frame and Evidence Boundary

## Status

**Status:** Corrected baseline, not an architecture selection.

**Project:** IDREA NeX-Gen Robotics Challenge.

**Purpose:** Establish the starting frame for applying the Universal Virtual Enterprise workflow to the supplied robotics challenge.

## 1. Supplied challenge

The supplied challenge is to design and develop a battery-powered robotic prototype capable of stable locomotion and controlled multi-axis traversal across vertical and non-planar surfaces. The official challenge page states that the prototype should integrate mechanical design, control architecture, and energy management and align with inspection, maintenance, and industrial automation applications. [1]

The official rulebook identifies three target-surface categories: ferromagnetic vertical structures, non-ferromagnetic surfaces such as carbon fibre and painted surfaces, and cylindrical vertical geometries such as pipes, towers, and columnar systems. [2]

The challenge therefore enters the enterprise as a **given project/problem statement**. The framework must not replace it with an unrelated upstream problem. It must, however, decompose it, clarify its meaning, identify the mission and operating implications, and test whether the supplied scope is internally coherent.

## 2. Literal official requirements

The following are recorded as official rulebook requirements or evaluation statements. They are not yet engineering feasibility conclusions.

| Requirement area | Literal requirement | Evidence state |
|---|---|---|
| Vertical mobility | Stable 90° vertical movement and controlled ascent/descent. | Verified official |
| Planar traversal | Controlled traversal across planar vertical surfaces. | Verified official |
| Cylindrical traversal | Controlled traversal across curved cylindrical geometries. | Verified official |
| Motion modes | Axial translation, circumferential traversal, and lateral translation. | Verified official |
| Vertical distance | Minimum successful vertical traversal of 10 m. | Verified official |
| Payload | Minimum payload of 1.5 kg during operation. | Verified official |
| Control | Embedded microcontroller or SBC; tele-operated and/or semi-autonomous functionality. | Verified official |
| Power | Fully onboard battery system for sustained operation. | Verified official |
| Failsafe | Controlled shutdown or recovery during power or communication failure; protection against sudden detachment and instability. | Verified official |
| Surface interaction | No surface damage, material degradation, or unsafe interaction. | Verified official |
| Evaluation | Mobility, control precision/reliability, multi-surface adaptability, efficiency, innovation, engineering depth, feasibility, and simulation-backed validation. | Verified official |
| Round 1 submission | Maximum 10-slide presentation, excluding the cover slide; PPT/PDF. | Verified official |
| Later rounds | Technical review/documentation and prototype-readiness or physical-prototype demonstrations. | Verified official |

The official challenge page lists Round 1 as 28 August 2026 and states that the Round 1 submission is a PPT of not more than 10 slides. [1] The project’s inherited continuity file additionally recorded a user-stated requirement for a maximum two-page PDF abstract. That abstract requirement is **user-stated / unresolved official status** and must not be silently treated as rulebook fact.

## 3. User intent and strategic constraints

The user’s stated strategy is not to optimise only for Round 1 selection. The intended output is a technically deep, defensible concept with sufficient groundwork that physical prototyping could begin immediately if funding became available. The user also stated that funding constraints may prevent proceeding to later rounds.

The canonical body of work must therefore be deeper than the compressed competition artefacts. The abstract and presentation, if produced, must be derived views and must not contain claims stronger than the underlying evidence.

## 4. What has and has not been established

The project has established the literal challenge frame and a preliminary set of likely architecture-driving conflicts. It has not yet established the real operating landscape, representative surface conditions, evaluation apparatus, acceptable safety implementation, detailed mass budget, energy budget, adhesion physics, control architecture, or the feasibility of any candidate mechanism.

The inherited factor catalogue contains useful hypotheses about magnetic adhesion, vacuum/airflow adhesion, geometry adaptation, payload-power coupling, and failsafe behaviour. These are **design-space hypotheses and research prompts**, not final findings. The previous task also contained unsupported statements about current inspection workflows, existing robotic alternatives, and real-world failure consequences; those statements must be re-researched before being used as facts.

## 5. Candidate families currently quarantined as hypotheses

The following families appeared in the inherited task. They remain available for later comparison but have no selected status:

| Candidate family | Current status | What must be established before comparison |
|---|---|---|
| Suction/airflow hybrid with articulated chassis | Hypothesis | Downforce under relevant surface conditions, power, mass, noise, failure behaviour, curvature adaptation, surface interaction, and recovery. |
| Multi-modal magnetic plus dry-adhesive/spine system | Hypothesis | Material compatibility, contamination tolerance, switching, force margin, damage risk, curvature, payload, and passive failure behaviour. |
| Soft/reconfigurable conforming robot | Hypothesis | Payload capability, structural efficiency, control, energy, repeatability, manufacturing, failure behaviour, and evidence from comparable systems. |

No family may become the preferred architecture merely because it appears intuitive, innovative, or compatible with one surface category.

## 6. Required evidence boundary

The project must distinguish the following before making architecture claims:

- **Verified official:** Directly stated by the official challenge page or rulebook.
- **Verified external:** Supported by a traceable external source relevant to the claim.
- **Derived calculation:** Produced from explicit equations, inputs, assumptions, and uncertainty.
- **Measured locally:** Observed in a controlled local test with configuration and conditions recorded.
- **Design inference:** A reasoned implication of verified requirements and evidence.
- **Hypothesis:** A candidate explanation or design proposition awaiting evidence.
- **Estimate:** A quantitative or qualitative approximation with stated method and uncertainty.
- **Open:** Not yet known or not yet researched sufficiently.
- **Excluded:** Deliberately outside the present scope, with rationale.

## 7. Immediate next decision gate

The next gate is not “which adhesion mechanism should we select?” It is:

> **Is the problem, operating context, evaluation context, and architecture-changing factor space understood well enough to begin disciplined architecture comparison?**

To reach that gate, the project must research and map the problem landscape, operating environments, relevant surface/material/geometry classes, inspection or automation use cases, existing solution families, safety consequences, evaluation conditions, and the physics/resource factors that can overturn the architecture.

## References

[1] [IDREA NeX-Gen Robotics Challenge](https://idrea.org/robotic-challenge/)

[2] [IDREA Technical Rulebook and Competition Guidelines](https://idrea.org/robotic-challenge/wp-content/uploads/2026/06/Technical-Rulebook-and-Competition-Guidelines.pdf)

[3] [Universal Enterprise Blueprint v2.0](../../../02-canonical-architecture/drafts/universal-enterprise-blueprint-v2.0.md)

[4] [Referenced task artefacts](../source/referenced-task-80HbnErd57jvZt90n0TbkD/)
