# IDREA NeX-Gen Robotics Challenge: Working Continuity State

**Project:** NeX-Gen Robotics Challenge Submission
**Last updated:** 20 August 2026
**Purpose:** Durable state for resuming work after conversation compaction or in a new AI conversation.

> This file is a structured state record, not a raw conversation transcript. It preserves what matters for continuing the work: goals, decisions, rationale, constraints, source hierarchy, open questions, and the current next step.

## 1. Overall Objective
The user is participating in the IDREA NeX-Gen Robotics Challenge. The competition requires designing a battery-powered robotic platform capable of stable, controlled multi-axis traversal on vertical and non-planar surfaces (ferromagnetic, non-ferromagnetic, and cylindrical).

**Strategic Goal:** The user does not intend to proceed past Round 1 due to funding constraints for physical prototyping. However, the objective is **not** to optimize merely for passing Round 1. The goal is to produce a "bulletproof concept" with rigorous groundwork and upstream research, ensuring that if funding were available, the team could immediately begin building a highly competitive, winning prototype.

**Immediate Deadline:** Round 1 submission is due tomorrow at 11:59 PM IST.
**Deliverables Required:**
1. Project Abstract (Maximum 2 pages, PDF)
2. Concept Presentation (Maximum 10 content slides, PPT/PPTX/PDF)

## 2. Collaboration Contract & Operating Model (Correction)
The previous interaction violated the established Universal Virtual Enterprise framework by jumping straight from a shallow reading of the rulebook to proposing candidate mechanisms (vortex, active suction, dry adhesives).

**The corrected operating model is:**
1. **Quarantine premature solutions:** The previous mechanism suggestions are quarantined. We do not yet know enough about the problem, the operating context, the consequences of failure, or the evaluation criteria to select an architecture.
2. **Reconstruct the real challenge:** We must understand the causal problem the competition is trying to solve, beyond the wording of the prompt. Who are the stakeholders? What is the operating environment? What are the consequences of failure?
3. **Map the landscapes:** We must map the problem, solution, operational, technical, and evaluation landscapes before making decisions.
4. **Build the factor catalogue:** Every important variable, constraint, and unknown must be explicitly listed and connected to decisions and consequences.
5. **Compare architectures systematically:** Only after the factors are mapped and triaged will we define requirements and compare architecture families against explicit criteria.
6. **Produce the canonical output first:** We will produce the rigorous, physics-backed, prototype-ready technical design before compressing it into the 2-page abstract and 10-slide presentation.

## 3. Extracted Fact Base (Rulebook Constraints - Literal)
*Note: These are literal constraints from the rulebook. Their implications and hidden dependencies have not yet been mapped.*

- **Mobility:** 90° vertical climbing/descent, circumferential traversal (cylinders), lateral translation. Minimum 10 meters vertical distance.
- **Payload:** Minimum 1.5 kg onboard payload.
- **Power:** Fully onboard battery; no tethers.
- **Surfaces:** Ferromagnetic (steel), Non-ferromagnetic (composites/painted), Cylindrical (pipes/towers).
- **Control:** Embedded control platform (microcontroller or SBC); tele-operated or semi-autonomous.
- **Safety:** Failsafe mechanisms for power/communication loss; no surface damage allowed.
- **Failure Conditions:** Loss of stability/control, inability to climb, power failure, failsafe failure, or unsafe behavior.
- **Round 1 Evaluation:** Clarity of concept, innovation in adhesion/locomotion, feasibility, simulation-backed validation.

## 4. Problem Formation: Reconstructing the Real Challenge
The competition asks for a robot that can climb steel, composite, and cylindrical structures carrying a 1.5kg payload.

**What is the real problem this solves?**
This describes an industrial inspection and maintenance robot for complex infrastructure like wind turbine towers (steel/composite, cylindrical), chemical storage tanks (steel, curved), or offshore oil rigs (steel, painted, cylindrical).

**Why is this hard?**
1. **The Multi-Surface Contradiction:** Ferromagnetic adhesion (magnetic wheels/tracks) is highly reliable, energy-efficient (permanent magnets require no power to hold), and standard for steel tanks. However, it fails completely on non-ferromagnetic surfaces (composites, thick paint).
2. **The Geometry Contradiction:** Flat walls require a rigid chassis for stability. Cylindrical pipes require an articulated or conforming chassis to maintain contact area.
3. **The Power/Payload Contradiction:** Non-magnetic adhesion (e.g., active vacuum) requires significant continuous power to maintain a seal, especially with a 1.5kg payload and its own battery weight, drastically reducing runtime and increasing the risk of catastrophic failure if power is lost.
4. **The Failsafe Requirement:** The rules mandate safe recovery during power loss. An active vacuum system drops the robot if power fails. A passive magnetic system stays attached. How do you fail-safe a non-magnetic climber?

## 5. Current Recommended Next Step
The immediate next step is to **map the operational and technical landscapes** for industrial inspection robots. We need to research the real-world operating environments (wind turbines, storage tanks, ship hulls) to understand the surface conditions (roughness, coatings, curvature, environmental factors like wind/moisture) that the rulebook implies but doesn't explicitly state.

We must also map the physics of adhesion and locomotion to build the factor catalogue (e.g., friction coefficients, required normal force for a 1.5kg payload + robot mass, power consumption of active vs. passive systems).

Only after mapping these landscapes will we be able to define the requirements and begin comparing architecture families.

## 6. Recovery Instructions for a New Conversation
If this file is reopened in a new session:
1. Read this continuity state in full.
2. Acknowledge that the project is operating under the strict Universal Virtual Enterprise framework. Do not jump to solutions.
3. Resume from the current phase: mapping the operational and technical landscapes to build the factor catalogue and evidence map.
