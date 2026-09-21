import numpy as np
from scipy.integrate import solve_ivp

def solve_adaptive_rk45(f, x0, y0, x_end, rtol=1e-5, atol=1e-8):
    """Uses robust adaptive Runge-Kutta (RK45) from SciPy."""
    def scipy_f(t, y):
        return f(t, y)
    
    sol = solve_ivp(scipy_f, [x0, x_end], y0, method='RK45', rtol=rtol, atol=atol)
    
    status = "SUCCESS" if sol.success else f"FAILED ({sol.message})"
    return sol.t, sol.y.T, status
