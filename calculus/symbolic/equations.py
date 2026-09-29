import sympy as sp
from typing import Dict, Any, List

def solve_equation(expr: sp.Expr, var: sp.Symbol) -> Dict[str, Any]:
    """Solves f(x) = 0 exactly. Returns conditions and solution sets."""
    try:
        solutions = sp.solveset(expr, var, domain=sp.S.Reals)
        return {"Solutions": solutions, "Status": "Exact Solution"}
    except Exception as e:
        return {"Solutions": None, "Status": f"Failed: {str(e)}"}

def solve_system(exprs: List[sp.Expr], vars_list: List[sp.Symbol]) -> Dict[str, Any]:
    """Solves a system of linear or nonlinear equations f_i(x_1...x_n) = 0."""
    try:
        solutions = sp.solve(exprs, vars_list, dict=True)
        return {"Solutions": solutions, "Status": "Exact System Solution"}
    except Exception as e:
        return {"Solutions": None, "Status": f"Failed: {str(e)}"}

def solve_inequality(ineq_expr: sp.Expr) -> Dict[str, Any]:
    """Solves inequalities like f(x) > 0 and returns valid intervals."""
    try:
        solution = sp.reduce_inequalities(ineq_expr)
        return {"Interval": solution, "Status": "Success"}
    except Exception as e:
        return {"Interval": None, "Status": f"Failed: {str(e)}"}
