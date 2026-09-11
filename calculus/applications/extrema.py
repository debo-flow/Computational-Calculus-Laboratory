import sympy as sp
from calculus.functions.function_engine import FunctionEngine
from calculus.differentiation.derivative_engine import DerivativeEngine
from calculus.applications.critical_points import find_critical_points

def classify_local_extrema(engine: FunctionEngine) -> dict:
    """Uses the Second Derivative Test to classify critical points."""
    crit_pts = find_critical_points(engine)
    dev_eng = DerivativeEngine(engine)
    
    classifications = {}
    for c in crit_pts:
        f_double_prime_c = dev_eng.evaluate_derivative(c, 2)
        
        if isinstance(f_double_prime_c, str):
            classifications[c] = "Inconclusive (f''(c) undefined)"
        elif f_double_prime_c > 0:
            classifications[c] = "Local Minimum"
        elif f_double_prime_c < 0:
            classifications[c] = "Local Maximum"
        else:
            classifications[c] = "Inconclusive (f''(c) = 0)"
            
    return classifications

def find_absolute_extrema(engine: FunctionEngine, a: float, b: float) -> dict:
    """Closed Interval Method for [a, b]."""
    crit_pts = [c for c in find_critical_points(engine) if a <= c <= b]
    test_pts = [a, b] + crit_pts
    
    evaluations = {}
    for p in test_pts:
        _, val = engine.evaluate(p)
        if isinstance(val, float):
            evaluations[p] = val
            
    if not evaluations:
        return {"Max": None, "Min": None}
        
    abs_max_pt = max(evaluations, key=evaluations.get)
    abs_min_pt = min(evaluations, key=evaluations.get)
    
    return {
        "Absolute Maximum": {"x": abs_max_pt, "f(x)": evaluations[abs_max_pt]},
        "Absolute Minimum": {"x": abs_min_pt, "f(x)": evaluations[abs_min_pt]}
    }
