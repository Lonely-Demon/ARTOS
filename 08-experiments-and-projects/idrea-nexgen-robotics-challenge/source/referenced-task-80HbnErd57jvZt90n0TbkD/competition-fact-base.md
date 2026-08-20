# IDREA NeX-Gen Robotics Challenge: Fact Base and Uncertainty Register

## 1. Competition Overview
- **Objective:** Design and develop a battery-powered robotic prototype capable of stable locomotion and controlled multi-axis traversal across vertical and non-planar surfaces.
- **Application Alignment:** Inspection, maintenance, and industrial automation.
- **Organizer:** IDREA (International Decarbonization and Renewable Energy Association).
- **Prize:** ₹1,00,000 cash prize for the winning team (up to 6 members), potential job offers, and industry deployment support.

## 2. Technical Requirements

### 2.1 Locomotion & Target Surfaces
- **Motion Types:** 90° vertical climbing/descent, circumferential traversal (around cylinders), and lateral translation (sideways on vertical planes).
- **Distance:** Must successfully traverse a minimum vertical distance of 10 meters.
- **Surface Types:**
  - Ferromagnetic vertical structures (e.g., structural steel, tanks).
  - Non-ferromagnetic surfaces (e.g., carbon fiber, painted/coated surfaces).
  - Cylindrical vertical geometries (e.g., pipes, towers) with varying diameters.

### 2.2 Payload & Power
- **Payload:** Must carry a minimum payload of 1.5 kg during operation (simulating cameras, sensors, etc.).
- **Power System:** Fully onboard battery system. No external power tethers allowed.

### 2.3 Control & Safety
- **Control Architecture:** Embedded control platform (microcontroller or SBC).
- **Operation Modes:** Tele-operated or semi-autonomous.
- **Safety/Failsafe:** Must include controlled shutdown/recovery during power/communication failure, safeguards against sudden detachment, and protection against instability.

## 3. Constraints & Failure Conditions
- **Independence:** Fully self-contained, no external physical support.
- **Damage:** No surface damage or material degradation allowed.
- **Failure Triggers:** Loss of stability/control, inability to climb, power failure, failsafe failure, or unsafe behavior.

## 4. Submission Timeline and Artifacts

### Round 1: Concept Presentation
- **Date:** 28th August 2026 (Online)
- **Deadline per User:** Tomorrow at 11:59 PM IST.
- **Submission Requirements:** 
  - Presentation (PPT/PDF, max 10 slides excluding cover).
  - Project Abstract (max 2 pages, PDF format) — *Note: Abstract mentioned by user, not explicitly in the rulebook text extracted, but must be fulfilled.*
- **Content:** High-level design, innovation in adhesion/locomotion, feasibility, and simulation-backed validation (images/videos preferred).

### Round 2: Design Validation & Prototype Readiness
- **Date:** 27th November 2026 (Hybrid)
- **Submission:** Technical Presentation (max 15 slides), Engineering Documentation (PDF, ~20-25 pages), and Prototype Demonstration (live or video showing 80% completion).

### Round 3: Prototype Demonstration (Final Round)
- **Date:** December 2026 – January 2027 (Offline in Chennai)
- **Submission:** Physical working prototype + Complete Technical Package.

## 5. Uncertainty Register & Strategic Implications

1. **Abstract Requirement Discrepancy:** The user mentioned a "Project Abstract-Maximum 2 Pages, in PDF format" due tomorrow, but the official rulebook only mentions the 10-slide PPT for Round 1. *Strategy: We will produce both the 2-page abstract and the 10-slide presentation to ensure full compliance with the user's constraints.*
2. **Adhesion Mechanism for Multi-Surface:** The robot must traverse both ferromagnetic (steel) and non-ferromagnetic (composite/painted) vertical surfaces. Magnetic wheels/tracks alone will fail on non-ferromagnetic surfaces. Vacuum/suction, micro-spines, or hybrid systems are required. *Strategy: Upstream research must immediately focus on hybrid adhesion mechanisms capable of 1.5kg payload on vertical non-porous and porous/composite surfaces.*
3. **Curved vs. Flat Translation:** The robot must handle both flat walls and pipes. *Strategy: The mechanical chassis must likely be articulated or use omnidirectional/holonomic mobility (e.g., mecanum wheels with vacuum, or segmented tracks) to handle varying curvatures.*
4. **Simulation Requirement:** Round 1 heavily prefers "Simulation-backed validation of the concept". Since we are building a bulletproof concept without immediate physical prototyping, we need to generate rigorous mathematical models, force calculations (friction, payload torque, vacuum requirements), and conceptual CAD/diagrams to substitute for physical simulation software output.
