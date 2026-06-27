from dataclasses import dataclass
from typing import Optional


@dataclass
class ExplanationInput:
    technical_summary: str
    numeric_summary: Optional[str] = None
    user_level: str = "mixed"  # "beginner", "advanced", "mixed"


@dataclass
class ExplanationOutput:
    text: str


def format_explanation(inp: ExplanationInput) -> ExplanationOutput:
    """
    Very simple formatter that could later be enhanced by the LLM.
    """
    parts = []
    if inp.user_level in ("beginner", "mixed"):
        parts.append("Intuitive explanation:\n" + inp.technical_summary)
    if inp.numeric_summary:
        parts.append("\nNumeric summary:\n" + inp.numeric_summary)
    if inp.user_level in ("advanced", "mixed"):
        parts.append("\nTechnical notes:\n" + inp.technical_summary)
    return ExplanationOutput(text="\n".join(parts))
