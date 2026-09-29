import sympy as sp
from .functional import Functional

def derive_euler_lagrange(functional: Functional) -> dict:
    """
    Derives the Euler-Lagrange equation: ∂F/∂y - d/dx(∂F/∂y') + d^2/dx^2(∂F/∂y'') = 0.
    """
    F = functional.integrand
    x, y, yp, ypp = functional.x, functional.y, functional.yp, functional.ypp
    
    # Partial derivatives (treating y, yp, ypp as independent symbols momentarily for clean differentiation)
    sy, syp, sypp = sp.symbols('sy syp sypp')
    F_sym = F.subs({ypp: sypp, yp: syp, y: sy})
    
    dF_dy_sym = sp.diff(F_sym, sy)
    dF_dyp_sym = sp.diff(F_sym, syp)
    dF_dypp_sym = sp.diff(F_sym, sypp)
    
    # Back-substitute functions
    dF_dy = dF_dy_sym.subs({sypp: ypp, syp: yp, sy: y})
    dF_dyp = dF_dyp_sym.subs({sypp: ypp, syp: yp, sy: y})
    dF_dypp = dF_dypp_sym.subs({sypp: ypp, syp: yp, sy: y})
    
    # Total derivatives
    d_dx_dF_dyp = sp.diff(dF_dyp, x)
    d2_dx2_dF_dypp = sp.diff(dF_dypp, x, 2)
    
    el_lhs = sp.simplify(dF_dy - d_dx_dF_dyp + d2_dx2_dF_dypp)
    
    return {
        "∂F/∂y": dF_dy,
        "∂F/∂y'": dF_dyp,
        "d/dx(∂F/∂y')": d_dx_dF_dyp,
        "EL Equation": sp.Eq(el_lhs, 0),
        "Is Higher Order": dF_dypp != 0
    }
