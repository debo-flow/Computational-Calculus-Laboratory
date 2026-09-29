from typing import Callable, Dict

def richardson_extrapolation(f: Callable, x: float, h: float) -> Dict:
    """Estimates higher-order derivative approximation using Richardson Extrapolation."""
    # Central difference D(h)
    D_h = (f(x + h) - f(x - h)) / (2 * h)
    # Central difference D(h/2)
    D_h2 = (f(x + h/2) - f(x - h/2)) / h
    
    # Extrapolated result: A = (4*A(h/2) - A(h)) / 3
    extrapolated = (4 * D_h2 - D_h) / 3.0
    truncation_est = abs(extrapolated - D_h2)
    
    return {
        "D(h)": D_h,
        "D(h/2)": D_h2,
        "Richardson Extrapolation": extrapolated,
        "Estimated Truncation Error": truncation_est
    }
