import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from typing import List, Dict, Any
from calculus.functions.function_engine import FunctionEngine
from calculus.integration.integral_analysis import compute_riemann_sum

def plot_definite_integral_area(engine: FunctionEngine, a: float, b: float, num_points: int = 600) -> plt.Figure:
    """
    Plots f(x) and shades signed area (green for f(x) >= 0, red for f(x) < 0).
    """
    span = max(abs(b - a), 2.0)
    x_min, x_max = min(a, b) - 0.25 * span, max(a, b) + 0.25 * span
    x_vals = np.linspace(x_min, x_max, num_points)
    
    f_lambda = sp.lambdify(engine.x, engine.expression, modules=['numpy'])
    y_vals = f_lambda(x_vals)
    if np.isscalar(y_vals):
        y_vals = np.full_like(x_vals, y_vals)
    y_vals = np.where(np.abs(y_vals) > 500, np.nan, y_vals)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(x_vals, y_vals, label=f'$f(x) = {sp.latex(engine.expression)}$', color='#1f77b4', linewidth=2)

    # Shading integration interval
    x_fill = np.linspace(min(a, b), max(a, b), 400)
    y_fill = f_lambda(x_fill)
    if np.isscalar(y_fill):
        y_fill = np.full_like(x_fill, y_fill)
        
    ax.fill_between(x_fill, 0, y_fill, where=(y_fill >= 0), color='green', alpha=0.35, label='Positive Area (+)')
    ax.fill_between(x_fill, 0, y_fill, where=(y_fill < 0), color='red', alpha=0.35, label='Negative Area (-)')

    ax.axvline(a, color='black', linestyle='--', linewidth=1.2, label=f'Bound a = {a}')
    ax.axvline(b, color='black', linestyle='--', linewidth=1.2, label=f'Bound b = {b}')
    ax.axhline(0, color='black', linewidth=1)
    ax.grid(True, linestyle='--', alpha=0.6)
    
    ax.set_title("Definite Integral: Signed Area Accumulation", fontsize=13)
    ax.set_xlabel("x", fontsize=11)
    ax.set_ylabel("f(x)", fontsize=11)
    ax.legend()
    return fig

def plot_riemann_rectangles(engine: FunctionEngine, a: float, b: float, n: int, method: str = 'midpoint') -> plt.Figure:
    """
    Visualizes Riemann approximation rectangles against the continuous curve.
    """
    res = compute_riemann_sum(engine, a, b, n, method)
    dx = res["DeltaX"]
    x_evals = res["x_eval"]
    heights = res["rect_heights"]

    x_vals = np.linspace(min(a, b) - 0.5, max(a, b) + 0.5, 400)
    f_lambda = sp.lambdify(engine.x, engine.expression, modules=['numpy'])
    y_vals = f_lambda(x_vals)
    if np.isscalar(y_vals):
        y_vals = np.full_like(x_vals, y_vals)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(x_vals, y_vals, color='#1f77b4', linewidth=2, label='$f(x)$')

    # Draw rectangles
    for i in range(n):
        rect_left = a + i * dx
        ax.bar(
            rect_left, heights[i], width=dx, align='edge',
            facecolor='orange', edgecolor='black', alpha=0.45,
            label='Riemann Rectangles' if i == 0 else ""
        )

    ax.scatter(x_evals, heights, color='red', s=25, zorder=5, label='Evaluation Points')
    ax.axhline(0, color='black', linewidth=1)
    ax.grid(True, linestyle='--', alpha=0.6)
    
    ax.set_title(f"{method.capitalize()} Riemann Sum (n = {n}, Approx = {res['Approximation']:.4f})", fontsize=13)
    ax.set_xlabel("x", fontsize=11)
    ax.set_ylabel("f(x)", fontsize=11)
    ax.legend()
    return fig

def plot_area_between_curves(engine1: FunctionEngine, engine2: FunctionEngine, a: float, b: float) -> plt.Figure:
    """
    Visualizes the bounded region between two intersecting or non-intersecting curves.
    """
    x_vals = np.linspace(a - 1.0, b + 1.0, 500)
    f_lam1 = sp.lambdify(engine1.x, engine1.expression, modules=['numpy'])
    f_lam2 = sp.lambdify(engine2.x, engine2.expression, modules=['numpy'])
    
    y1 = f_lam1(x_vals)
    y2 = f_lam2(x_vals)
    if np.isscalar(y1): y1 = np.full_like(x_vals, y1)
    if np.isscalar(y2): y2 = np.full_like(x_vals, y2)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(x_vals, y1, label=f'$f(x) = {sp.latex(engine1.expression)}$', color='#1f77b4', linewidth=2)
    ax.plot(x_vals, y2, label=f'$g(x) = {sp.latex(engine2.expression)}$', color='#d62728', linewidth=2)

    x_fill = np.linspace(a, b, 400)
    y1_fill = f_lam1(x_fill)
    y2_fill = f_lam2(x_fill)
    if np.isscalar(y1_fill): y1_fill = np.full_like(x_fill, y1_fill)
    if np.isscalar(y2_fill): y2_fill = np.full_like(x_fill, y2_fill)

    ax.fill_between(x_fill, y1_fill, y2_fill, color='purple', alpha=0.35, label='Enclosed Region')
    ax.axvline(a, color='black', linestyle='--', linewidth=1.2)
    ax.axvline(b, color='black', linestyle='--', linewidth=1.2)
    ax.axhline(0, color='black', linewidth=1)
    ax.grid(True, linestyle='--', alpha=0.6)
    
    ax.set_title("Area Enclosed Between Two Curves", fontsize=13)
    ax.set_xlabel("x", fontsize=11)
    ax.set_ylabel("y", fontsize=11)
    ax.legend()
    return fig

def plot_riemann_convergence(n_values: List[int], errors: List[float]) -> plt.Figure:
    """
    Log-log error plot demonstrating algebraic convergence O(1/n) or O(1/n^2).
    """
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.loglog(n_values, errors, marker='o', color='crimson', linewidth=2, label='Midpoint Error')
    ax.set_title("Riemann Sum Convergence: Error vs Subintervals (n)", fontsize=13)
    ax.set_xlabel("Subintervals (n)", fontsize=11)
    ax.set_ylabel("Absolute Error", fontsize=11)
    ax.grid(True, which="both", linestyle='--', alpha=0.6)
    ax.legend()
    return fig
