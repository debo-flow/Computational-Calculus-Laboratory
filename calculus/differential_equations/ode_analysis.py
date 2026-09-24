import sympy as sp
import numpy as np
from typing import Dict, List, Callable

def classify_ode(eq_str: str, func_name: str = 'y', var_name: str = 'x') -> dict:
    """Rigorous symbolic classification of an ODE."""
    x = sp.Symbol(var_name, real=True)
    y = sp.Function(func_name)(x)
    
    lhs, rhs = eq_str.split('=') if '=' in eq_str else (eq_str, "0")
    ode_expr = sp.simplify(sp.sympify(lhs) - sp.sympify(rhs))
    
    try:
        hints = sp.classify_ode(sp.Eq(ode_expr, 0), y)
        order = sp.ode_order(ode_expr, y)
        hints_str = [str(h) for h in hints]
        
        is_linear = any("linear" in h.lower() for h in hints_str)
        is_homo = any("homogeneous" in h.lower() for h in hints_str)
        is_exact = any("exact" in h.lower() for h in hints_str)
        is_bernoulli = any("bernoulli" in h.lower() for h in hints_str)
        is_separable = any("separable" in h.lower() for h in hints_str)
        
        return {
            "Order": order,
            "Linearity": "Linear" if is_linear else "Nonlinear",
            "Homogeneity": "Homogeneous" if is_homo else "Non-homogeneous",
            "Autonomous": "Autonomous" if not ode_expr.has(x) else "Non-autonomous",
            "Exact": is_exact,
            "Separable": is_separable,
            "Bernoulli": is_bernoulli,
            "Supported Methods": hints_str
        }
    except Exception as e:
        return {"Error": f"Classification inconclusive: {str(e)}"}

def empirical_convergence_study(f: Callable, exact_func: Callable, x0: float, y0: np.ndarray, x_end: float, base_h: float, solver_func) -> List[Dict]:
    """Estimates empirical convergence order p ~ log(E1/E2) / log(h1/h2)."""
    h_vals = [base_h, base_h/2.0, base_h/4.0, base_h/8.0]
    results = []
    prev_err, prev_h = None, None
    
    for h in h_vals:
        x_num, y_num, stat = solver_func(f, x0, y0, x_end, h)
        if stat != "SUCCESS": continue
            
        exact_y = np.array([exact_func(xi) for xi in x_num])
        max_err = float(np.max(np.abs(exact_y - y_num[:, 0])))
        
        p_est = "N/A"
        if prev_err is not None and max_err > 0 and prev_h > 0:
            p_est = np.log(prev_err / max_err) / np.log(prev_h / h)
            
        results.append({
            "Step Size (h)": h,
            "Max Absolute Error": max_err,
            "Observed Order (p)": p_est
        })
        prev_err, prev_h = max_err, h
        
    return results
