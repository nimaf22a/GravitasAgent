# skills/physics_validation_skill.py

from tools.physics_validation_tool import validate_physical_params, ValidationInput


class PhysicsValidationSkill:
    """
    Ensures physical validity of scenarios.
    """

    def validate(self, mass_kg: float, radius_m: float, velocity_m_s: float = 0.0):
        result = validate_physical_params(
            ValidationInput(
                mass_kg=mass_kg,
                radius_m=radius_m,
                velocity_m_s=velocity_m_s,
            )
        )
        return {
            "is_valid": result.is_valid,
            "issues": result.issues,
            "suggestions": result.suggestions,
        }
