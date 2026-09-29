import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def plot_extremal_comparison(x_vals: np.ndarray, y_num: np.ndarray, sym_expr: sp.Expr = None, a: float = 0, b: float = 1) -> plt.Figure:
    """Plots the numerically optimized extremal against the symbolic analytical candidate."""
    fig, ax = plt.subplots(figsize=(9, 5))
    
    ax.plot(x_vals, y_num, label="Numerical Extremal (Discretized)", color='crimson', linewidth=2.5, linestyle='--')
    
    if sym_expr is not None:
        x = sp.Symbol('x')
        f_lam = sp.lambdify(x, sym_expr, modules=['numpy'])
        y_sym = f_lam(x_vals)
        if np.isscalar(y_sym): y_sym = np.full_like(x_vals, y_sym)
        ax.plot(x_vals, y_sym, label="Symbolic Euler-Lagrange Extremal", color='blue', linewidth=1.5, alpha=0.8)
        
    ax.scatter([x_vals[0], x_vals[-1]], [y_num[0], y_num[-1]], color='black', zorder=5, label="Fixed Boundaries")
    
    ax.set_title("Calculus of Variations: Extremal Functions")
    ax.set_xlabel("x")
    ax.set_ylabel("y(x)")
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend()
    return fig

def plot_el_residual(x_vals: np.ndarray, residuals: np.ndarray) -> plt.Figure:
    """Plots R(x) to verify if the numerical solution truly satisfies EL locally."""
    fig, ax = plt.subplots(figsize=(9, 3))
    ax.plot(x_vals, residuals, color='purple')
    ax.axhline(0, color='black', linestyle='--')
    ax.set_title("Euler-Lagrange Residual $R(x)$ over Domain")
    ax.set_xlabel("x")
    ax.set_ylabel("Residual Error")
    ax.grid(True, linestyle='--', alpha=0.5)
    return fig
