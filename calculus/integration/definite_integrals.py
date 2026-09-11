import sympy as sp
from typing import Dict, Any, Union
from calculus.functions.function_engine import FunctionEngine

def compute_definite_integral(engine: FunctionEngine, a_val: Any, b_val: Any) -> Dict[str, Any]:
    """
    Calculates ∫_a^b f(x) dx symbolically and numerically.
    Handles reversed bounds: ∫_b^a f(x) dx = -∫_a^b f(x) dx.
    Distinguishes signed area from total geometric area ∫_a^b |f(x)| dx.
    """
    x = engine.x
    expr = engine.expression

    try:
        a = sp.sympify(a_val)
        b = sp.sympify(b_val)
        
        reversed_bounds = False
        if a.is_real and b.is_real and a > b:
            reversed_bounds = True

        exact_val = sp.integrate(expr, (x, a, b))
        
        if exact_val.has(sp.oo, -sp.oo, sp.zoo, sp.nan):
            return {
                "Status": "Divergent or Undefined",
                "Exact": exact_val,
                "Numerical": str(exact_val),
                "SignedArea": None,
                "GeometricArea": None,
                "ReversedBounds": reversed_bounds
            }

        num_val = float(exact_val.evalf())

        # Determine sign
        if num_val > 1e-12:
            sign_str = "Positive (Net accumulation above x-axis)"
        elif num_val < -1e-12:
            sign_str = "Negative (Net accumulation below x-axis)"
        else:
            sign_str = "Zero (Balanced net cancellation or null interval)"

        # Geometric area: ∫ |f(x)| dx
        try:
            geom_exact = sp.integrate(sp.Abs(expr), (x, min(float(a.evalf()), float(b.evalf())), max(float(a.evalf()), float(b.evalf()))))
            geom_num = float(geom_exact.evalf())
        except Exception:
            geom_num = "Numerical estimation required"

        interpretation = (
            f"Over the interval [{a}, {b}], the signed accumulation is {num_val:.6g}. "
        )
        if reversed_bounds:
            interpretation += "Bounds were specified in reversed order (a > b), negating the integral."

        return {
            "Status": "Success",
            "LowerBound": a,
            "UpperBound": b,
            "ReversedBounds": reversed_bounds,
            "Exact": exact_val,
            "Numerical": num_val,
            "Sign": sign_str,
            "SignedArea": num_val,
            "GeometricArea": geom_num,
            "Interpretation": interpretation
        }
    except Exception as e:
        return {
            "Status": "Error",
            "Error": str(e),
            "Exact": None,
            "Numerical": None
        }
