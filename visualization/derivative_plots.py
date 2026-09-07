import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from calculus.functions.function_engine import FunctionEngine
from calculus.differentiation.derivative_engine import DerivativeEngine

def plot_derivatives(engine: FunctionEngine, x_start: float, x_end: float, orders: list = [0, 1]) -> plt.Figure:
    """Plots f(x), f'(x), and f''(x) based on orders requested (0 is f(x))."""
    x_vals = np.linspace(x_start, x_end, 1000)
    fig, ax = plt.subplots(figsize=(9, 5))
    
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
    labels = ['$f(x)$', "$f'(x)$", "$f''(x)$"]
    
    dev_eng = DerivativeEngine(engine)
    
    for idx, order in enumerate(orders):
        expr = engine.expression if order == 0 else dev_eng.get_derivative(order)
        f_lambda = sp.lambdify(engine.x, expr, modules=['numpy'])
        y_vals = f_lambda(x_vals)
        if np.isscalar(y_vals):
            y_vals = np.full_like(x_vals, y_vals)
        y_vals = np.where(np.abs(y_vals) > 500, np.nan, y_vals)
        ax.plot(x_vals, y_vals, label=labels[order], color=colors[order], linewidth=2)

    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.set_title("Function and Derivatives", fontsize=14)
    ax.legend()
    return fig

def plot_tangent_secant(engine: FunctionEngine, a: float, h: float, span: float = 3.0) -> plt.Figure:
    """Plots the function, the tangent line at a, and the secant line from a to a+h."""
    x_vals = np.linspace(a - span, a + span, 500)
    f_lambda = sp.lambdify(engine.x, engine.expression, modules=['numpy'])
    y_vals = f_lambda(x_vals)
    
    f_a = f_lambda(a)
    f_ah = f_lambda(a + h)
    
    dev_eng = DerivativeEngine(engine)
    f_prime_a = dev_eng.evaluate_derivative(a)
    
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(x_vals, y_vals, label='$f(x)$', color='#1f77b4', linewidth=2)
    
    if isinstance(f_prime_a, float):
        # Tangent line: y = f(a) + f'(a)*(x - a)
        tangent_y = f_a + f_prime_a * (x_vals - a)
        ax.plot(x_vals, tangent_y, '--', color='green', label='Tangent Line')
        
    if h != 0:
        # Secant line: y = f(a) + m*(x - a)
        m_sec = (f_ah - f_a) / h
        secant_y = f_a + m_sec * (x_vals - a)
        ax.plot(x_vals, secant_y, '-.', color='red', label='Secant Line')
        ax.plot([a, a+h], [f_a, f_ah], 'ro') # Points

    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.set_title(f"Derivative as a Limit (Tangent vs Secant, h={h})", fontsize=14)
    ax.legend()
    
    # Set reasonable y limits based on the function local region
    if isinstance(f_a, (int, float)):
        ax.set_ylim(f_a - span*2, f_a + span*2)
        
    return fig
