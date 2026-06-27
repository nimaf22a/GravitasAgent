from dataclasses import dataclass

C = 3e8
G = 6.67430e-11


@dataclass
class LensingInput:
    lens_mass_kg: float
    impact_parameter_m: float


@dataclass
class LensingResult:
    deflection_rad: float
    description: str


def compute_light_deflection(inp: LensingInput) -> LensingResult:
    """
    Weak-field approximation for light deflection by a point mass:
    alpha ~= 4GM / (b c^2)
    """
    alpha = 4 * G * inp.lens_mass_kg / (inp.impact_parameter_m * C ** 2)
    desc = (
        f"Approximate deflection angle is {alpha:.3e} radians for a light ray "
        f"passing at impact parameter {inp.impact_parameter_m:.3e} m "
        f"by mass {inp.lens_mass_kg:.3e} kg (weak-field approximation)."
    )
    return LensingResult(deflection_rad=alpha, description=desc)
