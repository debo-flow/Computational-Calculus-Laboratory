import numpy as np
from .numerical_solver import solve_fixed_step

def basic_shooting_method(f_sys: callable, a: float, b: float, alpha: float, beta: float, v_guess1: float, v_guess2: float, h: float, tol: float = 1e-5) -> dict:
    """Converts y''=f(x,y,y') BVP to IVP and solves initial slope via Secant method."""
    def shoot(v):
        x_vals, Y_vals, status = solve_fixed_step(f_sys, a, np.array([alpha, v]), b, h, 'RK4')
        if status != "SUCCESS": raise ValueError("Integration Failed.")
        return Y_vals[-1][0] - beta, x_vals, Y_vals

    try:
        F1, _, _ = shoot(v_guess1)
        F2, _, _ = shoot(v_guess2)
        v1, v2 = v_guess1, v_guess2
        
        for i in range(20):
            if abs(F2 - F1) < 1e-12: break
            v_new = v2 - F2 * (v2 - v1) / (F2 - F1)
            F_new, x_vals, Y_vals = shoot(v_new)
            if abs(F_new) < tol:
                return {"Status": "Converged", "Iterations": i+1, "y'(a)": v_new, "Error": abs(F_new), "x": x_vals, "y": Y_vals[:, 0]}
            v1, F1, v2, F2 = v2, F2, v_new, F_new
            
        return {"Status": "Failed to converge"}
    except Exception as e:
        return {"Status": f"Error: {e}"}
