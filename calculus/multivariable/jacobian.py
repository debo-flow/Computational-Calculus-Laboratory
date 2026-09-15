import sympy as sp
from typing import List, Dict, Union

def compute_jacobian(expr_strs: List[str], vars_str: str) -> Dict[str, Union[sp.Matrix, sp.Expr, str]]:
    """Calculates the Jacobian matrix and its determinant for F(x1, ... xn)."""
    variables = sp.symbols(vars_str)
    funcs = [sp.sympify(e) for e in expr_strs]
    
    jacobian_matrix = sp.Matrix([[sp.diff(f, v) for v in variables] for f in funcs])
    
    res = {"Jacobian Matrix": jacobian_matrix}
    if jacobian_matrix.is_square:
        res["Determinant"] = sp.simplify(jacobian_matrix.det())
    else:
        res["Determinant"] = "N/A (Non-square matrix)"
        
    return res
