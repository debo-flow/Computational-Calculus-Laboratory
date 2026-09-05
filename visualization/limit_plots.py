import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from calculus.functions.function_engine import FunctionEngine

def plot_limit(engine: FunctionEngine, limit_point: float, span: float = 5.0, num_points: int = 1000) -> plt.Figure:
    """
    Visualizes a limit, including the approaching paths and target limit point.
    """
    x_start = limit_point - span
    x_end = limit_point + span
    x_vals = np.linspace(x_start, x_end, num_points)
    
    # Remove exact limit point to prevent division by zero in numpy
    x_vals = x_vals[np.abs(x_vals - limit_point) > 1e-7]
    
    f_lambda = sp.lambdify(engine.x, engine.expression, modules=['numpy'])
    y_vals = f_lambda(x_vals)
    if np.isscalar(y_vals):
        y_vals = np.full_like(x_vals, y_vals)
        
    # Mask large values to prevent vertical connecting lines across asymptotes
    y_vals = np.where(np.abs(y_vals) > 1000, np.nan, y_vals)

    fig, ax = plt.subplots(figsize=(9, 6))
    ax.plot(x_vals, y_vals, label=f'$f(x)$', color='#1f77b4', linewidth=2)
    
    # Limit point vertical guide
    ax.axvline(limit_point, color='red', linestyle='--', alpha=0.5, label=f'Limit approaching x={limit_point}')
    
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.grid(True, linestyle='--', alpha=0.7)
    
    ax.set_title("Limit Visualization", fontsize=14)
    ax.set_xlabel("x", fontsize=12)
    ax.set_ylabel("f(x)", fontsize=12)
    ax.legend()
    
    return fig
