from skills.astrophysics_knowledge_skill import AstrophysicsKnowledgeSkill
from skills.relativistic_computation_skill import RelativisticComputationSkill
from skills.explanation_skill import ExplanationSkill
from skills.orbit_analysis_skill import OrbitAnalysisSkill
from skills.visualization_skill import VisualizationSkill
from skills.lensing_analysis_skill import LensingAnalysisSkill
from skills.scenario_comparison_skill import ScenarioComparisonSkill


def example_time_dilation_sgr_a_star():
    """
    Example:
    Compare time dilation at 3 Rs and 10 Rs for Sagittarius A*.
    """
    astro = AstrophysicsKnowledgeSkill()
    comp = RelativisticComputationSkill()
    explain = ExplanationSkill()
    compare = ScenarioComparisonSkill()

    # 1) Get mass of Sagittarius A*
    m_res = astro.lookup("sgr_a_star_mass_kg")
    if "error" in m_res:
        print("Error:", m_res["error"])
        return

    M = m_res["value"]
    print(f"Sagittarius A* mass: {M:.3e} kg")

    # Schwarzschild radius
    # We reuse the relativistic_math_tool indirectly via a small helper:
    # here we just define Rs explicitly for clarity.
    from tools.relativistic_math_tool import G, C

    Rs = 2 * G * M / (C ** 2)
    r1 = 3 * Rs
    r2 = 10 * Rs

    # 2) Compare time dilation at r1 and r2
    scenarios = [
        {"mass_kg": M, "radius_m": r1},
        {"mass_kg": M, "radius_m": r2},
    ]
    comparison = compare.compare_time_dilation(scenarios)

    # 3) Build explanation
    tech_summary = (
        "We computed gravitational time dilation near Sagittarius A* at two radii: "
        "3 times the Schwarzschild radius (3Rs) and 10 times the Schwarzschild radius (10Rs). "
        "The time dilation factor is t_far / t_near, where t_far is time far from the black hole "
        "and t_near is time experienced by an observer at that radius."
    )

    numeric_lines = []
    for idx, res in enumerate(comparison["results"], start=1):
        r = res["input"]["radius_m"]
        f = res["time_dilation"]["factor"]
        numeric_lines.append(f"Scenario {idx}: radius = {r:.3e} m, time dilation factor ~= {f:.6f}")

    numeric_summary = "\n".join(numeric_lines)
    exp = explain.explain(
        technical_summary=tech_summary,
        numeric_summary=numeric_summary,
        user_level="mixed",
    )

    print("\n=== Gravitas AI: Time Dilation Comparison ===")
    print(exp["explanation"])


def example_orbit_and_plot():
    """
    Example:
    Simulate a circular orbit around a solar-mass object and produce a plot spec.
    """
    orbit_skill = OrbitAnalysisSkill()
    viz_skill = VisualizationSkill()

    solar_mass = 1.98847e30
    radius = 1.5e11  # ~1 AU

    orbit_res = orbit_skill.simulate_orbit(
        mass_kg=solar_mass,
        radius_m=radius,
        steps=180,
    )

    plot_res = viz_skill.orbit_plot(orbit_res["trajectory"])

    print("\n=== Gravitas AI: Orbit Simulation ===")
    print(orbit_res["description"])
    print("\nPlot spec (truncated):")
    spec = plot_res["plot_spec"]
    print({k: spec[k] for k in ["type", "title", "x_label", "y_label"]})
    print(f"Number of points: {len(spec['series'][0]['x'])}")


def example_lensing():
    """
    Example:
    Compute light deflection by a massive lens.
    """
    lens_skill = LensingAnalysisSkill()
    astro = AstrophysicsKnowledgeSkill()

    m_res = astro.lookup("solar_mass_kg")
    if "error" in m_res:
        print("Error:", m_res["error"])
        return

    M = m_res["value"]
    impact = 1e9  # 1 billion meters

    lens_res = lens_skill.compute_lensing(
        mass_kg=M,
        impact_parameter_m=impact,
    )

    print("\n=== Gravitas AI: Gravitational Lensing ===")
    print(lens_res["description"])

    if not lens_res["validation"]["is_valid"]:
        print("Validation issues:", lens_res["validation"]["issues"])


def main():
    print("Running Gravitas AI demo examples...\n")
    example_time_dilation_sgr_a_star()
    example_orbit_and_plot()
    example_lensing()
    print("\nDone.")


if __name__ == "__main__":
    main()
