import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from calculus.differential_equations.phase_portraits import compute_phase_data

def plot_direction_field(eq_str: str, x_range: tuple, y_range: tuple, res: int = 20) -> plt.Figure:
    """Plots normalized slope field for dy/dx = f(x,y)."""
    x, y = sp.symbols('x y')
    f_lam = sp.lambdify((x, y), sp.sympify(eq_str), modules=['numpy'])
    
    X, Y = np.meshgrid(np.linspace(x_range[0], x_range[1], res),
                       np.linspace(y_range[0], y_range[1], res))
    
    U = np.ones_like(X)
    V = f_lam(X, Y)
    
    mag = np.hypot(U, V)
    mag[mag == 0] = 1 # Safety
    U, V = U / mag, V / mag
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.quiver(X, Y, U, V, color='teal', pivot='mid', alpha=0.6)
    ax.set_title("Direction Field: $\\frac{dy}{dx} = f(x,y)$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, linestyle='--', alpha=0.5)
    return fig

def plot_solver_comparison(x_vals: np.ndarray, y_dict: dict, exact_y: np.ndarray = None) -> plt.Figure:
    """Plots multiple numerical solutions against each other or an exact reference."""
    fig, ax = plt.subplots(figsize=(10, 5))
    colors = ['blue', 'orange', 'green', 'red', 'purple']
    
    for idx, (method, y_arr) in enumerate(y_dict.items()):
        ax.plot(x_vals, y_arr[:, 0], label=method, linestyle='--', color=colors[idx % len(colors)])
        
    if exact_y is not None:
        ax.plot(x_vals, exact_y, label="Exact Analytical", color='black', linewidth=2)
        
    ax.set_title("Numerical Solver Comparison")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()
    return fig

def plot_phase_portrait_complete(sys_exprs: list, vars_str: str, x_range: tuple, y_range: tuple, equilibria: list = None) -> plt.Figure:
    """Plots Streamlines, Nullclines, and Equilibrium points dynamically."""
    X, Y, U, V, X_nc, Y_nc, U_nc, V_nc = compute_phase_data(sys_exprs, vars_str, x_range, y_range)
    variables = sp.symbols(vars_str)
    
    fig, ax = plt.subplots(figsize=(9, 7))
    ax.streamplot(X, Y, U, V, color=np.hypot(U, V), cmap='plasma', density=1.5)
    
    ax.contour(X_nc, Y_nc, U_nc, levels=[0], colors='green', alpha=0.6, linewidths=2)
    ax.contour(X_nc, Y_nc, V_nc, levels=[0], colors='red', alpha=0.6, linewidths=2)
    ax.plot([], [], color='green', label=f'${sp.latex(sp.sympify(sys_exprs[0]))} = 0$ (Nullcline 1)')
    ax.plot([], [], color='red', label=f'${sp.latex(sp.sympify(sys_exprs[1]))} = 0$ (Nullcline 2)')
    
    if equilibria:
        for eq in equilibria:
            if x_range[0] <= eq[0] <= x_range[1] and y_range[0] <= eq[1] <= y_range[1]:
                ax.plot(eq[0], eq[1], 'ko', markersize=8, markeredgecolor='white', label="Equilibrium" if eq == equilibria[0] else "")
                
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.set_title("Phase Portrait & Nullclines")
    ax.set_xlabel(str(variables[0]))
    ax.set_ylabel(str(variables[1]))
    ax.legend()
    return fig
