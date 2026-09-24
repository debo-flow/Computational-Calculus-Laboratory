import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

def plot_phase_portrait_with_nullclines(sys_exprs: list, vars_str: str, x_range: tuple, y_range: tuple) -> plt.Figure:
    """Plots vector field, trajectories, and f(x,y)=0, g(x,y)=0 nullclines."""
    variables = sp.symbols(vars_str)
    X, Y = np.meshgrid(np.linspace(x_range[0], x_range[1], 30),
                       np.linspace(y_range[0], y_range[1], 30))
    
    u_lam = sp.lambdify(variables, sp.sympify(sys_exprs[0]), modules=['numpy'])
    v_lam = sp.lambdify(variables, sp.sympify(sys_exprs[1]), modules=['numpy'])
    
    U, V = u_lam(X, Y), v_lam(X, Y)
    
    fig, ax = plt.subplots(figsize=(9, 7))
    # Streamlines
    ax.streamplot(X, Y, U, V, color=np.hypot(U, V), cmap='plasma', density=1.2)
    
    # Nullclines
    X_nc, Y_nc = np.meshgrid(np.linspace(x_range[0], x_range[1], 200), np.linspace(y_range[0], y_range[1], 200))
    U_nc, V_nc = u_lam(X_nc, Y_nc), v_lam(X_nc, Y_nc)
    
    ax.contour(X_nc, Y_nc, U_nc, levels=[0], colors='green', alpha=0.6, linewidths=2)
    ax.contour(X_nc, Y_nc, V_nc, levels=[0], colors='red', alpha=0.6, linewidths=2)
    ax.plot([], [], color='green', label=f'${sp.latex(sys_exprs[0])} = 0$ (x-nullcline)')
    ax.plot([], [], color='red', label=f'${sp.latex(sys_exprs[1])} = 0$ (y-nullcline)')
    
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.set_title("Phase Portrait & Nullclines")
    ax.set_xlabel(str(variables[0]))
    ax.set_ylabel(str(variables[1]))
    ax.legend()
    return fig

def plot_3d_trajectory(t_vals: np.ndarray, y_vals: np.ndarray, vars_str: str) -> plt.Figure:
    """Visualizes 3D dynamical system trajectories (e.g. Lorenz Attractor)."""
    v_names = [v.strip() for v in vars_str.split(',')]
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(y_vals[:, 0], y_vals[:, 1], y_vals[:, 2], color='teal', linewidth=1.2)
    
    ax.set_title(f"3D Phase Space Trajectory")
    if len(v_names) == 3:
        ax.set_xlabel(v_names[0])
        ax.set_ylabel(v_names[1])
        ax.set_zlabel(v_names[2])
    return fig

def plot_sensitivity_separation(t_vals: np.ndarray, separation: np.ndarray) -> plt.Figure:
    """Plots distance D(t) between two slightly perturbed trajectories."""
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.semilogy(t_vals, separation, color='crimson', linewidth=2)
    ax.set_title("Sensitivity to Initial Conditions: $D(t) = ||X_1(t) - X_2(t)||$")
    ax.set_xlabel("Time (t)")
    ax.set_ylabel("Separation Distance (Log Scale)")
    ax.grid(True, which="both", linestyle='--', alpha=0.6)
    return fig
