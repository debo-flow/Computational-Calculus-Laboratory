import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from visualization.ode_plots import plot_slope_field, plot_phase_portrait, plot_solution_comparison

def plot_isoclines(eq_str: str, x_range: tuple, y_range: tuple, c_values: list = [-1, 0, 1]) -> plt.Figure:
    """Plots isoclines f(x,y) = c superimposed on the slope field."""
    x, y = sp.symbols('x y')
    f_expr = sp.sympify(eq_str)
    f_lam = sp.lambdify((x, y), f_expr, modules=['numpy'])
    
    # Base slope field
    fig = plot_slope_field(eq_str, x_range, y_range)
    ax = fig.gca()
    
    X, Y = np.meshgrid(np.linspace(x_range[0], x_range[1], 100),
                       np.linspace(y_range[0], y_range[1], 100))
    Z = f_lam(X, Y)
    
    contour = ax.contour(X, Y, Z, levels=c_values, colors='red', alpha=0.8, linestyles='dashed')
    ax.clabel(contour, inline=True, fontsize=10, fmt="c=%1.1f")
    
    ax.plot([], [], color='red', linestyle='dashed', label='Isoclines $f(x,y)=c$')
    ax.legend()
    ax.set_title("Slope Field with Isoclines")
    return fig

def plot_bvp_solution(x_vals: np.ndarray, y_vals: np.ndarray, title: str = "BVP Solution") -> plt.Figure:
    """Visualizes the boundary points anchored to the numerical BVP trajectory."""
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(x_vals, y_vals, color='purple', linewidth=2, label="Numerical BVP Solution")
    ax.scatter([x_vals[0], x_vals[-1]], [y_vals[0], y_vals[-1]], color='red', zorder=5, s=60, label="Boundary Conditions (Anchors)")
    ax.set_title(title)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()
    return fig
