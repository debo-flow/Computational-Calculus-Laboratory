import sympy as sp
from typing import List, Dict, Union

class SequenceEngine:
    """Core engine representing a discrete mathematical sequence a_n = f(n)."""
    def __init__(self, expr_str: str, var_name: str = 'n'):
        self.n = sp.Symbol(var_name, integer=True, positive=True)
        try:
            self.expression = sp.sympify(expr_str.replace('^', '**'))
        except Exception as e:
            raise ValueError(f"Invalid sequence expression: {e}")

    def generate_terms(self, start: int, count: int) -> List[Dict[str, Union[int, sp.Expr, float]]]:
        """Generates exact and numerical terms for the sequence."""
        terms = []
        for i in range(start, start + count):
            exact_val = self.expression.subs(self.n, i)
            approx_val = float(exact_val.evalf()) if exact_val.is_real else None
            terms.append({"n": i, "a_n (Exact)": exact_val, "a_n (Approx)": approx_val})
        return terms

    def get_subsequence(self, transform_str: str):
        """Creates a new SequenceEngine based on an index transformation (e.g., '2*n')."""
        trans = sp.sympify(transform_str.replace('^', '**'))
        new_expr = self.expression.subs(self.n, trans)
        return SequenceEngine(str(new_expr))
