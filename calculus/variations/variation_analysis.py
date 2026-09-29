import numpy as np
import sympy as sp
from .functional import Functional
from .euler_lagrange import derive_euler_lagrange

def calculate_el_residual(functional: Functional, x_vals: np.ndarray, y_vals: np.ndarray) -> np.ndarray:
    """Evaluates the discrete numerical residual of the Euler-Lagrange equation."""
    el_data = derive_euler_lagrange(functional)
    eq_lhs = el_data["EL Equation"].lhs
    
    f_lam = sp.lambdify((functional.x, functional.y, functional.yp, functional.ypp), eq_lhs, modules=['numpy'])
    
    dx = x_vals[1] - x_vals[0]
    yp_vals = np.gradient(y_vals, dx)
    ypp_vals = np.gradient(yp_vals, dx)
    
    try:
        residuals = f_lam(x_vals, y_vals, yp_vals, ypp_vals)
        return residuals
    except Exception:
        return np.full_like(x_vals, np.nan)
