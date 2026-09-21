import sympy as sp
from typing import Dict, Any
from .vector_engine import VectorFunctionEngine
from .vector_fields import VectorFieldEngine
from .vector_functions import compute_kinematics

def vector_line_integral(field: VectorFieldEngine, curve: VectorFunctionEngine, t_a: float, t_b: float) -> Dict[str, Any]:
    """W = ∫_C F · dr = ∫ F(r(t)) · r'(t) dt"""
    t = curve.t
    r = curve.components
    v = compute_kinematics(curve)["Velocity (v)"]
    
    sub_map = dict(zip(field.vars, r))
    F_rt = [comp.subs(sub_map) for comp in field.components]
    
    dot_prod = sp.simplify(sum(f * dr for f, dr in zip(F_rt, v)))
    
    try:
        exact_val = sp.integrate(dot_prod, (t, t_a, t_b))
        num_val = float(exact_val.evalf()) if exact_val.is_real else "N/A"
        return {"Integrand (F·dr)": dot_prod, "Exact": exact_val, "Numerical": num_val}
    except Exception as e:
        return {"Status": "Failed", "Error": str(e)}
