import numpy as np
from typing import Dict, Union
from calculus.functions.function_engine import FunctionEngine

def gauss_legendre_quadrature(engine: FunctionEngine, a: float, b: float, n: int) -> Dict[str, Union[float, str, int, list]]:
    """Evaluates using n-point Gauss-Legendre Quadrature by transforming [-1, 1] to [a, b]."""
    if n < 1:
        raise ValueError("Number of nodes n must be >= 1.")
        
    # Get standard nodes (t_i) and weights (v_i) for [-1, 1]
    t_nodes, v_weights = np.polynomial.legendre.leggauss(n)
    
    integral = 0.0
    transformed_nodes = []
    
    scale = (b - a) / 2.0
    shift = (b + a) / 2.0
    
    for t, v in zip(t_nodes, v_weights):
        x_i = scale * t + shift
        transformed_nodes.append(float(x_i))
        
        _, f_xi = engine.evaluate(float(x_i))
        if isinstance(f_xi, str):
            return {"Status": "Failed", "Reason": f"Singularity at transformed node x = {x_i:.4f}"}
            
        integral += v * f_xi
        
    integral *= scale
    
    return {
        "Status": "Success",
        "Approximation": integral,
        "Evaluations": n,
        "Nodes": transformed_nodes
    }
