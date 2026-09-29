import sympy as sp
from typing import Dict

def compute_exterior_derivative_1form(P_str: str, Q_str: str, R_str: str, vars_str: str) -> Dict[str, sp.Expr]:
    """d(P dx + Q dy + R dz) = (R_y - Q_z) dy^dz + (P_z - R_x) dz^dx + (Q_x - P_y) dx^dy"""
    x, y, z = sp.symbols(vars_str)
    P, Q, R = sp.sympify(P_str), sp.sympify(Q_str), sp.sympify(R_str)
    
    dy_dz = sp.simplify(sp.diff(R, y) - sp.diff(Q, z))
    dz_dx = sp.simplify(sp.diff(P, z) - sp.diff(R, x))
    dx_dy = sp.simplify(sp.diff(Q, x) - sp.diff(P, y))
    
    return {
        "dy ∧ dz": dy_dz,
        "dz ∧ dx": dz_dx,
        "dx ∧ dy": dx_dy,
        "Interpretation": "The exterior derivative of a 1-form perfectly mirrors the Curl operator in vector calculus."
    }
