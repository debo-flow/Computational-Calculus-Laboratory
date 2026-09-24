import numpy as np
from typing import Callable, Dict, List, Tuple
from numerical.ode_solvers import solve_fixed_step, solve_adaptive
from numerical.validation import calculate_absolute_error

def run_convergence_study(f: Callable, exact_func: Callable, x0: float, y0: np.ndarray, x_end: float, base_h: float, method: str = 'RK4') -> List[Dict]:
    """
    Evaluates empirical convergence order p ~ log(E1/E2) / log(h1/h2).
    error is proportional to h^p.
    """
    h_vals = [base_h, base_h/2.0, base_h/4.0, base_h/8.0]
    results = []
    prev_err = None
    prev_h = None
    
    for h in h_vals:
        x_num, y_num, stat = solve_fixed_step(f, x0, y0, x_end, h, method)
        if stat != "SUCCESS":
            continue
            
        exact_y = np.array([exact_func(xi) for xi in x_num])
        
        # Max Absolute Error over the interval
        abs_errs = np.linalg.norm(exact_y - y_num[:, 0]) # Assuming scalar ODE for basic convergence study
        max_err = float(np.max(np.abs(exact_y - y_num[:, 0])))
        
        p_est = "N/A"
        if prev_err is not None and max_err > 0 and prev_h > 0:
            p_est = np.log(prev_err / max_err) / np.log(prev_h / h)
            
        results.append({
            "Step Size (h)": h,
            "Max Error": max_err,
            "Observed Order (p)": p_est
        })
        
        prev_err = max_err
        prev_h = h
        
    return results
