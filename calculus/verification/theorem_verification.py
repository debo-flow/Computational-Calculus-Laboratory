import sympy as sp
from typing import Dict

def verify_greens_theorem(P_str: str, Q_str: str, x_bnds: tuple, y_bnds: tuple) -> Dict:
    """
    Computational verification of Green's Theorem: ∮ P dx + Q dy = ∬ (dQ/dx - dP/dy) dA.
    Restricted to rectangular domains for automated benchmark simplicity.
    """
    x, y = sp.symbols('x y')
    P, Q = sp.sympify(P_str), sp.sympify(Q_str)
    
    # 1. Double Integral (RHS)
    curl_2d = sp.diff(Q, x) - sp.diff(P, y)
    rhs_val = sp.integrate(curl_2d, (x, x_bnds[0], x_bnds[1]), (y, y_bnds[0], y_bnds[1]))
    
    # 2. Line Integral (LHS) over 4 boundary segments
    # Bottom: y = y_bnds[0], dx
    I_bottom = sp.integrate(P.subs(y, y_bnds[0]), (x, x_bnds[0], x_bnds[1]))
    # Right: x = x_bnds[1], dy
    I_right = sp.integrate(Q.subs(x, x_bnds[1]), (y, y_bnds[0], y_bnds[1]))
    # Top: y = y_bnds[1], dx (Reverse orientation)
    I_top = sp.integrate(P.subs(y, y_bnds[1]), (x, x_bnds[1], x_bnds[0]))
    # Left: x = x_bnds[0], dy (Reverse orientation)
    I_left = sp.integrate(Q.subs(x, x_bnds[0]), (y, y_bnds[1], y_bnds[0]))
    
    lhs_val = sp.simplify(I_bottom + I_right + I_top + I_left)
    diff = sp.simplify(lhs_val - rhs_val)
    
    status = "SYMBOLICALLY VERIFIED" if diff == 0 else "FAILED"
    
    return {
        "Theorem": "Green's Theorem",
        "LHS (Line Integral)": lhs_val,
        "RHS (Surface Integral)": rhs_val,
        "Difference": diff,
        "Status": status,
        "Disclaimer": "Computational verification for a specific domain. Not a generalized topological proof."
    }
