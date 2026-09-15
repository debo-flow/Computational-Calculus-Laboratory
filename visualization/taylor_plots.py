import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from calculus.taylor.taylor_engine import TaylorEngine

def plot_taylor_approximation(t_engine: TaylorEngine, order: int, x_span: float = 5.0) -> plt.Figure:
    """Plots f(x) alongside T_n(x) to visualize convergence."""
    x_vals = np.linspace(t_engine.a - x_span, t_engine.a + x_span, 1000)
    
    # Original Function
    f_lam = sp.lambdify(t_engine.engine.x, t_engine.engine.expression, modules=['numpy'])
    y_f = f_lam(x_vals)
    if np.isscalar(y_f): y_f = np.full_like(x_vals, y_f)
    y_f = np.where(np.abs(y_f) > 100, np.nan, y_f)
    
    # Taylor Polynomial
    T_n = t_engine.get_polynomial(order)
    t_lam = sp.lambdify(t_engine.engine.x, T_n, modules=['numpy'])
    y_t = t_lam(x_vals)
    if np.isscalar(y_t): y_t = np.full_like(x_vals, y_t)
    y_t = np.where(np.abs(y_t) > 100, np.nan, y_t)
    
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(x_vals, y_f, label='$f(x)$', color='black', linewidth=2)
    ax.plot(x_vals, y_t, label=f'$T_{{{order}}}(x)$', color='orange', linestyle='--', linewidth=2)
    
    # Expansion point
    f_a = f_lam(t_engine.a)
    ax.scatter([t_engine.a], [f_a], color='red', zorder=5, label=f'Expansion Point a={t_engine.a}')
    
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_ylim(-10, 10) # Bounded for clarity on polynomials
    ax.set_title(f"Taylor Polynomial Approximation (Order {order})", fontsize=13)
    ax.legend()
    
    return fig

def plot_taylor_error_map(t_engine: TaylorEngine, orders: list, x_span: float = 3.0) -> plt.Figure:
    """Plots E_n(x) = |f(x) - T_n(x)| on a log scale."""
    x_vals = np.linspace(t_engine.a - x_span, t_engine.a + x_span, 500)
    f_lam = sp.lambdify(t_engine.engine.x, t_engine.engine.expression, modules=['numpy'])
    y_f = f_lam(x_vals)
    
    fig, ax = plt.subplots(figsize=(9, 5))
    
    for n in orders:
        T_n = t_engine.get_polynomial(n)
        t_lam = sp.lambdify(t_engine.engine.x, T_n, modules=['numpy'])
        y_t = t_lam(x_vals)
        error = np.abs(y_f - y_t)
        
        # Clip error to avoid log(0) issues
        error = np.clip(error, 1e-15, None)
        ax.semilogy(x_vals, error, label=f'Order {n} Error')
        
    ax.axvline(t_engine.a, color='red', linestyle='--', alpha=0.5, label='Expansion Point')
    ax.set_title("Taylor Approximation Error Map: $|f(x) - T_n(x)|$", fontsize=13)
    ax.set_ylabel("Absolute Error (Log Scale)")
    ax.set_xlabel("x")
    ax.grid(True, which="both", linestyle='--', alpha=0.5)
    ax.legend()
    return fig

