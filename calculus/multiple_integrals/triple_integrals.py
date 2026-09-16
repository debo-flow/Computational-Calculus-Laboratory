import sympy as sp
from typing import Dict, Any, Tuple
from calculus.multivariable.multivariable_engine import MultivariableEngine

def compute_triple_integral(engine: MultivariableEngine, x_bnds: Tuple[Any, Any], y_bnds: Tuple[Any, Any], z_bnds: Tuple[Any, Any]) -> Dict[str, Any]:
    """Computes ∫∫∫_V f(x,y,z) dV."""
    if len(engine.vars) < 3:
        return {"Status": "Failed", "Error": "Triple integral requires at least 3 variables."}
        
    x, y, z = engine.vars[0], engine.vars[1], engine.vars[2]
    expr = engine.expression
    
    try:
        xb = (sp.sympify(x_bnds[0]), sp.sympify(x_bnds[1]))
        yb = (sp.sympify(y_bnds[0]), sp.sympify(y_bnds[1]))
        zb = (sp.sympify(z_bnds[0]), sp.sympify(z_bnds[1]))
        
        int_z = sp.integrate(expr, (z, zb[0], zb[1]))
        int_y = sp.integrate(int_z, (y, yb[0], yb[1]))
        int_x = sp.integrate(int_y, (x, xb[0], xb[1]))
        
        num_val = float(int_x.evalf()) if int_x.is_real else "N/A"
        
        return {
            "Status": "Success",
            "Inner Integral (dz)": int_z,
            "Middle Integral (dy)": int_y,
            "Exact Result": int_x,
            "Numerical Result": num_val
        }
    except Exception as e:
        return {"Status": "Failed", "Error": str(e)}
