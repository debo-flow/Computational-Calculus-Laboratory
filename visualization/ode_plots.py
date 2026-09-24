import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from calculus.differential_equations.phase_space import compute_phase_data
from calculus.differential_equations.direction_fields import compute_direction_field

def plot_direction_field_with_trajectories(eq_str: str, x_range: tuple, y_range: tuple, trajectories: list = None) -> plt.Figure:
    """Overlays ODE numerical solutions onto normalized slope fields."""
    X, Y, U, V = compute_direction_field(eq_str, x_range, y_range)
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.quiver(X, Y, U, V, color='teal', pivot='mid', alpha=0.5)
    
    if trajectories:
        for t_x, t_y in trajectories:
            ax.plot(t_x, t_y, linewidth=2)
            
    ax.set_title("Direction Field & Solution Trajectories")
    ax.set_xlim(x_range)
    ax.set_ylim(y_range)
    ax.grid(True, linestyle='--', alpha=0.5)
    return fig

def plot_phase_portrait_complete(sys_exprs: list, vars_str: str, x_range: tuple, y_range: tuple, equilibria: list = None, trajectories: list = None) -> plt.Figure:
    """Visualizes Phase Space: Streamlines, Nullclines, Equilibria."""
    X, Y, U, V, X_nc, Y_nc, U_nc, V_nc = compute_phase_data(sys_exprs, vars_str, x_range, y_range)
    
    fig, ax = plt.subplots(figsize=(9, 7))
    ax.streamplot(X, Y, U, V, color=np.hypot(U, V), cmap='plasma', density=1.2)
    
    ax.contour(X_nc, Y_nc, U_nc, levels=[0], colors='green', alpha=0.6, linewidths=2)
    ax.contour(X_nc, Y_nc, V_nc, levels=[0], colors='red', alpha=0.6, linewidths=2)
    ax.plot([], [], color='green', label='x-Nullcline ($dx/dt=0$)')
    ax.plot([], [], color='red', label='y-Nullcline ($dy/dt=0$)')
    
    if trajectories:
        for traj in trajectories:
            ax.plot(traj[:, 0], traj[:, 1], 'w-', linewidth=1.5)
            
    if equilibria:
        for eq in equilibria:
            if x_range[0] <= eq[0] <= x_range[1] and y_range[0] <= eq[1] <= y_range[1]:
                ax.plot(eq[0], eq[1], 'ko', markersize=8, markeredgecolor='white', label="Equilibrium" if eq == equilibria[0] else "")
                
    ax.set_title("Dynamical Phase Portrait")
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.legend()
    return fig

def plot_solver_comparison(x_vals: np.ndarray, y_dict: dict, exact_y: np.ndarray = None) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(10, 5))
    colors = ['blue', 'orange', 'green', 'red', 'purple']
    for idx, (method, y_arr) in enumerate(y_dict.items()):
        ax.plot(x_vals, y_arr[:, 0], label=method, linestyle='--', color=colors[idx % len(colors)])
    if exact_y is not None:
        ax.plot(x_vals, exact_y, label="Exact", color='black', linewidth=2)
    ax.set_title("Numerical Solver Benchmark")
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()
    return fig
