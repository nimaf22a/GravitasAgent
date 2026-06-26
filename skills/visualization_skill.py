# skills/visualization_skill.py

from tools.visualization_spec_tool import make_orbit_plot_spec


class VisualizationSkill:
    """
    Generates visualization specifications for plots and diagrams.
    """

    def orbit_plot(self, trajectory):
        spec = make_orbit_plot_spec(trajectory)
        return {
            "plot_spec": spec,
            "description": "Generated a 2D orbit plot specification.",
        }
