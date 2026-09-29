import sympy as sp
import mpmath
from typing import Dict

def compare_precision(expr_str: str, eval_point: float, dps: int = 50) -> Dict:
    """Compares standard 64-bit float precision against arbitrary multi-precision (mpmath)."""
    x = sp.Symbol('x')
    expr = sp.sympify(expr_str)
    
    # Standard IEEE 754 64-bit floating point
    f_float = sp.lambdify(x, expr, modules=['numpy'])
    val_float = float(f_float(eval_point))
    
    # Arbitrary precision
    mpmath.mp.dps = dps
    f_mp = sp.lambdify(x, expr, modules=['mpmath'])
    val_mp = f_mp(eval_point)
    
    diff = abs(val_mp - val_float)
    rel_diff = diff / abs(val_mp) if val_mp != 0 else diff
    
    return {
        "Standard Float (64-bit)": val_float,
        f"High Precision ({dps} dps)": str(val_mp),
        "Absolute Difference": float(diff),
        "Relative Difference": float(rel_diff),
        "Interpretation": "High precision acts as a numerical reference but does not constitute a formal mathematical proof."
    }
