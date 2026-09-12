import sympy as sp
from calculus.sequences.sequence_engine import SequenceEngine
from .divergence_tests import nth_term_test
from .convergence_tests import ratio_test, root_test, alternating_series_test, integral_test

class SeriesEngine:
    """Coordinator for infinite series Σ a_n analysis and tests."""
    def __init__(self, seq_engine: SequenceEngine):
        self.seq_engine = seq_engine
        self.a_n = seq_engine.expression
        self.n = seq_engine.n

    def evaluate_exact_sum(self):
        """Attempts to find the exact infinite sum analytically."""
        try:
            res = sp.Sum(self.a_n, (self.n, 1, sp.oo)).doit()
            return res if not res.has(sp.Sum) else "No elementary exact sum found."
        except:
            return "Unable to compute exact sum."

    def run_all_tests(self) -> dict:
        """Runs the suite of convergence tests and returns the strongest conclusion."""
        report = {}
        
        # 1. N-th Term Test for Divergence (Necessary condition)
        term_res = nth_term_test(self.seq_engine)
        report["N-th Term Test"] = term_res
        if term_res["Classification"] == "Divergent":
            report["Final Conclusion"] = "Divergent (by N-th Term Test)"
            return report

        # 2. Ratio Test
        ratio_res = ratio_test(self.seq_engine)
        report["Ratio Test"] = ratio_res
        if ratio_res["Classification"] != "Inconclusive":
            report["Final Conclusion"] = f"{ratio_res['Classification']} (by Ratio Test)"
            return report

        # 3. Root Test
        root_res = root_test(self.seq_engine)
        report["Root Test"] = root_res
        if root_res["Classification"] != "Inconclusive":
            report["Final Conclusion"] = f"{root_res['Classification']} (by Root Test)"
            return report

        # 4. Alternating Series Test (if applicable)
        if self.a_n.has(-1) and (sp.sympify("-1**n") in self.a_n.args or sp.sympify("(-1)**n") in self.a_n.as_ordered_factors()):
            alt_res = alternating_series_test(self.seq_engine)
            report["Alternating Series Test"] = alt_res
            if alt_res["Classification"] != "Inconclusive":
                report["Final Conclusion"] = f"{alt_res['Classification']} (by Alternating Series Test)"
                return report

        report["Final Conclusion"] = "Inconclusive. Advanced tests (Limit Comparison/Integral) required."
        return report
