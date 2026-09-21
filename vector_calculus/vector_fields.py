import sympy as sp
from typing import List, Union

class VectorFieldEngine:
    """Represents a vector field F(x,y,z) = <P, Q, R>."""
    def __init__(self, exprs: List[str], vars_str: str = "x, y, z"):
        self.vars = sp.symbols(vars_str)
        try:
            self.components = [sp.sympify(e.replace('^', '**')) for e in exprs]
            self.dim = len(self.components)
        except Exception as e:
            raise ValueError(f"Invalid vector field: {e}")

    def evaluate(self, point: List[float]) -> Union[List[float], str]:
        if len(point) != len(self.vars): return "Dimension mismatch"
        sub_map = dict(zip(self.vars, point))
        try:
            return [float(comp.subs(sub_map).evalf()) for comp in self.components]
        except Exception:
            return "Undefined"

