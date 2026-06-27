from typing import Dict

ASTRO_CONSTANTS: Dict[str, float] = {
    "solar_mass_kg": 1.98847e30,
    "earth_mass_kg": 5.9722e24,
    "sgr_a_star_mass_kg": 4.297e6 * 1.98847e30,  # ~4.3 million solar masses
}


def get_astro_constant(name: str) -> float:
    """
    Returns a known astrophysical constant by name.
    Raises KeyError if not found.
    """
    return ASTRO_CONSTANTS[name]
