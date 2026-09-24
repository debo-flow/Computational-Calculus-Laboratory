import numpy as np
from scipy.integrate import solve_ivp
from typing import Callable, Tuple, Dict, Any

def euler_step(f, x, y, h): return y + h * f(x, y)
def heun_step(f, x, y, h): 
    k1 = f(x, y)
    return y + (h / 2.0) * (k1 + f(x + h, y + h * k1))
def midpoint_step(f, x, y, h): 
    return y + h * f(x + h/2.0, y + (h/2.0) * f(x, y))
def rk4_step(f, x, y, h):
    k1 = f(x, y)
    k2 = f(x + h/2.0, y + (h/2.0) * k1)
    k3 = f(x + h/2.0, y + (h/2.0) * k2)
    k4 = f(x + h, y + h * k3)
    return y + (h / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

def solve_fixed_step(f: Callable, x0: float, y0: np.ndarray, x_end: float, h: float, method: str = 'RK4') -> Tuple[np.ndarray, np.ndarray, str]:
    steps = int(np.ceil((x_end - x0) / h))
    x_vals = np.linspace(x0, x0 + steps*h, steps + 1)
    y_vals = np.zeros((steps + 1, len(np.atleast_1d(y0))))
    y_vals[0] = y0
    
    methods = {'Euler': euler_step, 'Heun': heun_step, 'Midpoint': midpoint_step, 'RK4': rk4_step}
    step_func = methods.get(method, rk4_step)
    
    for i in range(steps):
        try:
            y_vals[i+1] = step_func(f, x_vals[i], y_vals[i], h)
            if np.any(np.isnan(y_vals[i+1])) or np.any(np.isinf(y_vals[i+1])):
                return x_vals[:i+1], y_vals[:i+1], "FAILED (Numerical Instability)"
        except Exception as e:
            return x_vals[:i+1], y_vals[:i+1], f"FAILED ({e})"
    return x_vals, y_vals, "SUCCESS"

def solve_adaptive(f: Callable, x0: float, y0: np.ndarray, x_end: float, rtol: float = 1e-5, atol: float = 1e-8) -> Tuple[np.ndarray, np.ndarray, dict]:
    sol = solve_ivp(lambda t, y: f(t, y), [x0, x_end], y0, method='RK45', rtol=rtol, atol=atol)
    status = {"Status": "SUCCESS" if sol.success else f"FAILED ({sol.message})", "Evaluations": sol.nfev, "Steps": len(sol.t)}
    return sol.t, sol.y.T, status
