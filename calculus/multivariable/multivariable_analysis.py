import sympy as sp
from .multivariable_engine import MultivariableEngine

def path_limit_exploration(engine: MultivariableEngine, limit_point: list) -> dict:
    """Explores lim (x,y)->(a,b) along standard paths y=mx, y=kx^2."""
    if len(engine.vars) != 2:
        return {"Status": "Path limits only implemented for 2D."}
    
    x, y = engine.vars
    a, b = limit_point
    
    m, k = sp.symbols('m k')
    # Path 1: y - b = m(x - a)
    path_linear = b + m*(x - a)
    expr_linear = engine.expression.subs(y, path_linear)
    lim_linear = sp.limit(expr_linear, x, a)
    
    # Path 2: y - b = k(x - a)^2
    path_quad = b + k*(x - a)**2
    expr_quad = engine.expression.subs(y, path_quad)
    lim_quad = sp.limit(expr_quad, x, a)
    
    exists = "LIMIT DOES NOT EXIST" if lim_linear.has(m) or lim_quad.has(k) or lim_linear != lim_quad else "Paths agree (NOT a proof of limit existence)"
    
    return {
        "Limit along y=m(x-a)": lim_linear,
        "Limit along y=k(x-a)^2": lim_quad,
        "Conclusion": exists
    }
