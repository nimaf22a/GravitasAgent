# skills/relativity_scenario_skill.py

from tools.scenario_builder_tool import build_scenario_from_nl
from tools.physics_validation_tool import validate_physical_params, ValidationInput


class RelativityScenarioSkill:
    """
    Converts natural-language descriptions into structured GR scenarios.
    """

    def run(self, description: str):
        scenario = build_scenario_from_nl(description)

        mass = scenario.get("central_mass_kg")
        radius = scenario.get("radius_m")
        velocity = scenario.get("velocity_m_s", 0.0)

        validation = validate_physical_params(
            ValidationInput(
                mass_kg=mass,
                radius_m=radius,
                velocity_m_s=velocity,
            )
        )

        return {
            "scenario": scenario,
            "validation": {
                "is_valid": validation.is_valid,
                "issues": validation.issues,
                "suggestions": validation.suggestions,
            },
        }
