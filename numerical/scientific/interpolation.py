import numpy as np
from scipy.interpolate import CubicSpline
from typing import Dict

def cubic_spline_interpolation(x_data: list, y_data: list, eval_points: list, bc_type: str = 'natural') -> Dict:
    """Constructs a cubic spline and evaluates it at target points."""
    x = np.array(x_data)
    y = np.array(y_data)
    
    # Sort data strictly
    sort_idx = np.argsort(x)
    x, y = x[sort_idx], y[sort_idx]
    
    cs = CubicSpline(x, y, bc_type=bc_type)
    x_eval = np.array(eval_points)
    y_eval = cs(x_eval)
    
    return {
        "x_eval": x_eval.tolist(),
        "y_eval": y_eval.tolist(),
        "Spline Coefficients": cs.c.tolist()
    }
