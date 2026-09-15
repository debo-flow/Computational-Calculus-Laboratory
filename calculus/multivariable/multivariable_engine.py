import sympy as sp
from typing import Dict, Union, List

class MultivariableEngine:
    """Core engine for functions of several variables."""
    def __init__(self, expr_str: str, vars_str: str = "x, y"):
        self.vars = tuple(sp.symbols(vars_str))
        try:
            self.expression = sp.sympify(expr_str.replace('^', '**'))
        except Exception as e:
            raise ValueError(f"Invalid multivariable expression: {e}")

    def evaluate(self, point: List[float]) -> Union[float, str]:
        if len(point) != len(self.vars):
            raise ValueError("Point dimension must match variable dimension.")
        sub_map = dict(zip(self.vars, point))
        val = self.expression.subs(sub_map)
        if val.has(sp.zoo, sp.nan, sp.oo, -sp.oo) or not val.is_real:
            return "Undefined"
        return float(val.evalf())
