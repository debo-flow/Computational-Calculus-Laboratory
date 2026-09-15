import sympy as sp
from typing import List
from .multivariable_engine import MultivariableEngine
from .gradient import evaluate_gradient

def compute_tangent_plane(engine: MultivariableEngine, point: List[float]) -> dict:
    """
    Computes the tangent plane for z = f(x, y):
    z = f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b)
    """
    if len(engine.vars) != 2:
        return {"Error": "Tangent plane visualization strictly supported for 2D scalar fields z = f(x,y)."}
    
    x, y = engine.vars
    a, b = point
    f_ab = engine.evaluate(point)
    grad_eval = evaluate_gradient(engine, point)
    
    if isinstance(f_ab, str) or "Status" in grad_eval:
        return {"Error": "Function or gradient undefined at point."}
        
    fx_ab, fy_ab = grad_eval["Gradient Vector"]
    
    tangent_expr = f_ab + fx_ab * (x - a) + fy_ab * (y - b)
    differential_df = sp.Symbol('f_x')*sp.Symbol('dx') + sp.Symbol('f_y')*sp.Symbol('dy')
    
    return {
        "Base Point": point,
        "f(a,b)": f_ab,
        "Tangent Plane Equation": sp.simplify(tangent_expr),
        "Differential df": differential_df,
        "Linear Approximation L(x,y)": tangent_expr
    }
