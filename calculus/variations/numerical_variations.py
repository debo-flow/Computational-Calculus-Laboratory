import numpy as np
from scipy.optimize import minimize
from scipy.integrate import simpson
import sympy as sp
from .functional import Functional

def numerical_functional_optimization(functional: Functional, a: float, b: float, A: float, B: float, N: int = 50) -> dict:
    """
    Direct Discretization Method for Functional Optimization.
    Minimizes the discretized integral J[y_i] subject to fixed boundary conditions.
    """
    x_vals = np.linspace(a, b, N)
    dx = x_vals[1] - x_vals[0]
    
    f_lam = sp.lambdify((functional.x, functional.y, functional.yp), functional.integrand, modules=['numpy'])
    
    def objective(y_inner):
        # Reconstruct full y array with fixed boundaries
        y_full = np.concatenate(([A], y_inner, [B]))
        
        # Central difference for derivative (first-order edge fallback)
        yp = np.gradient(y_full, dx)
        
        try:
            integrand_vals = f_lam(x_vals, y_full, yp)
            # Simpson's rule integration
            return simpson(y=integrand_vals, x=x_vals)
        except Exception:
            return 1e9 # Heavy penalty for domain violations (e.g. sqrt of negative)

    # Initial guess: linear interpolation between boundaries
    y_guess = np.linspace(A, B, N)[1:-1]
    
    res = minimize(objective, y_guess, method='BFGS')
    
    if res.success:
        y_opt = np.concatenate(([A], res.x, [B]))
        return {
            "Status": "Converged",
            "J_min": res.fun,
            "x": x_vals,
            "y": y_opt,
            "Iterations": res.nit
        }
    return {"Status": "Failed", "Message": res.message}
