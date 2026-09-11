import numpy as np
import matplotlib.pyplot as plt
from typing import List, Dict
from calculus.functions.function_engine import FunctionEngine
from numerical.differentiation.derivative_approximations import apply_stencil
from numerical.differentiation.finite_difference import STENCILS

def plot_error_vs_stepsize(results: List[Dict]) -> plt.Figure:
    """Plots a log-log graph of Absolute Error vs h to show the classic 'V' shape."""
    h_vals = [r["h"] for r in results if isinstance(r["Abs Error"], float) and r["Abs Error"] > 0]
    e_vals = [r["Abs Error"] for r in results if isinstance(r["Abs Error"], float) and r["Abs Error"] > 0]
    
    fig, ax = plt.subplots(figsize=(9, 5))
    if not h_vals:
        ax.text(0.5, 0.5, "Insufficient valid data for log-log plot", ha='center')
        return fig
        
    ax.loglog(h_vals, e_vals, marker='o', linestyle='-', color='purple', label="Total Numerical Error")
    
    ax.set_title("Truncation vs. Round-off Error Analysis (Log-Log)", fontsize=14)
    ax.set_xlabel("Step size (h)", fontsize=12)
    ax.set_ylabel("Absolute Error", fontsize=12)
    ax.invert_xaxis() # Read left to right as h decreases
    ax.grid(True, which="both", ls="--", alpha=0.5)
    
    # Annotate Truncation and Round-off regions
    min_err_idx = np.argmin(e_vals)
    ax.axvline(h_vals[min_err_idx], color='red', linestyle='--', alpha=0.7, label=f"Optimal h ≈ {h_vals[min_err_idx]:.1e}")
    ax.text(h_vals[0], np.max(e_vals), "Truncation Error\nDominates", ha='left', va='top', color='blue')
    ax.text(h_vals[-1], np.max(e_vals), "Round-off (Cancellation)\nDominates", ha='right', va='top', color='red')
    
    ax.legend()
    return fig

def plot_noisy_derivative(engine: FunctionEngine, x_start: float, x_end: float, noise_magnitude: float = 0.05) -> plt.Figure:
    """Demonstrates how numerical differentiation dangerously amplifies noise."""
    x_vals = np.linspace(x_start, x_end, 100)
    h = x_vals[1] - x_vals[0]
    
    # Exact data
    f_lambda = __import__('sympy').lambdify(engine.x, engine.expression, modules=['numpy'])
    y_exact = f_lambda(x_vals)
    
    # Noisy data
    np.random.seed(42) # For reproducibility
    noise = np.random.normal(0, noise_magnitude, len(x_vals))
    y_noisy = y_exact + noise
    
    # Differentiate using numpy gradient (central difference)
    dy_exact = np.gradient(y_exact, h)
    dy_noisy = np.gradient(y_noisy, h)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    ax1.plot(x_vals, y_exact, label="Original f(x)", color="black", linewidth=2)
    ax1.scatter(x_vals, y_noisy, label="Noisy f(x)", color="red", alpha=0.5, s=10)
    ax1.set_title("Function with Noise", fontsize=12)
    ax1.grid(True, ls="--", alpha=0.5)
    ax1.legend()
    
    ax2.plot(x_vals, dy_exact, label="Exact f'(x)", color="black", linewidth=2)
    ax2.plot(x_vals, dy_noisy, label="Numerical f'(x) of Noisy Data", color="orange", alpha=0.8)
    ax2.set_title("Noise Amplification in Derivative", fontsize=12)
    ax2.grid(True, ls="--", alpha=0.5)
    ax2.legend()
    
    return fig
