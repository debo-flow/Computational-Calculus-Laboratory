import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from calculus.differential_equations.systems import create_numerical_system
from calculus.differential_equations.equilibrium import find_equilibria

def plot_slope_field(eq_str: str, x_range: tuple, y_range: tuple, resolution: int = 20) -> plt.Figure:
    """Plots normalized direction field for dy/dx = f(x,y)."""
    x, y = sp.symbols('x y')
    f_expr = sp.sympify(eq_str)
    f_lam = sp.lambdify((x, y), f_expr, modules=['numpy'])
    
    X, Y = np.meshgrid(np.linspace(x_range[0], x_range[1], resolution),
                       np.linspace(y_range[0], y_range[1], resolution))
    
    U = np.ones_like(X)
    V = f_lam(X, Y)
    
    # Normalize to plot direction (slope) rather than magnitude
    mag = np.hypot(U, V)
    mag[mag == 0] = 1
    U, V = U / mag, V / mag
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.quiver(X, Y, U, V, color='teal', pivot='mid', alpha=0.6)
    ax.set_title("Direction/Slope Field")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, linestyle='--', alpha=0.5)
    return fig

def plot_phase_portrait(sys_exprs: list, vars_str: str, x_range: tuple, y_range: tuple) -> plt.Figure:
    """Plots trajectories and nullclines for a 2D autonomous system."""
    variables = sp.symbols(vars_str)
    X_grid, Y_grid = np.meshgrid(np.linspace(x_range[0], x_range[1], 30),
                                 np.linspace(y_range[0], y_range[1], 30))
    
    u_lam = sp.lambdify(variables, sp.sympify(sys_exprs[0]), modules=['numpy'])
    v_lam = sp.lambdify(variables, sp.sympify(sys_exprs[1]), modules=['numpy'])
    
    U = u_lam(X_grid, Y_grid)
    V = v_lam(X_grid, Y_grid)
    
    fig, ax = plt.subplots(figsize=(9, 7))
    ax.streamplot(X_grid, Y_grid, U, V, color=np.hypot(U, V), cmap='plasma', density=1.2)
    
    # Plot Equilibria
    equilibria = find_equilibria(sys_exprs, vars_str)
    for eq in equilibria:
        if x_range[0] <= eq[0] <= x_range[1] and y_range[0] <= eq[1] <= y_range[1]:
            ax.plot(eq[0], eq[1], 'ro', markersize=8, label="Equilibrium Point" if eq == equilibria[0] else "")
            
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.set_title("Phase Portrait & Trajectories")
    ax.set_xlabel(str(variables[0]))
    ax.set_ylabel(str(variables[1]))
    if equilibria: ax.legend()
    return fig

def plot_solution_comparison(x_vals, y_arrays: dict, exact_y=None) -> plt.Figure:
    """Compares different numerical solvers."""
    fig, ax = plt.subplots(figsize=(10, 5))
    
    colors = ['blue', 'orange', 'green', 'red']
    for idx, (method, y_val) in enumerate(y_arrays.items()):
        ax.plot(x_vals, y_val[:, 0], label=f"{method}", linestyle='--', color=colors[idx % len(colors)])
        
    if exact_y is not None:
        ax.plot(x_vals, exact_y, label="Exact Analytical", color='black', linewidth=2)
        
    ax.set_title("Numerical Solver Comparison")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()
    return fig
