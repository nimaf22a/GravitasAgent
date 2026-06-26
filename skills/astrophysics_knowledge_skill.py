# skills/astrophysics_knowledge_skill.py

from tools.astrophysics_lookup_tool import get_astro_constant


class AstrophysicsKnowledgeSkill:
    """
    Retrieves astrophysical constants and reference data.
    """

    def lookup(self, name: str):
        try:
            value = get_astro_constant(name)
            return {
                "name": name,
                "value": value,
                "description": f"Retrieved astrophysical constant '{name}'.",
            }
        except KeyError:
            return {
                "error": f"Constant '{name}' not found.",
                "available_constants": ["solar_mass_kg", "earth_mass_kg", "sgr_a_star_mass_kg"],
            }
