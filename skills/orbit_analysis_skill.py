# skills/orbit_analysis_skill.py

from tools.orbit_simulation_tool import (
    simulate_circular_orbit,
    OrbitParams,
)
from tools.physics_validation_tool import validate_physical_params, ValidationInput


class OrbitAnalysisSkill:
    """
    Simulates and analyzes orbital motion.
    """

    def simulate_orbit(self, mass_kg: float, radius_m: float, steps: int = 360):
        validation = validate_physical_params(
            ValidationInput(
                mass_kg=mass_kg,
                radius_m=radius_m,
                velocity_m_s=0.0,
            )
        )

        trajectory = simulate_circular_orbit(
            OrbitParams(
                central_mass_kg=mass_kg,
                radius_m=radius_m,
                steps=steps,
            )
        )

        return {
            "trajectory": trajectory.positions,
            "description": trajectory.description,
            "validation": {
                "is_valid": validation.is_valid,
                "issues": validation.issues,
                "suggestions": validation.suggestions,
            },
        }
