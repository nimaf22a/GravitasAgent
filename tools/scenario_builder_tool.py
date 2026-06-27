from dataclasses import dataclass, asdict
from typing import Optional, Literal, Dict, Any

MetricType = Literal["schwarzschild", "kerr", "newtonian"]


@dataclass
class Scenario:
    name: str
    metric: MetricType
    central_mass_kg: float
    radius_m: Optional[float] = None
    velocity_m_s: Optional[float] = None
    spin_parameter: Optional[float] = None  # for Kerr, dimensionless a*
    notes: Optional[str] = None


def build_scenario_from_nl(description: str) -> Dict[str, Any]:
    """
    Very simple heuristic parser for now.
    In a real implementation, you'd use the LLM + schema to fill this.
    """
    scenario = Scenario(
        name="auto_scenario_from_text",
        metric="schwarzschild",
        central_mass_kg=1.98847e30,  # 1 solar mass
        radius_m=1e7,
        velocity_m_s=None,
        notes=f"Auto-generated from description: {description}",
    )
    return asdict(scenario)
