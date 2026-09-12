from typing import Dict, Union
from calculus.functions.function_engine import FunctionEngine

def composite_trapezoidal(engine: FunctionEngine, a: float, b: float, n: int) -> Dict[str, Union[float, str, int]]:
    """Evaluates the composite trapezoidal rule."""
    if n < 1:
        raise ValueError("Number of subintervals n must be >= 1.")
        
    h = (b - a) / n
    evals = 0
    
    _, fa = engine.evaluate(a)
    _, fb = engine.evaluate(b)
    if isinstance(fa, str) or isinstance(fb, str):
        return {"Status": "Failed", "Reason": "Endpoint singularity detected."}
        
    integral = fa + fb
    evals += 2
    
    for i in range(1, n):
        _, fi = engine.evaluate(a + i * h)
        if isinstance(fi, str):
            return {"Status": "Failed", "Reason": f"Singularity detected at x = {a + i * h}"}
        integral += 2 * fi
        evals += 1
        
    integral *= h / 2.0
    
    return {
        "Status": "Success",
        "Approximation": integral,
        "Evaluations": evals,
        "h": h
    }
