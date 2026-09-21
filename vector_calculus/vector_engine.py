import sympy as sp
from typing import List, Union

class VectorFunctionEngine:
    """Represents a parametric vector-valued function r(t) = <x(t), y(t), z(t)>."""
    def __init__(self, exprs: List[str], var_str: str = 't'):
        self.t = sp.Symbol(var_str, real=True)
        try:
            self.components = [sp.sympify(e.replace('^', '**')) for e in exprs]
            self.dim = len(self.components)
        except Exception as e:
            raise ValueError(f"Invalid vector function: {e}")

    def evaluate(self, t_val: float) -> Union[List[float], str]:
        try:
            res = [float(comp.subs(self.t, t_val).evalf()) for comp in self.components]
            return res
        except Exception:
            return "Undefined"
