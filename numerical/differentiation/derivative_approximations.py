import numpy as np
from typing import List, Tuple, Union
from calculus.functions.function_engine import FunctionEngine
from numerical.differentiation.finite_difference import FiniteDifferenceStencil

def apply_stencil(engine: FunctionEngine, x: float, h: float, stencil: FiniteDifferenceStencil) -> Union[float, str]:
    """Applies a finite difference stencil to a continuous function."""
    if h == 0:
        return "Undefined (h=0)"
        
    result = 0.0
    for offset, coeff in stencil.coefficients.items():
        eval_x = x + (offset * h)
        _, f_val = engine.evaluate(eval_x)
        
        if isinstance(f_val, str):
            return f"Undefined (Evaluation failed at {eval_x})"
            
        result += coeff * f_val
        
    return result / (h ** stencil.derivative_order)

def differentiate_discrete_data(x_data: List[float], y_data: List[float]) -> List[float]:
    """
    Differentiates discrete data. 
    Uses 2nd-order non-uniform approximations for interior points, 
    and 1st-order forward/backward for the edges.
    """
    n = len(x_data)
    if n < 2 or len(x_data) != len(y_data):
        raise ValueError("Data must have at least 2 points and matching lengths.")
        
    derivatives = np.zeros(n)
    
    # Left edge (Forward difference)
    derivatives[0] = (y_data[1] - y_data[0]) / (x_data[1] - x_data[0])
    
    # Interior points (Non-uniform central difference)
    for i in range(1, n - 1):
        h1 = x_data[i] - x_data[i-1]
        h2 = x_data[i+1] - x_data[i]
        
        # Exact weights for non-uniform grid to achieve O(h^2)
        w1 = -h2 / (h1 * (h1 + h2))
        w2 = (h2 - h1) / (h1 * h2)
        w3 = h1 / (h2 * (h1 + h2))
        
        derivatives[i] = w1 * y_data[i-1] + w2 * y_data[i] + w3 * y_data[i+1]
        
    # Right edge (Backward difference)
    derivatives[-1] = (y_data[-1] - y_data[-2]) / (x_data[-1] - x_data[-2])
    
    return derivatives.tolist()

