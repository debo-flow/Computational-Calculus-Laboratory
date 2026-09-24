import numpy as np
from typing import Dict, List

def compute_ode_error(exact_y: np.ndarray, num_y: np.ndarray) -> Dict[str, float]:
    """Computes global error bounds for ODE solvers when an exact reference exists."""
    abs_errors = np.abs(exact_y - num_y)
    
    # Ignore zero denominators safely
    with np.errstate(divide='ignore', invalid='ignore'):
        rel_errors = np.where(exact_y != 0, abs_errors / np.abs(exact_y), 0)
        
    rms_error = np.sqrt(np.mean(abs_errors**2))
    
    return {
        "Maximum Absolute Error": float(np.max(abs_errors)),
        "Maximum Relative Error": float(np.max(rel_errors)),
        "RMS Error": float(rms_error)
    }

