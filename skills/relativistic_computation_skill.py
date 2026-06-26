# skills/relativistic_computation_skill.py

from tools.relativistic_math_tool import (
    compute_gravitational_time_dilation,
    TimeDilationInput,
)


class RelativisticComputationSkill:
    """
    Performs GR and SR calculations using the relativistic math tool.
    """

    def compute_time_dilation(self, mass_kg: float, radius_m: float):
        result = compute_gravitational_time_dilation(
            TimeDilationInput(
                mass_kg=mass_kg,
                radius_m=radius_m,
            )
        )
        return {
            "factor": result.factor,
            "description": result.description,
        }
