import numpy as np
import sympy as sp
from typing import Dict, List

def compute_condition_number(expr_str: str, point: float) -> Dict:
    """
    Computes absolute and relative condition numbers for y = f(x).
    Relative Condition K = |x * f'(x) / f(x)|
    """
    x = sp.Symbol('x')
    f = sp.sympify(expr_str)
    df = sp.diff(f, x)
    
    f_val = float(f.subs(x, point).evalf())
    df_val = float(df.subs(x, point).evalf())
    
    abs_cond = abs(df_val)
    rel_cond = abs(point * df_val / f_val) if f_val != 0 else np.inf
    
    status = "Ill-conditioned" if rel_cond > 100 else "Well-conditioned"
    
    return {
        "Absolute Condition (Sensitivity)": abs_cond,
        "Relative Condition Number (K)": rel_cond,
        "Status": status,
        "Note": "Problem conditioning reflects inherent sensitivity to input perturbations, independent of the algorithm used."
    }
