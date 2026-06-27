from dataclasses import dataclass
from typing import List

C = 3e8
G = 6.67430e-11


@dataclass
class ValidationInput:
    mass_kg: float
    radius_m: float
    velocity_m_s: float


@dataclass
class ValidationResult:
    is_valid: bool
    issues: List[str]
    suggestions: List[str]


def validate_physical_params(inp: ValidationInput) -> ValidationResult:
    issues = []
    suggestions = []

    rs = 2 * G * inp.mass_kg / (C ** 2)
    if inp.radius_m <= rs:
        issues.append("Radius is at or within the Schwarzschild radius.")
        suggestions.append(f"Use radius > {1.1 * rs:.3e} m for an external observer.")

    if inp.velocity_m_s >= C:
        issues.append("Velocity is at or above the speed of light.")
        suggestions.append("Use velocity < 0.9c for realistic scenarios.")

    is_valid = len(issues) == 0
    return ValidationResult(is_valid=is_valid, issues=issues, suggestions=suggestions)
