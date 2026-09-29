import sympy as sp
import numpy as np
from typing import Dict

def check_equivalence(expr_a: sp.Expr, expr_b: sp.Expr) -> Dict[str, str]:
    """Mathematically proves equivalence by simplifying A - B to 0."""
    diff = sp.simplify(expr_a - expr_b)
    if diff == 0:
        return {"Equivalence": "Equivalent", "Difference": "0"}
    return {"Equivalence": "Not Equivalent / Conditionally Equivalent", "Simplified Difference": str(diff)}

def numerical_cross_validation(expr_a: sp.Expr, expr_b: sp.Expr, variables: list, samples: int = 10) -> Dict[str, float]:
    """Evaluates expressions at random valid domain points to corroborate symbolic proofs."""
    f_a = sp.lambdify(variables, expr_a, modules=['numpy'])
    f_b = sp.lambdify(variables, expr_b, modules=['numpy'])
    
    max_err, max_rel_err = 0.0, 0.0
    for _ in range(samples):
        # Sample away from 0 to avoid trivial singularities
        pts = np.random.uniform(0.1, 5.0, len(variables))
        try:
            val_a = float(f_a(*pts))
            val_b = float(f_b(*pts))
            abs_err = abs(val_a - val_b)
            rel_err = abs_err / abs(val_a) if val_a != 0 else abs_err
            
            max_err = max(max_err, abs_err)
            max_rel_err = max(max_rel_err, rel_err)
        except Exception:
            continue # Skip domain violations
            
    return {"Maximum Absolute Error": max_err, "Maximum Relative Error": max_rel_err}
