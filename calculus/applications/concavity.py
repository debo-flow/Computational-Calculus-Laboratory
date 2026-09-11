import sympy as sp
from calculus.functions.function_engine import FunctionEngine
from calculus.differentiation.derivative_engine import DerivativeEngine

def find_inflection_points(engine: FunctionEngine) -> dict:
    """Finds candidates where f''(x) = 0 and verifies concavity change."""
    x = engine.x
    dev_eng = DerivativeEngine(engine)
    f_double_prime = dev_eng.get_derivative(2)
    
    inflection_pts = {}
    try:
        candidates = sp.solve(f_double_prime, x)
        for c in candidates:
            if c.is_real:
                c_val = float(c.evalf())
                # Verify concavity change using tiny step
                h = 1e-5
                left_concavity = dev_eng.evaluate_derivative(c_val - h, 2)
                right_concavity = dev_eng.evaluate_derivative(c_val + h, 2)
                
                if isinstance(left_concavity, float) and isinstance(right_concavity, float):
                    if left_concavity * right_concavity < 0:
                        inflection_pts[c_val] = "Verified Inflection Point"
                    else:
                        inflection_pts[c_val] = "Candidate Only (No Concavity Change)"
    except Exception:
        pass
        
    return inflection_pts
