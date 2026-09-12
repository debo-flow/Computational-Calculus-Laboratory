import numpy as np
from calculus.functions.function_engine import FunctionEngine
from calculus.differentiation.derivative_engine import DerivativeEngine

def theoretical_error_bound(engine: FunctionEngine, a: float, b: float, n: int, method: str) -> dict:
    """Estimates the theoretical error bounds for closed Newton-Cotes formulas."""
    dev_eng = DerivativeEngine(engine)
    
    # Numerically sample to find max derivative (symbolic global optimization is too brittle here)
    x_vals = np.linspace(a, b, 1000)
    
    try:
        if method == "Trapezoidal":
            # Bound: K * (b-a)^3 / (12 * n^2), where K = max |f''(x)|
            deriv_vals = [abs(dev_eng.evaluate_derivative(x, 2)) for x in x_vals]
            if any(isinstance(v, str) for v in deriv_vals):
                return {"Bound": "N/A (Derivative singularity)"}
            max_d2 = max(deriv_vals)
            bound = max_d2 * ((b - a)**3) / (12 * n**2)
            return {"Derivative Used": "f''(x)", "Max Magnitude": max_d2, "Error Bound": bound}
            
        elif method == "Simpson 1/3":
            # Bound: K * (b-a)^5 / (180 * n^4), where K = max |f^(4)(x)|
            deriv_vals = [abs(dev_eng.evaluate_derivative(x, 4)) for x in x_vals]
            if any(isinstance(v, str) for v in deriv_vals):
                return {"Bound": "N/A (Derivative singularity)"}
            max_d4 = max(deriv_vals)
            bound = max_d4 * ((b - a)**5) / (180 * n**4)
            return {"Derivative Used": "f^(4)(x)", "Max Magnitude": max_d4, "Error Bound": bound}
            
        return {"Bound": "Method not supported for theoretical bound calculation."}
    except Exception as e:
        return {"Bound": f"Error calculating bounds: {str(e)}"}
