import sympy as sp
from typing import List, Dict
from .multivariable_engine import MultivariableEngine
from .gradient import compute_gradient

def find_multivariable_critical_points(engine: MultivariableEngine) -> List[Dict]:
    """Finds points where gradient is zero and classifies them using the Hessian."""
    grad = compute_gradient(engine)["Gradient"]
    solutions = sp.solve(grad, engine.vars, dict=True)
    
    results = []
    for sol in solutions:
        if all(val.is_real for val in sol.values()):
            pt = [float(sol[v].evalf()) for v in engine.vars]
            class_data = second_derivative_test(engine, pt)
            results.append({"Point": pt, "Classification": class_data})
            
    return results

def second_derivative_test(engine: MultivariableEngine, point: List[float]) -> dict:
    """Applies the Hessian 2nd Derivative Test for f(x,y)."""
    if len(engine.vars) != 2:
        return {"Status": "Classification supported only for 2 variables currently."}
        
    x, y = engine.vars
    f_xx = sp.diff(engine.expression, x, 2)
    f_yy = sp.diff(engine.expression, y, 2)
    f_xy = sp.diff(sp.diff(engine.expression, x), y)
    
    sub_map = dict(zip(engine.vars, point))
    
    try:
        D_val = float((f_xx * f_yy - f_xy**2).subs(sub_map).evalf())
        fxx_val = float(f_xx.subs(sub_map).evalf())
        
        if D_val > 0 and fxx_val > 0: classification = "Local Minimum"
        elif D_val > 0 and fxx_val < 0: classification = "Local Maximum"
        elif D_val < 0: classification = "Saddle Point"
        else: classification = "Inconclusive (D=0)"
        
        return {"D": D_val, "f_xx": fxx_val, "Result": classification}
    except Exception:
        return {"Result": "Failed to evaluate Hessian at point."}
