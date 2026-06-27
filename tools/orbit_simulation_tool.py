from dataclasses import dataclass
from typing import List, Tuple
import math

G = 6.67430e-11


@dataclass
class OrbitParams:
    central_mass_kg: float
    radius_m: float
    steps: int = 360


@dataclass
class OrbitTrajectory:
    positions: List[Tuple[float, float]]
    description: str


def simulate_circular_orbit(params: OrbitParams) -> OrbitTrajectory:
    """
    Simple Newtonian circular orbit in 2D.
    Returns positions (x, y) on the orbital path.
    """
    r = params.radius_m
    positions = []
    for i in range(params.steps):
        theta = 2 * math.pi * i / params.steps
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        positions.append((x, y))

    desc = (
        f"Simulated a circular orbit at radius {r:.3e} m around mass "
        f"{params.central_mass_kg:.3e} kg with {params.steps} sample points."
    )
    return OrbitTrajectory(positions=positions, description=desc)
