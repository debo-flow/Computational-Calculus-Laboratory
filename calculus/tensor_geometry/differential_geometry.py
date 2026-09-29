import sympy as sp
from typing import Dict, Any

def compute_surface_geometry(x_str: str, y_str: str, z_str: str, uv_vars: str) -> Dict[str, Any]:
    """Computes First and Second Fundamental Forms, Gaussian (K) and Mean (H) Curvature."""
    u, v = sp.symbols(uv_vars)
    r = sp.Matrix([sp.sympify(x_str), sp.sympify(y_str), sp.sympify(z_str)])
    
    r_u = sp.diff(r, u)
    r_v = sp.diff(r, v)
    
    # First Fundamental Form coefficients
    E = sp.simplify(r_u.dot(r_u))
    F = sp.simplify(r_u.dot(r_v))
    G = sp.simplify(r_v.dot(r_v))
    
    cross_uv = r_u.cross(r_v)
    mag_cross = sp.simplify(sp.sqrt(cross_uv.dot(cross_uv)))
    
    if mag_cross == 0:
        return {"Status": "Failed", "Error": "Degenerate surface (zero cross product)."}
        
    normal = sp.simplify(cross_uv / mag_cross)
    
    # Second Fundamental Form coefficients
    r_uu = sp.diff(r_u, u)
    r_uv = sp.diff(r_u, v)
    r_vv = sp.diff(r_v, v)
    
    e = sp.simplify(normal.dot(r_uu))
    f = sp.simplify(normal.dot(r_uv))
    g = sp.simplify(normal.dot(r_vv))
    
    # Curvatures
    EG_F2 = sp.simplify(E*G - F**2)
    K = sp.simplify((e*g - f**2) / EG_F2) # Gaussian Curvature
    H = sp.simplify((e*G - 2*f*F + g*E) / (2 * EG_F2)) # Mean Curvature
    
    return {
        "Status": "Success",
        "E": E, "F": F, "G": G,
        "e": e, "f": f, "g": g,
        "Normal (n)": normal,
        "Gaussian Curvature (K)": K,
        "Mean Curvature (H)": H,
        "Surface Area Element (dA)": mag_cross
    }
