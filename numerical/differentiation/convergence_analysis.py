import math
from typing import Dict, Union
from calculus.functions.function_engine import FunctionEngine
from numerical.differentiation.derivative_approximations import apply_stencil
from numerical.differentiation.finite_difference import STENCILS

def richardson_extrapolation(engine: FunctionEngine, x: float, h: float) -> Dict[str, Union[float, str]]:
    """Applies Richardson Extrapolation on the O(h^2) Central Difference to achieve O(h^4)."""
    stencil = STENCILS["Central (2nd Order)"]
    
    A_h = apply_stencil(engine, x, h, stencil)
    A_h_half = apply_stencil(engine, x, h/2.0, stencil)
    
    if isinstance(A_h, str) or isinstance(A_h_half, str):
        return {"Status": "Failed", "Reason": "Function undefined at sample points."}
        
    # Richardson formula for p=2: R = (4*A(h/2) - A(h)) / 3
    extrapolated = (4.0 * A_h_half - A_h) / 3.0
    
    return {
        "Status": "Success",
        "Original A(h)": A_h,
        "Original A(h/2)": A_h_half,
        "Extrapolated (O(h^4))": extrapolated
    }

def estimate_convergence_order(E1: float, E2: float, h1: float, h2: float) -> Union[float, str]:
    """Calculates observed convergence order p ≈ log(E1/E2) / log(h1/h2)"""
    if E1 <= 0 or E2 <= 0 or h1 <= 0 or h2 <= 0 or h1 == h2:
        return "N/A"
    try:
        return math.log(E1 / E2) / math.log(h1 / h2)
    except:
        return "N/A"

