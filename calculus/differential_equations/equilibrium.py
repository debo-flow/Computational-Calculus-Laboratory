import sympy as sp
from typing import List

def find_equilibria(sys_exprs: List[str], vars_str: str) -> List[list]:
    """Solves f(X) = 0 for an autonomous dynamical system."""
    variables = sp.symbols(vars_str)
    equations = [sp.sympify(e) for e in sys_exprs]
    
    try:
        sols = sp.solve(equations, variables, dict=True)
        valid_equilibria = []
        for sol in sols:
            if all(val.is_real for val in sol.values()):
                valid_equilibria.append([float(sol[v].evalf()) for v in variables])
        return valid_equilibria
    except Exception:
        return []
