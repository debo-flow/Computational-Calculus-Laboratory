import sympy as sp
from typing import Dict, Any
from .vector_engine import VectorFunctionEngine

def compute_kinematics(engine: VectorFunctionEngine) -> Dict[str, Any]:
    """Computes velocity (r'), acceleration (r''), and speed (|r'|)."""
    t = engine.t
    r = engine.components
    v = [sp.diff(c, t) for c in r]
    a = [sp.diff(c, t) for c in v]
    speed = sp.simplify(sp.sqrt(sum(vc**2 for vc in v)))
    
    return {"Velocity (v)": v, "Acceleration (a)": a, "Speed (|v|)": speed}

def compute_arc_length(engine: VectorFunctionEngine, t_a: float, t_b: float) -> Dict[str, Any]:
    """L = ∫ |r'(t)| dt"""
    speed = compute_kinematics(engine)["Speed (|v|)"]
    try:
        sym_len = sp.integrate(speed, (engine.t, t_a, t_b))
        num_len = float(sym_len.evalf()) if sym_len.is_real else "N/A"
        return {"Integral": sym_len, "Numerical": num_len, "Integrand (Speed)": speed}
    except Exception as e:
        return {"Status": "Failed", "Error": str(e)}

