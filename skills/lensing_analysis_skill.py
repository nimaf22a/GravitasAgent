# skills/lensing_analysis_skill.py

from tools.lensing_calculator_tool import (
    compute_light_deflection,
    LensingInput,
)
from tools.physics_validation_tool import validate_physical_params, ValidationInput


class LensingAnalysisSkill:
    """
    Computes gravitational lensing effects.
    """

    def compute_lensing(self, mass_kg: float, impact_parameter_m: float):
        validation = validate_physical_params(
            ValidationInput(
                mass_kg=mass_kg,
                radius_m=impact_parameter_m,
                velocity_m_s=0.0,
            )
        )

        result = compute_light_deflection(
            LensingInput(
                lens_mass_kg=mass_kg,
                impact_parameter_m=impact_parameter_m,
            )
        )

        return {
            "deflection_rad": result.deflection_rad,
            "description": result.description,
            "validation": {
                "is_valid": validation.is_valid,
                "issues": validation.issues,
                "suggestions": validation.suggestions,
            },
        }
