import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from calculus.multivariable.multivariable_engine import MultivariableEngine

def plot_double_integral_region(x_bnds: tuple, y_bnds: tuple) -> plt.Figure:
    """Visualizes a 2D rectangular integration domain."""
    fig, ax = plt.subplots(figsize=(6, 6))
    
    x = [x_bnds[0], x_bnds[1], x_bnds[1], x_bnds[0], x_bnds[0]]
    y = [y_bnds[0], y_bnds[0], y_bnds[1], y_bnds[1], y_bnds[0]]
    
    ax.fill(x, y, color='purple', alpha=0.3, label='Integration Region $D$')
    ax.plot(x, y, color='black', linewidth=2)
    
    ax.set_title("Integration Region $D$ in xy-plane")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()
    return fig

def plot_monte_carlo_samples(engine: MultivariableEngine, x_bnds: tuple, y_bnds: tuple, mc_data: dict) -> plt.Figure:
    """Plots random Monte Carlo sampling points over the domain."""
    fig, ax = plt.subplots(figsize=(7, 6))
    
    # Plot Region
    x = [x_bnds[0], x_bnds[1], x_bnds[1], x_bnds[0], x_bnds[0]]
    y = [y_bnds[0], y_bnds[0], y_bnds[1], y_bnds[1], y_bnds[0]]
    ax.plot(x, y, color='black', linewidth=2)
    
    # Plot Samples
    xs = mc_data["x_samples"]
    ys = mc_data["y_samples"]
    
    f_lam = sp.lambdify(engine.vars, engine.expression, modules=['numpy'])
    zs = f_lam(xs, ys)
    
    scatter = ax.scatter(xs, ys, c=zs, cmap='viridis', alpha=0.6, s=10)
    fig.colorbar(scatter, ax=ax, label='$f(x,y)$ Value')
    
    ax.set_title(f"Monte Carlo Uniform Sampling (Showing 1000 points)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, linestyle='--', alpha=0.6)
    return fig
