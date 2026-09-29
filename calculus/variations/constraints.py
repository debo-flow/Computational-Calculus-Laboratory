import sympy as sp
from .functional import Functional

def setup_isoperimetric_problem(F_str: str, G_str: str) -> dict:
    """Constructs the modified Lagrangian H = F + \lambda G."""
    lam = sp.Symbol('lambda', real=True)
    
    F_func = Functional(F_str)
    G_func = Functional(G_str)
    
    H_integrand = F_func.integrand + lam * G_func.integrand
    H_func = Functional(str(H_integrand)) # Proxy functional
    
    return {
        "Objective Integrand F": F_func.integrand,
        "Constraint Integrand G": G_func.integrand,
        "Modified Integrand H": H_integrand,
        "Multiplier": lam
    }
