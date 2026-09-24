import numpy as np
from .rk4 import solve_fixed_step

def shooting_method(f_sys, a: float, b: float, alpha: float, beta: float, v_guess1: float, v_guess2: float, h: float, tol: float = 1e-5) -> dict:
    """
    Shooting Method for y'' = f(x, y, y').
    Converts BVP to IVP and uses Secant method to find the correct initial slope v = y'(a).
    """
    def shoot(v):
        # f_sys expects (x, Y) where Y = [y, y']
        x_vals, Y_vals, status = solve_fixed_step(f_sys, a, np.array([alpha, v]), b, h, 'RK4')
        if status != "SUCCESS":
            raise ValueError("RK4 Integration Failed during shooting.")
        return Y_vals[-1][0] - beta, x_vals, Y_vals

    try:
        F1, _, _ = shoot(v_guess1)
        F2, _, _ = shoot(v_guess2)
        
        v1, v2 = v_guess1, v_guess2
        for i in range(20): # Max iterations
            if abs(F2 - F1) < 1e-12:
                break
            
            # Secant Method step
            v_new = v2 - F2 * (v2 - v1) / (F2 - F1)
            F_new, x_vals, Y_vals = shoot(v_new)
            
            if abs(F_new) < tol:
                return {
                    "Status": "Converged", 
                    "Iterations": i+1, 
                    "Initial Slope y'(a)": v_new, 
                    "Terminal Error": abs(F_new),
                    "x": x_vals, 
                    "y": Y_vals[:, 0]
                }
                
            v1, F1 = v2, F2
            v2, F2 = v_new, F_new
            
        return {"Status": "Failed to converge within iterations"}
    except Exception as e:
        return {"Status": f"Failed: {str(e)}"}

def finite_difference_bvp_linear(p_func, q_func, r_func, a: float, b: float, alpha: float, beta: float, n: int) -> dict:
    """
    Finite Difference Method for Linear BVP: y'' + p(x)y' + q(x)y = r(x)
    y(a) = alpha, y(b) = beta
    """
    x_vals = np.linspace(a, b, n+1)
    h = (b - a) / n
    
    A = np.zeros((n-1, n-1))
    B = np.zeros(n-1)
    
    try:
        for i in range(1, n):
            xi = x_vals[i]
            p, q, r = p_func(xi), q_func(xi), r_func(xi)
            
            idx = i - 1
            A[idx, idx] = -2/h**2 + q
            if idx > 0:
                A[idx, idx-1] = 1/h**2 - p/(2*h)
            if idx < n-2:
                A[idx, idx+1] = 1/h**2 + p/(2*h)
                
            B[idx] = r
            if i == 1:
                B[idx] -= alpha * (1/h**2 - p/(2*h))
            if i == n - 1:
                B[idx] -= beta * (1/h**2 + p/(2*h))
                
        y_int = np.linalg.solve(A, B)
        y_vals = np.concatenate(([alpha], y_int, [beta]))
        return {"Status": "Success", "x": x_vals, "y": y_vals}
    except Exception as e:
        return {"Status": f"Matrix Solver Failed: {str(e)}"}

