import sympy as sp
from typing import Dict, Any, List
from calculus.functions.function_engine import FunctionEngine
from .indefinite_integrals import compute_indefinite_integral
from .definite_integrals import compute_definite_integral
from .integration_rules import identify_integration_rule
from .improper_integrals import evaluate_improper_integral
from .integral_analysis import (
    compute_riemann_sum,
    riemann_convergence_series,
    verify_fundamental_theorem_part1,
    verify_fundamental_theorem_part2,
    area_between_curves
)

class IntegralEngine:
    """
    Unified coordinator for symbolic integration, definite integrals,
    Riemann sum approximations, theorems, and technique verifications.
    """
    def __init__(self, engine: FunctionEngine):
        self.engine = engine
        self.x = engine.x
        self.expr = engine.expression

    def integrate_indefinite(self) -> Dict[str, Any]:
        return compute_indefinite_integral(self.engine)

    def integrate_definite(self, a: Any, b: Any) -> Dict[str, Any]:
        return compute_definite_integral(self.engine, a, b)

    def get_rule_breakdown(self) -> Dict[str, str]:
        return identify_integration_rule(self.expr, self.x)

    def riemann_sum(self, a: float, b: float, n: int, method: str = 'midpoint') -> Dict[str, Any]:
        return compute_riemann_sum(self.engine, a, b, n, method)

    def riemann_convergence(self, a: float, b: float, n_list: List[int] = [4, 8, 16, 32, 64, 128]) -> List[Dict[str, Any]]:
        return riemann_convergence_series(self.engine, a, b, n_list)

    def verify_ftc(self, a: float, b: float) -> Dict[str, Any]:
        part1 = verify_fundamental_theorem_part1(self.engine, a)
        part2 = verify_fundamental_theorem_part2(self.engine, a, b)
        return {"Part1": part1, "Part2": part2}

    def area_between(self, other_engine: FunctionEngine, a: float, b: float) -> Dict[str, Any]:
        return area_between_curves(self.engine, other_engine, a, b)
