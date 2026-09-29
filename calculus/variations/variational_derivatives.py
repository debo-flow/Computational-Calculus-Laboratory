import sympy as sp
from .functional import Functional

def compute_first_variation(functional: Functional) -> dict:
    """Computes δJ = d/dε J[y + εη] | ε=0."""
    x = functional.x
    eta = sp.Function('eta')(x)
    eps = sp.Symbol('epsilon', real=True)
    
    y_pert = functional.y + eps * eta
    yp_pert = sp.diff(y_pert, x)
    
    sym_y, sym_yp = sp.symbols('y yp')
    F_sym = functional.integrand.subs({functional.yp: sym_yp, functional.y: sym_y})
    
    F_pert = F_sym.subs({sym_yp: yp_pert, sym_y: y_pert})
    
    dF_deps = sp.diff(F_pert, eps)
    first_variation = sp.simplify(dF_deps.subs(eps, 0))
    
    return {
        "Perturbed y": y_pert,
        "Perturbed F": F_pert,
        "First Variation δF": first_variation,
        "Interpretation": "Integral of δF yields δJ. Setting δJ = 0 for arbitrary η leads directly to the Euler-Lagrange equations."
    }
