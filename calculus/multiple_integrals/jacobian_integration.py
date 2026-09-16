import sympy as sp
from typing import Dict, Any
from calculus.multivariable.jacobian import compute_jacobian
from .coordinate_transformations import get_polar_transformation, get_cylindrical_transformation, get_spherical_transformation

def apply_coordinate_transformation(expr: sp.Expr, transform_data: Dict[str, Any]) -> Dict[str, Any]:
    """Applies a coordinate transformation, calculates the Jacobian, and returns the transformed integrand."""
    old_vars = transform_data["Old"]
    new_vars = transform_data["New"]
    eqs = transform_data["Equations"]
    
    # 1. Substitute variables
    sub_map = dict(zip(old_vars, eqs))
    transformed_expr = sp.simplify(expr.subs(sub_map))
    
    # 2. Compute Jacobian Det
    j_vars_str = ", ".join([str(v) for v in new_vars])
    eqs_str = [str(e) for e in eqs]
    j_res = compute_jacobian(eqs_str, j_vars_str)
    j_det = j_res["Determinant"]
    
    # Absolute value of Jacobian factor |J|
    # (Assuming standard positive orientations for r, rho, phi)
    if transform_data["Name"] in ["Polar", "Cylindrical"]:
        abs_j = new_vars[0] # r
    elif transform_data["Name"] == "Spherical":
        abs_j = new_vars[0]**2 * sp.sin(new_vars[1]) # rho^2 sin(phi)
    else:
        abs_j = sp.Abs(j_det)
        
    final_integrand = sp.simplify(transformed_expr * abs_j)
    
    return {
        "Transformation": transform_data["Name"],
        "Substitutions": sub_map,
        "f(u,v)": transformed_expr,
        "Jacobian Determinant (J)": j_det,
        "Absolute Jacobian Factor |J|": abs_j,
        "Final Integrand f(u,v)|J|": final_integrand
    }
