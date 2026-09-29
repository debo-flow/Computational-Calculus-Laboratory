import time
import sympy as sp
import numpy as np
from typing import Callable, Dict

def benchmark_execution(func: Callable, *args, iterations: int = 10, **kwargs) -> Dict:
    """Measures execution time and basic computational scaling."""
    times = []
    
    for _ in range(iterations):
        t0 = time.perf_counter()
        res = func(*args, **kwargs)
        t1 = time.perf_counter()
        times.append(t1 - t0)
        
    return {
        "Algorithm": func.__name__,
        "Iterations": iterations,
        "Mean Runtime (s)": np.mean(times),
        "Min Runtime (s)": np.min(times),
        "Max Runtime (s)": np.max(times)
    }

def scaling_test_polynomial_derivative(max_degree: int = 100) -> list:
    """Tests SymPy differentiation scaling as polynomial degree increases."""
    x = sp.Symbol('x')
    results = []
    
    for deg in range(10, max_degree + 1, 10):
        poly = sum(x**i for i in range(deg))
        
        t0 = time.perf_counter()
        sp.diff(poly, x)
        t1 = time.perf_counter()
        
        results.append({"Degree": deg, "Runtime (s)": t1 - t0})
        
    return results
