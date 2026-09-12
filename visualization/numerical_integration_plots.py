import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from typing import List, Tuple
from calculus.functions.function_engine import FunctionEngine

def plot_adaptive_subdivisions(engine: FunctionEngine, a: float, b: float, subdivisions: List[Tuple[float, float]]) -> plt.Figure:
    """Highlights regions where adaptive quadrature required dense refinement."""
    x_vals = np.linspace(a, b, 1000)
    f_lam = sp.lambdify(engine.x, engine.expression, modules=['numpy'])
    y_vals = f_lam(x_vals)
    if np.isscalar(y_vals): y_vals = np.full_like(x_vals, y_vals)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x_vals, y_vals, color='#1f77b4', linewidth=2, label='Integrand f(x)')
    
    # Draw vertical lines for subdivisions
    unique_points = set([p[0] for p in subdivisions] + [p[1] for p in subdivisions])
    for p in unique_points:
        ax.axvline(p, color='red', linestyle='-', alpha=0.3)
        
    ax.axhline(0, color='black', linewidth=1)
    ax.set_title(f"Adaptive Simpson Quadrature Mesh ({len(unique_points)} evaluation nodes)", fontsize=13)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend(["f(x)", "Adaptive Mesh Boundaries"])
    return fig

def plot_cumulative_integral(cum_data: dict) -> plt.Figure:
    """Plots original f(x) against the numerically constructed F(x)."""
    fig, ax1 = plt.subplots(figsize=(9, 5))
    
    color1 = 'tab:blue'
    ax1.set_xlabel('x')
    ax1.set_ylabel('Original f(x)', color=color1)
    ax1.plot(cum_data["x"], cum_data["f(x)"], color=color1, label='f(x)')
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.axhline(0, color='black', linewidth=1)
    
    ax2 = ax1.twinx()  
    color2 = 'tab:green'
    ax2.set_ylabel('Cumulative F(x)', color=color2)
    ax2.plot(cum_data["x"], cum_data["F(x)"], color=color2, linestyle='--', linewidth=2, label='F(x) = ∫f(t)dt')
    ax2.tick_params(axis='y', labelcolor=color2)
    
    fig.tight_layout()
    plt.title("Cumulative Numerical Integration (FTC Demonstration)")
    return fig
