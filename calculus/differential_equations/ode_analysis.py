import sympy as sp
from typing import Dict, Any

def verify_conservation(sys_exprs: list, vars_str: str, invariant_str: str) -> Dict[str, Any]:
    """Tests if dI/dt = 0 exactly along the trajectories of the system."""
    variables = sp.symbols(vars_str)
    vector_field = [sp.sympify(e) for e in sys_exprs]
    invariant = sp.sympify(invariant_str)
    
    # Chain Rule: dI/dt = ∇I · F
    grad_I = [sp.diff(invariant, v) for v in variables]
    dI_dt = sp.simplify(sum(g * f for g, f in zip(grad_I, vector_field)))
    
    is_conserved = (dI_dt == 0)
    
    return {
        "Candidate Invariant I(X)": invariant,
        "Derivative dI/dt": dI_dt,
        "Is Conserved": is_conserved,
        "Interpretation": "Constant of motion verified." if is_conserved else "Quantity is not conserved."
    }
