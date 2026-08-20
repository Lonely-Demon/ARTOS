# Factor, Evidence, and Dependency Catalogue

## 1. Problem Landscape: The Current Workflow and Its Failures
*   **Current Human Workflow:** Vertical infrastructure inspection (wind turbines, storage tanks, bridges) relies heavily on rope access technicians and scaffolding. This is dangerous, slow, expensive, and limited by weather conditions.
*   **Current Robotic Alternatives:** 
    *   **Drones (UAVs):** Excellent for rapid, standoff visual assessment (e.g., screening a whole wind farm). However, they cannot carry heavy contact-based Non-Destructive Testing (NDT) payloads (like Ultrasound or GPR), cannot operate inside confined spaces easily, and are restricted by wind and ATEX (explosive atmosphere) regulations.
    *   **Magnetic Crawlers:** Highly reliable, power-efficient, and capable of carrying heavy payloads. However, they are strictly limited to ferromagnetic (steel) surfaces. They cannot climb concrete, composites (FRP), aluminum, or austenitic stainless steel (304/316).
    *   **Pure Vacuum Crawlers:** Can climb non-magnetic surfaces, but require a smooth, sealable surface to maintain a vacuum. They fail on rough concrete, brick, or highly irregular geometries.
    *   **Suction-and-Airflow Hybrids (e.g., HausBots AEROGRIP):** Generate continuous downforce without needing a perfect seal, allowing them to climb rough and non-magnetic surfaces. However, they require continuous, high power draw to maintain the airflow.

## 2. The Multi-Surface & Geometry Contradiction
The IDREA challenge explicitly requires traversal on:
1.  Ferromagnetic vertical structures (steel walls/tanks).
2.  Non-ferromagnetic surfaces (composites, painted).
3.  Cylindrical vertical geometries (pipes, towers).

**The Dependency Collision:**
*   To climb non-ferromagnetic surfaces, we must abandon passive magnetic adhesion.
*   To climb cylindrical geometries (curved), we must abandon rigid, flat vacuum pads.
*   Therefore, the system requires a hybrid or adaptable adhesion mechanism (like soft adhesive wheels, or segmented suction-and-airflow) mounted on an articulated or folding chassis that can conform to curves.

## 3. The Power and Failsafe Contradiction
*   **Constraint:** The robot must carry a 1.5kg payload and operate on an onboard battery.
*   **Constraint:** The robot must have failsafe mechanisms for power/communication failure to prevent sudden detachment.
*   **The Dependency Collision:** If we use active suction/airflow to climb non-magnetic surfaces, a power failure immediately stops the downforce generation, causing the robot (and its 1.5kg payload) to fall. 
*   **Resolution Requirement:** We must design a mechanical failsafe that does not rely on electrical power to deploy, or a redundant power architecture that guarantees a safe descent or static lock upon primary power loss.

## 4. Factor Catalogue

| Factor | Domain | Consequence if unresolved | Dependency / Trade-off |
| :--- | :--- | :--- | :--- |
| **Adhesion Type** | Mechanical / Physics | Robot cannot climb non-magnetic surfaces. | Active suction requires high power. Magnetic requires steel. Dry adhesives require clean surfaces. |
| **Chassis Rigidity** | Mechanical | Robot cannot conform to cylindrical pipes. | A folding/articulated chassis adds mechanical complexity and weight. |
| **Power Draw** | Energy | Battery drains too fast to reach 10m height. | Higher adhesion force requires higher power, requiring a heavier battery, requiring more adhesion force. |
| **Failsafe Mechanism** | Safety / Control | Robot falls during power loss, violating rules. | Must be passive or have a dedicated emergency capacitor/battery. Adds weight. |
| **Payload Capacity (1.5kg)** | Mechanical / Energy | Robot slips or stalls under load. | Increases normal force requirement, increasing power draw of the adhesion system. |

## 5. Architectural Alternatives to Compare (Next Phase)
1.  **Architecture A: Suction-and-Airflow Hybrid on an Articulated Chassis.** Uses directed airflow (like an inverted hovercraft) to generate downforce on any surface, mounted on a segmented chassis to handle curves. 
2.  **Architecture B: Multi-Modal (Magnetic + Dry Adhesive/Spines) on a Wheeled Chassis.** Uses switchable magnets for steel and gecko-inspired dry adhesives for composites.
3.  **Architecture C: Soft Reconfigurable Robot.** Uses soft robotics and pneumatic/vacuum actuation to conform to any shape and grip via soft suction cups.
