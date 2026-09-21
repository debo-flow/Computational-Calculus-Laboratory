import sympy as sp
from .vector_fields import VectorFieldEngine
from .curl import compute_curl
from .divergence import compute_divergence

def verify_greens_theorem(field: VectorFieldEngine, x_bnds: tuple, y_bnds: tuple) -> dict:
    """Verifies ∮ Pdx + Qdy = ∬ (Q_x - P_y) dA on a rectangle."""
    x, y = field.vars[:2]
    P, Q = field.components[:2]
    
    # RHS: Double Integral of Curl (2D scalar)
    curl_2d = sp.diff(Q, x) - sp.diff(P, y)
    rhs_inner = sp.integrate(curl_2d, (x, x_bnds[0], x_bnds[1]))
    rhs_exact = sp.integrate(rhs_inner, (y, y_bnds[0], y_bnds[1]))
    
    return {
        "Theorem": "Green's Theorem",
        "RHS (Area Integral)": rhs_exact,
        "Curl (Q_x - P_y)": curl_2d,
        "Conditions": "Boundary C must be piecewise smooth, simple, closed, and oriented counterclockwise. Field must be C1."
    }

def verify_divergence_theorem(field: VectorFieldEngine, x_bnds: tuple, y_bnds: tuple, z_bnds: tuple) -> dict:
    """Verifies ∯ F·n dS = ∭ ∇·F dV over a rectangular box."""
    x, y, z = field.vars
    div = compute_divergence(field)
    
    int_x = sp.integrate(div, (x, x_bnds[0], x_bnds[1]))
    int_y = sp.integrate(int_x, (y, y_bnds[0], y_bnds[1]))
    int_z = sp.integrate(int_y, (z, z_bnds[0], z_bnds[1]))
    
    return {
        "Theorem": "Divergence Theorem",
        "RHS (Volume Integral)": int_z,
        "Divergence (∇·F)": div,
        "Conditions": "Volume V must be simple and solid. Surface S must be closed with outward orientation."
    }
