import numpy as np
import sympy as sp
from typing import Dict, Union
from calculus.functions.function_engine import FunctionEngine
from .polynomial import TaylorPolynomial

def calculate_remainder_bounds(poly: TaylorPolynomial, x_eval: float, order: int) -> Dict[str, Union[float, str]]:
    """
    Calculates exact error and the Lagrange error bound.
    M_val is estimated numerically over [a, x_eval] as symbolic maximization is brittle.
    """
    a_float = float(poly.a.evalf())
    x_val = float(x_eval)
    
    # Exact Error
    _, f_exact = poly.engine.evaluate(x_val)
    T_n_expr = poly.generate(order)
    T_n_val = float(T_n_expr.subs(poly.x, x_val).evalf())
    
    if isinstance(f_exact, str):
        return {"Status": "Failed", "Reason": "Original function undefined at evaluation point."}
        
    actual_error = abs(f_exact - T_n_val)
    
    # Lagrange Bound: |R_n(x)| <= M * |x-a|^(n+1) / (n+1)!
    # M = max |f^(n+1)(t)| for t between a and x
    f_np1 = poly.get_derivative(order + 1)
    f_np1_lam = sp.lambdify(poly.x, f_np1, modules=['numpy'])
    
    t_vals = np.linspace(min(a_float, x_val), max(a_float, x_val), 1000)
    try:
        deriv_vals = np.abs(f_np1_lam(t_vals))
        if np.any(np.isnan(deriv_vals)) or np.any(np.isinf(deriv_vals)):
            bound = "N/A (Singularity in derivative on interval)"
        else:
            M = np.max(deriv_vals)
            bound = M * (abs(x_val - a_float)**(order + 1)) / float(sp.factorial(order + 1))
    except Exception:
        bound = "N/A (Numerical bounding failed)"
        
    return {
        "Status": "Success",
        "Exact f(x)": f_exact,
        "Taylor T_n(x)": T_n_val,
        "Actual Error": actual_error,
        "Lagrange Error Bound": bound
    }
