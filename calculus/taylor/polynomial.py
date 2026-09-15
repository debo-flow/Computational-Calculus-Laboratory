import sympy as sp
from typing import Dict, Any, List
from calculus.functions.function_engine import FunctionEngine

class TaylorPolynomial:
    """Generates and caches Taylor Polynomials and their coefficients."""
    def __init__(self, engine: FunctionEngine, a: float):
        self.engine = engine
        self.x = engine.x
        self.a = sp.sympify(a)
        
        # Cache to prevent repeated symbolic differentiation
        self.derivatives = {0: engine.expression}
        self.coefficients = {}

    def get_derivative(self, k: int) -> sp.Expr:
        for i in range(1, k + 1):
            if i not in self.derivatives:
                self.derivatives[i] = sp.diff(self.derivatives[i-1], self.x)
        return self.derivatives[k]

    def get_coefficient(self, n: int) -> sp.Expr:
        if n not in self.coefficients:
            deriv_a = self.get_derivative(n).subs(self.x, self.a)
            if deriv_a.has(sp.zoo, sp.nan, sp.oo, -sp.oo):
                raise ValueError(f"Derivative undefined at expansion point for order {n}")
            self.coefficients[n] = deriv_a / sp.factorial(n)
        return self.coefficients[n]

    def generate(self, order: int) -> sp.Expr:
        """Generates T_n(x)."""
        poly = sp.S.Zero
        for n in range(order + 1):
            poly += self.get_coefficient(n) * (self.x - self.a)**n
        return poly

    def get_coefficient_table(self, order: int) -> List[Dict[str, Any]]:
        table = []
        for n in range(order + 1):
            f_n_a = self.get_derivative(n).subs(self.x, self.a)
            table.append({
                "n": n,
                "f^(n)(a)": f_n_a,
                "n!": sp.factorial(n),
                "c_n": self.get_coefficient(n)
            })
        return table
