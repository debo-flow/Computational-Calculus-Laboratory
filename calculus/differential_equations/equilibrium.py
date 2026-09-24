import sympy as sp
from typing import List

def find_equilibria(sys_exprs: List[str], vars_str: str) -> List[list]:
    """Solves F(X) = 0 for equilibria."""
    variables = sp.symbols(vars_str)
    equations = [sp.sympify(e) for e in sys_exprs]
    try:
        sols = sp.solve(equations, variables, dict=True)
        return [[float(sol[v].evalf()) for v in variables] for sol in sols if all(val.is_real for val in sol.values())]
    except Exception:
        return []
