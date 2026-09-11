from typing import List, Dict
from calculus.functions.function_engine import FunctionEngine
from numerical.validation import calculate_absolute_error, calculate_relative_error
from numerical.differentiation.finite_difference import FiniteDifferenceStencil
from numerical.differentiation.derivative_approximations import apply_stencil
from numerical.differentiation.convergence_analysis import estimate_convergence_order

def step_size_experiment(engine: FunctionEngine, exact_val: float, x: float, stencil: FiniteDifferenceStencil, h_powers: range = range(1, 16)) -> List[Dict]:
    """Generates error data for h ranging from 10^-1 to 10^-15 to demonstrate round-off cancellation."""
    results = []
    prev_err = None
    prev_h = None
    
    for p in h_powers:
        h = 10.0 ** (-p)
        approx = apply_stencil(engine, x, h, stencil)
        
        if isinstance(approx, str):
            continue
            
        abs_err = calculate_absolute_error(exact_val, approx)
        rel_err = calculate_relative_error(exact_val, approx)
        
        obs_order = "N/A"
        if prev_err is not None and prev_h is not None:
            obs_order = estimate_convergence_order(prev_err, abs_err, prev_h, h)
            
        results.append({
            "h": h,
            "Approximation": approx,
            "Exact": exact_val,
            "Abs Error": abs_err,
            "Rel Error": rel_err,
            "Observed Order": obs_order
        })
        
        prev_err = abs_err
        prev_h = h
        
    return results
