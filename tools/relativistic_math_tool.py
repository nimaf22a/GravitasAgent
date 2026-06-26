from dataclasses import dataclass
import math

C = 3e8  # speed of light (m/s)
G = 6.67430e-11  # gravitational constant (SI)


@dataclass
class TimeDilationInput:
    mass_kg: float
    radius_m: float


@dataclass
class TimeDilationResult:
    factor: float
    description: str


def compute_gravitational_time_dilation(inp: TimeDilationInput) -> TimeDilationResult:
    """
    Computes gravitational time dilation near a non-rotating mass (Schwarzschild metric, weak field).
    t_far / t_near = 1 / sqrt(1 - 2GM/(rc^2))
    """
    rs = 2 * G * inp.mass_kg / (C ** 2)
    if inp.radius_m <= rs:
        return TimeDilationResult(
            factor=float("nan"),
            description="Radius is at or within the Schwarzschild radius; static observer not possible.",
        )

    factor = 1.0 / math.sqrt(1.0 - (2 * G * inp.mass_kg) / (inp.radius_m * C ** 2))
    desc = (
        f"Gravitational time dilation factor at radius {inp.radius_m:.3e} m "
        f"from mass {inp.mass_kg:.3e} kg is ~{factor:.6f}. "
        "This is t_far / t_near (time far away divided by time near the mass)."
    )
    return TimeDilationResult(factor=factor, description=desc)
