import sympy as sp
from typing import Dict, Any, List
from .vector_fields import VectorFieldEngine

def surface_normal_vector(r_u: List[sp.Expr], r_v: List[sp.Expr]) -> List[sp.Expr]:
    """n = r_u × r_v"""
    u_mat = sp.Matrix(r_u)
    v_mat = sp.Matrix(r_v)
    return list(u_mat.cross(v_mat))

def compute_flux(field: VectorFieldEngine, param_surface: List[str], uv_vars: str, u_bnds: tuple, v_bnds: tuple) -> Dict[str, Any]:
    """Φ = ∬_S F · n dS"""
    u, v = sp.symbols(uv_vars)
    r = [sp.sympify(e) for e in param_surface]
    
    r_u = [sp.diff(c, u) for c in r]
    r_v = [sp.diff(c, v) for c in r]
    normal = surface_normal_vector(r_u, r_v)
    
    sub_map = dict(zip(field.vars, r))
    F_surf = [c.subs(sub_map) for c in field.components]
    
    dot_prod = sp.simplify(sum(f * n for f, n in zip(F_surf, normal)))
    
    try:
        inner = sp.integrate(dot_prod, (u, u_bnds[0], u_bnds[1]))
        outer = sp.integrate(inner, (v, v_bnds[0], v_bnds[1]))
        return {
            "Normal (n)": normal,
            "Integrand F·n": dot_prod,
            "Exact Flux": outer,
            "Numerical": float(outer.evalf()) if outer.is_real else "N/A"
        }
    except Exception as e:
        return {"Status": "Failed", "Error": str(e)}
