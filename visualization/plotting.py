import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from calculus.functions.function_engine import FunctionEngine

def plot_function(engine: FunctionEngine, x_start: float, x_end: float, num_points: int = 1000) -> plt.Figure:
    """
    Generates a 2D plot for the given FunctionEngine.
    """
    if x_start >= x_end:
        raise ValueError("x_start must be less than x_end.")

    # Create x values
    x_vals = np.linspace(x_start, x_end, num_points)
    
    # Fast evaluation using lambdify
    f_lambda = sp.lambdify(engine.x, engine.expression, modules=['numpy'])
    
    try:
        y_vals = f_lambda(x_vals)
        # Handle constants (lambdify returns a scalar instead of an array)
        if np.isscalar(y_vals):
            y_vals = np.full_like(x_vals, y_vals)
    except Exception as e:
        raise ValueError(f"Failed to generate plot data: {str(e)}")

    # Mask extremely large values to prevent ugly asymptote connecting lines
    y_vals = np.where(np.abs(y_vals) > 1000, np.nan, y_vals)

    # Plotting setup
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x_vals, y_vals, label=f'$f(x) = {sp.latex(engine.expression)}$', color='#1f77b4', linewidth=2)
    
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.grid(True, linestyle='--', alpha=0.7)
    
    ax.set_title("Function Plot", fontsize=14)
    ax.set_xlabel("x", fontsize=12)
    ax.set_ylabel("f(x)", fontsize=12)
    ax.legend()
    
    return fig

