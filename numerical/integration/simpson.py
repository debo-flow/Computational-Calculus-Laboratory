from typing import Dict, Union
from calculus.functions.function_engine import FunctionEngine

def composite_simpson_13(engine: FunctionEngine, a: float, b: float, n: int) -> Dict[str, Union[float, str, int]]:
    """Evaluates the composite Simpson's 1/3 rule."""
    if n % 2 != 0:
        raise ValueError("Simpson's 1/3 rule mathematically requires an EVEN number of subintervals (n).")
        
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
            return {"Status": "Failed", "Reason": f"Singularity detected at interior point."}
        weight = 4 if i % 2 != 0 else 2
        integral += weight * fi
        evals += 1
        
    integral *= h / 3.0
    
    return {"Status": "Success", "Approximation": integral, "Evaluations": evals, "h": h}

def composite_simpson_38(engine: FunctionEngine, a: float, b: float, n: int) -> Dict[str, Union[float, str, int]]:
    """Evaluates the composite Simpson's 3/8 rule."""
    if n % 3 != 0:
        raise ValueError("Simpson's 3/8 rule mathematically requires n to be a multiple of 3.")
        
    h = (b - a) / n
    evals = 0
    
    _, fa = engine.evaluate(a)
    _, fb = engine.evaluate(b)
    if isinstance(fa, str) or isinstance(fb, str):
        return {"Status": "Failed", "Reason": "Endpoint singularity."}
        
    integral = fa + fb
    evals += 2
    
    for i in range(1, n):
        _, fi = engine.evaluate(a + i * h)
        if isinstance(fi, str):
            return {"Status": "Failed", "Reason": "Interior singularity."}
        weight = 2 if i % 3 == 0 else 3
        integral += weight * fi
        evals += 1
        
    integral *= 3 * h / 8.0
    
    return {"Status": "Success", "Approximation": integral, "Evaluations": evals, "h": h}

