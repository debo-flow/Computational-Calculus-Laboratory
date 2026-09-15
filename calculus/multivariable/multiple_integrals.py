import sympy as sp
from typing import Dict, Union
from .multivariable_engine import MultivariableEngine

def double_integral_rectangular(engine: MultivariableEngine, x_bounds: tuple, y_bounds: tuple) -> Dict:
    """Computes ∫_c^d ∫_a^b f(x,y) dx dy."""
    if len(engine.vars) != 2:
        return {"Status": "Only 2D scalar fields supported."}
        
    x, y = engine.vars
    a, b = sp.sympify(x_bounds[0]), sp.sympify(x_bounds[1])
    c, d = sp.sympify(y_bounds[0]), sp.sympify(y_bounds[1])
    
    try:
        inner_int = sp.integrate(engine.expression, (x, a, b))
        outer_int = sp.integrate(inner_int, (y, c, d))
        
        return {
            "Status": "Success",
            "Inner Integral (dx)": inner_int,
            "Final Exact Integral": outer_int,
            "Numerical Value": float(outer_int.evalf()) if outer_int.is_real else "Complex/Undefined",
            "Interpretation": "Signed volume under the surface over the rectangular domain."
        }
    except Exception as e:
        return {"Status": "Error", "Details": str(e)}
