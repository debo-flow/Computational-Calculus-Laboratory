import sympy as sp
from typing import List, Dict
from .multivariable_engine import MultivariableEngine
from .gradient import compute_gradient

def directional_derivative(engine: MultivariableEngine, direction: List[float], point: List[float] = None) -> Dict:
    """Computes the directional derivative using the normalized direction vector."""
    grad_data = compute_gradient(engine)
    grad_sym = grad_data["Gradient"]
    
    magnitude = sum(d**2 for d in direction)**0.5
    if magnitude == 0:
        raise ValueError("Direction vector cannot be zero.")
    
    unit_u = [d / magnitude for d in direction]
    D_u_sym = sp.simplify(sum(g * u for g, u in zip(grad_sym, unit_u)))
    
    res = {
        "Unit Vector": unit_u,
        "Symbolic D_u": D_u_sym,
        "Max Rate of Change": grad_data["Magnitude"]
    }
    
    if point:
        sub_map = dict(zip(engine.vars, point))
        res["Evaluated D_u"] = float(D_u_sym.subs(sub_map).evalf())
        
    return res
