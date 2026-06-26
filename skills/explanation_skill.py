# skills/explanation_skill.py

from tools.explanation_formatter_tool import (
    format_explanation,
    ExplanationInput,
)


class ExplanationSkill:
    """
    Produces clear, structured explanations.
    """

    def explain(self, technical_summary: str, numeric_summary: str = None, user_level: str = "mixed"):
        result = format_explanation(
            ExplanationInput(
                technical_summary=technical_summary,
                numeric_summary=numeric_summary,
                user_level=user_level,
            )
        )
        return {
            "explanation": result.text,
        }
