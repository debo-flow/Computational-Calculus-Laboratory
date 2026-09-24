import sympy as sp
import numpy as np
from typing import Dict, Any, List, Callable
from .numerical_solver import solve_fixed_step

def classify_ode(eq_str: str, func_name: str = 'y', var_name: str = 'x') -> dict:
    """Classifies symbolic ODEs strictly returning known types."""
    x = sp.Symbol(var_name, real=True)
    y = sp.Function(func_name)(x)
    
    eq_parts = eq_str.split('=')
    lhs, rhs = sp.sympify(eq_parts[0]), sp.sympify(eq_parts[1]) if len(eq_parts) > 1 else sp.S.Zero
    ode_expr = sp.simplify(lhs - rhs)
    
    try:
        classifications = sp.classify_ode(sp.Eq(ode_expr, 0), y)
        order = sp.ode_order(ode_expr, y)
        is_linear = any("linear" in str(c).lower() for c in classifications)
        is_homo = any("homogeneous" in str(c).lower() for c in classifications)
        
        return {
            "Order": order,
            "Linearity": "Linear" if is_linear else "Nonlinear",
            "Homogeneity": "Homogeneous" if is_homo else "Non-homogeneous",
            "Autonomous": "Autonomous" if not ode_expr.has(x) else "Non-autonomous",
            "Supported Methods": classifications
        }
    except Exception as e:
        return {"Error": str(e)}

def compute_error_metrics(y_exact: np.ndarray, y_num: np.ndarray) -> Dict[str, float]:
    """Computes global error bounds for ODE solvers."""
    abs_errors = np.abs(y_exact - y_num)
    with np.errstate(divide='ignore', invalid='ignore'):
        rel_errors = np.where(np.abs(y_exact) > 1e-12, abs_errors / np.abs(y_exact), 0)
        
    return {
        "Max Absolute Error": float(np.max(abs_errors)),
        "Max Relative Error": float(np.max(rel_errors)),
        "RMS Error": float(np.sqrt(np.mean(abs_errors**2)))
    }

def step_size_convergence_study(f: Callable, exact_func: Callable, x0: float, y0: np.ndarray, x_end: float, base_h: float, method: str) -> List[Dict]:
    """Evaluates empirical convergence order p ~ log(E1/E2) / log(h1/h2)."""
    h_vals = [base_h, base_h/2.0, base_h/4.0, base_h/8.0]
    results = []
    prev_err, prev_h = None, None
    
    for h in h_vals:
        x_num, y_num, stat = solve_fixed_step(f, x0, y0, x_end, h, method)
        if stat != "SUCCESS": continue
            
        exact_y = np.array([exact_func(xi) for xi in x_num])
        max_err = float(np.max(np.abs(exact_y - y_num[:, 0])))
        
        p_est = "N/A"
        if prev_err is not None and max_err > 0 and prev_h > 0:
            p_est = np.log(prev_err / max_err) / np.log(prev_h / h)
            
        results.append({
            "Step Size (h)": h,
            "Max Absolute Error": max_err,
            "Experimental Order (p)": p_est
        })
        prev_err, prev_h = max_err, h
        
    return results
