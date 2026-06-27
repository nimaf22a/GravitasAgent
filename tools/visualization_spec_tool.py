from typing import Dict, Any, List, Tuple


def make_orbit_plot_spec(trajectory: List[Tuple[float, float]]) -> Dict[str, Any]:
    """
    Returns a JSON-like spec for plotting an orbit in 2D.
    """
    xs = [p[0] for p in trajectory]
    ys = [p[1] for p in trajectory]
    return {
        "type": "line_plot",
        "title": "Orbital Trajectory",
        "x_label": "x (m)",
        "y_label": "y (m)",
        "series": [
            {
                "name": "orbit",
                "x": xs,
                "y": ys,
            }
        ],
    }
