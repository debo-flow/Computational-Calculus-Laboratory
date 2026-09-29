import numpy as np
from typing import Dict, Union

def calculate_errors(computed: Union[float, np.ndarray], reference: Union[float, np.ndarray]) -> Dict[str, float]:
    """Computes rigorous error metrics between computed and reference values."""
    comp, ref = np.atleast_1d(computed), np.atleast_1d(reference)
    
    abs_err = np.abs(comp - ref)
    with np.errstate(divide='ignore', invalid='ignore'):
        rel_err = np.where(np.abs(ref) > 1e-14, abs_err / np.abs(ref), 0.0)
        
    return {
        "Max Absolute Error": float(np.max(abs_err)),
        "Mean Absolute Error": float(np.mean(abs_err)),
        "Max Relative Error": float(np.max(rel_err)),
        "RMS Error": float(np.sqrt(np.mean(abs_err**2)))
    }

def estimate_convergence_order(errors: list, step_sizes: list) -> Union[float, str]:
    """Estimates empirical convergence order p ~ log(E1/E2) / log(h1/h2)."""
    if len(errors) < 2 or errors[-1] == 0:
        return "INCONCLUSIVE (Insufficient data or exact match)"
    p_est = np.log(errors[-2] / errors[-1]) / np.log(step_sizes[-2] / step_sizes[-1])
    return float(p_est)
