from typing import Dict, List, Union
from calculus.functions.function_engine import FunctionEngine
from calculus.differentiation.derivative_engine import DerivativeEngine

def newton_raphson(engine: FunctionEngine, x0: float, tol: float = 1e-7, max_iter: int = 20) -> Dict:
    """Implements Newton's Method for finding roots: x_n+1 = x_n - f(x_n)/f'(x_n)"""
    dev_eng = DerivativeEngine(engine)
    current_x = x0
    history = []
    
    for i in range(max_iter):
        _, f_x = engine.evaluate(current_x)
        f_prime_x = dev_eng.evaluate_derivative(current_x, 1)
        
        if isinstance(f_x, str) or isinstance(f_prime_x, str):
            return {"Status": "Failed (Undefined evaluation)", "History": history}
            
        if f_prime_x == 0:
            return {"Status": "Failed (Zero derivative)", "History": history}
            
        next_x = current_x - (f_x / f_prime_x)
        error = abs(next_x - current_x)
        
        history.append({
            "n": i, "x_n": current_x, "f(x_n)": f_x, "f'(x_n)": f_prime_x, "error": error
        })
        
        if error < tol:
            return {"Status": "Converged", "Root": next_x, "Iterations": i+1, "History": history}
            
        current_x = next_x
        
    return {"Status": "Diverged (Max iterations reached)", "Root": current_x, "History": history}
