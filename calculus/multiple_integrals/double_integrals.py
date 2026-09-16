import sympy as sp
from typing import Dict, Any, Tuple
from calculus.multivariable.multivariable_engine import MultivariableEngine
from .region_analysis import analyze_2d_region

def compute_double_integral(engine: MultivariableEngine, x_bounds: Tuple[Any, Any], y_bounds: Tuple[Any, Any], order: str = "xy") -> Dict[str, Any]:
    """
    Computes iterated double integrals. 
    order="xy" means dx dy (inner integral dx, outer dy).
    order="yx" means dy dx (inner integral dy, outer dx).
    """
    x, y = engine.vars[0], engine.vars[1]
    expr = engine.expression
    
    region = analyze_2d_region(x_bounds, y_bounds, x, y)
    xb = region["x_bounds"]
    yb = region["y_bounds"]
    
    try:
        if order == "xy":
            # Inner: x, Outer: y (dx dy)
            inner_int = sp.integrate(expr, (x, xb[0], xb[1]))
            outer_int = sp.integrate(inner_int, (y, yb[0], yb[1]))
        elif order == "yx":
            # Inner: y, Outer: x (dy dx)
            inner_int = sp.integrate(expr, (y, yb[0], yb[1]))
            outer_int = sp.integrate(inner_int, (x, xb[0], xb[1]))
        else:
            raise ValueError("Integration order must be 'xy' or 'yx'.")
            
        numerical_val = float(outer_int.evalf()) if outer_int.is_real else "N/A"
        
        return {
            "Status": "Success",
            "Order": f"d{order[0]} d{order[1]}",
            "Region Type": region["Type"],
            "Inner Integral": inner_int,
            "Exact Result": outer_int,
            "Numerical Result": numerical_val
        }
    except Exception as e:
        return {"Status": "Failed", "Error": str(e)}

def change_integration_order(engine: MultivariableEngine, x_bnds: Tuple[Any, Any], y_bnds: Tuple[Any, Any]) -> Dict[str, Any]:
    """Demonstrates Fubini's Theorem on constant bounds."""
    res_xy = compute_double_integral(engine, x_bnds, y_bnds, order="xy")
    res_yx = compute_double_integral(engine, x_bnds, y_bnds, order="yx")
    
    match = False
    if res_xy["Status"] == "Success" and res_yx["Status"] == "Success":
        match = sp.simplify(res_xy["Exact Result"] - res_yx["Exact Result"]) == 0
        
    return {
        "dx dy Result": res_xy.get("Exact Result"),
        "dy dx Result": res_yx.get("Exact Result"),
        "Fubini Theorem Holds": match
    }
