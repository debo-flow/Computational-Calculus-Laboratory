import sympy as sp
from typing import Dict, Any, Tuple
from calculus.multivariable.multivariable_engine import MultivariableEngine
from .double_integrals import compute_double_integral

def compute_lamina_properties(density_expr: str, x_bnds: Tuple[Any, Any], y_bnds: Tuple[Any, Any]) -> Dict[str, Any]:
    """Computes Mass, Centroid (x_bar, y_bar), and Moments of Inertia (I_x, I_y, I_0)."""
    rho_eng = MultivariableEngine(density_expr, "x, y")
    x, y = rho_eng.vars
    
    # Mass M = ∫∫ ρ dA
    mass_res = compute_double_integral(rho_eng, x_bnds, y_bnds, "yx")
    M = mass_res["Exact Result"]
    
    if M == 0 or not mass_res["Status"] == "Success":
        return {"Status": "Failed", "Error": "Mass is zero or integral failed."}
        
    # Moments M_y = ∫∫ x*ρ dA, M_x = ∫∫ y*ρ dA
    M_y = compute_double_integral(MultivariableEngine(str(x * rho_eng.expression), "x, y"), x_bnds, y_bnds, "yx")["Exact Result"]
    M_x = compute_double_integral(MultivariableEngine(str(y * rho_eng.expression), "x, y"), x_bnds, y_bnds, "yx")["Exact Result"]
    
    # Centroid
    x_bar = sp.simplify(M_y / M)
    y_bar = sp.simplify(M_x / M)
    
    # Moments of Inertia
    I_x = compute_double_integral(MultivariableEngine(str(y**2 * rho_eng.expression), "x, y"), x_bnds, y_bnds, "yx")["Exact Result"]
    I_y = compute_double_integral(MultivariableEngine(str(x**2 * rho_eng.expression), "x, y"), x_bnds, y_bnds, "yx")["Exact Result"]
    I_0 = sp.simplify(I_x + I_y) # Polar moment
    
    return {
        "Status": "Success",
        "Mass (M)": M,
        "Centroid (x_bar, y_bar)": (x_bar, y_bar),
        "Moment M_x": M_x,
        "Moment M_y": M_y,
        "Inertia I_x": I_x,
        "Inertia I_y": I_y,
        "Polar Inertia I_0": I_0
    }
