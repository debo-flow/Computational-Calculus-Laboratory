import sympy as sp
from calculus.functions.function_engine import FunctionEngine
from calculus.continuity.continuity_engine import ContinuityEngine

def analyze_differentiability(engine: FunctionEngine, point: float) -> dict:
    cont_engine = ContinuityEngine(engine)
    cont_results = cont_engine.evaluate_point_continuity(str(point))
    
    x = engine.x
    f = engine.expression
    a = sp.sympify(point)
    
    # Difference quotient: (f(x) - f(a)) / (x - a)
    diff_quotient = (f - f.subs(x, a)) / (x - a)
    
    lhl_deriv = sp.limit(diff_quotient, x, a, dir='-')
    rhl_deriv = sp.limit(diff_quotient, x, a, dir='+')
    
    is_diff = (lhl_deriv == rhl_deriv) and lhl_deriv.is_real
    
    return {
        "Continuous": cont_results["Continuous"],
        "Left Derivative": lhl_deriv,
        "Right Derivative": rhl_deriv,
        "Differentiable": is_diff,
        "Classification": "Smooth" if is_diff else ("Corner/Cusp" if cont_results["Continuous"] else "Discontinuous")
    }
