import numpy as np

def rk4_step(f, x, y, h):
    """Classic Runge-Kutta 4th Order (RK4)"""
    k1 = f(x, y)
    k2 = f(x + h/2.0, y + (h/2.0) * k1)
    k3 = f(x + h/2.0, y + (h/2.0) * k2)
    k4 = f(x + h, y + h * k3)
    return y + (h / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

def solve_fixed_step(f, x0, y0, x_end, h, method='RK4'):
    """Iterates a fixed-step solver over [x0, x_end]."""
    steps = int(np.ceil((x_end - x0) / h))
    x_vals = np.linspace(x0, x0 + steps*h, steps + 1)
    y_vals = np.zeros((steps + 1, len(np.atleast_1d(y0))))
    y_vals[0] = y0
    
    methods = {
        'Euler': __import__('numerical.ode.euler', fromlist=['']).euler_step,
        'Heun': __import__('numerical.ode.heun', fromlist=['']).heun_step,
        'Midpoint': __import__('numerical.ode.midpoint', fromlist=['']).midpoint_step,
        'RK4': rk4_step
    }
    step_func = methods.get(method, rk4_step)
    
    for i in range(steps):
        try:
            y_vals[i+1] = step_func(f, x_vals[i], y_vals[i], h)
            if np.any(np.isnan(y_vals[i+1])) or np.any(np.isinf(y_vals[i+1])):
                return x_vals[:i+1], y_vals[:i+1], "FAILED (Numerical Instability)"
        except Exception:
            return x_vals[:i+1], y_vals[:i+1], "FAILED (Evaluation Error)"
            
    return x_vals, y_vals, "SUCCESS"
