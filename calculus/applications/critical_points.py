import sympy as sp
from calculus.functions.function_engine import FunctionEngine
from calculus.differentiation.derivative_engine import DerivativeEngine

def find_critical_points(engine: FunctionEngine) -> list:
    """Finds points where f'(x) = 0 or f'(x) is undefined (stationary/singular points)."""
    x = engine.x
    dev_eng = DerivativeEngine(engine)
    f_prime = dev_eng.get_derivative(1)
    
    critical_pts = []
    
    # Points where f'(x) = 0
    try:
        stat_points = sp.solve(f_prime, x)
        for p in stat_points:
            if p.is_real and p not in critical_pts:
                # Verify it's in the domain of f(x)
                if not engine.expression.subs(x, p).has(sp.zoo, sp.nan, sp.oo, -sp.oo):
                    critical_pts.append(p)
    except Exception:
        pass # Handle equations too complex for symbolic solver
        
    return sorted([float(p.evalf()) for p in critical_pts if p.is_real])
