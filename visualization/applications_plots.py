import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from calculus.functions.function_engine import FunctionEngine
from calculus.applications.critical_points import find_critical_points

def plot_function_analysis(engine: FunctionEngine, x_start: float, x_end: float) -> plt.Figure:
    """Plots f(x) and heavily overlays critical/inflection points."""
    x_vals = np.linspace(x_start, x_end, 1000)
    f_lambda = sp.lambdify(engine.x, engine.expression, modules=['numpy'])
    y_vals = f_lambda(x_vals)
    if np.isscalar(y_vals): y_vals = np.full_like(x_vals, y_vals)
    y_vals = np.where(np.abs(y_vals) > 500, np.nan, y_vals)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x_vals, y_vals, label='$f(x)$', color='#1f77b4', linewidth=2)
    
    # Overlay Critical Points
    crit_pts = [c for c in find_critical_points(engine) if x_start <= c <= x_end]
    for c in crit_pts:
        _, val = engine.evaluate(c)
        if isinstance(val, float):
            ax.plot(c, val, 'ro', markersize=8, label=f'Critical Point: x={c:.2f}' if c == crit_pts[0] else "")

    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.set_title("Function Analysis (Critical Points)", fontsize=14)
    ax.legend()
    return fig
