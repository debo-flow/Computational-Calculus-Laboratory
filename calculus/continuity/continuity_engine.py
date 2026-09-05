import sympy as sp
from typing import Dict, Union, List
from calculus.functions.function_engine import FunctionEngine
from calculus.limits.limit_engine import LimitEngine

class ContinuityEngine:
    """
    Engine for analyzing the continuity of a function at a specific point or interval.
    """
    def __init__(self, engine: FunctionEngine):
        self.engine = engine
        self.lim_engine = LimitEngine(engine)
        self.x = engine.x
        self.expr = engine.expression

    def evaluate_point_continuity(self, point_str: str) -> Dict[str, Union[sp.Expr, str, bool]]:
        """
        Evaluates the three conditions of continuity at a point x = a.
        """
        try:
            a = sp.sympify(point_str)
            
            # Condition 1: f(a) exists
            f_a = self.expr.subs(self.x, a)
            if f_a.has(sp.zoo, sp.nan, sp.oo, -sp.oo) or not f_a.is_real:
                f_a_val = "Undefined"
            else:
                f_a_val = sp.simplify(f_a)

            # Condition 2: Limits exist
            lim_results = self.lim_engine.evaluate_limits(a)
            lhl = lim_results['Left-Hand Limit']
            rhl = lim_results['Right-Hand Limit']
            tsl = lim_results['Two-Sided Limit']

            # Condition 3: Limit equals f(a)
            left_cont = (lhl == f_a_val) if f_a_val != "Undefined" else False
            right_cont = (rhl == f_a_val) if f_a_val != "Undefined" else False
            
            is_cont = False
            if f_a_val != "Undefined" and tsl != "Does Not Exist":
                is_cont = (tsl == f_a_val)

            return {
                "Point": a,
                "f(a)": f_a_val,
                "LHL": lhl,
                "RHL": rhl,
                "Limit": tsl,
                "Left Continuous": left_cont,
                "Right Continuous": right_cont,
                "Continuous": is_cont
            }
        except Exception as e:
            raise ValueError(f"Continuity evaluation failed: {str(e)}")

    def find_discontinuities_in_interval(self, start: float, end: float) -> List[sp.Expr]:
        """
        Attempts to symbolically find points of discontinuity in [start, end].
        """
        try:
            from sympy.calculus.singularities import singularities
            sings = singularities(self.expr, self.x)
            
            if isinstance(sings, sp.sets.Set):
                domain = sp.Interval(start, end)
                sings_in_domain = sings.intersect(domain)
                
                if isinstance(sings_in_domain, sp.sets.FiniteSet):
                    return list(sings_in_domain)
                elif sings_in_domain == sp.S.EmptySet:
                    return []
            return ["Analytical interval search too complex. Use point analysis."]
        except Exception:
            return ["Could not definitively calculate analytical discontinuities for this expression."]
