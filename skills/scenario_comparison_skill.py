from skills.relativistic_computation_skill import RelativisticComputationSkill


class ScenarioComparisonSkill:
    """
    Compares multiple GR scenarios (time dilation, orbits, lensing strength).
    """

    def compare_time_dilation(self, scenarios):
        """
        scenarios = [
            {"mass_kg": ..., "radius_m": ...},
            {"mass_kg": ..., "radius_m": ...}
        ]
        """
        comp = RelativisticComputationSkill()
        results = []

        for s in scenarios:
            td = comp.compute_time_dilation(
                mass_kg=s["mass_kg"],
                radius_m=s["radius_m"],
            )
            results.append(
                {
                    "input": s,
                    "time_dilation": td,
                }
            )

        return {
            "comparison_type": "time_dilation",
            "results": results,
        }
