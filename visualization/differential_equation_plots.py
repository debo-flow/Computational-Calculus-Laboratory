import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from visualization.ode_plots import plot_slope_field, plot_phase_portrait, plot_solution_comparison

def plot_sensitivity(t_vals: np.ndarray, y1: np.ndarray, y2: np.ndarray) -> plt.Figure:
    """Plots the trajectory separation ||X1(t) - X2(t)|| over time to detect chaotic divergence."""
    separation = np.linalg.norm(y1 - y2, axis=1)
    
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.semilogy(t_vals, separation, color='crimson', linewidth=2, label="$||X_1(t) - X_2(t)||$")
    ax.set_title("Sensitive Dependence on Initial Conditions (Trajectory Separation)")
    ax.set_xlabel("Time (t)")
    ax.set_ylabel("Distance (Log Scale)")
    ax.grid(True, which="both", linestyle='--', alpha=0.5)
    ax.legend()
    return fig

def plot_energy_variation(t_vals: np.ndarray, y_vals: np.ndarray, energy_str: str, vars_str: str) -> plt.Figure:
    """Plots E(t) = T + V over time to visualize energy conservation/dissipation."""
    variables = sp.symbols(vars_str)
    E_lam = sp.lambdify(variables, sp.sympify(energy_str), modules=['numpy'])
    
    # Evaluate energy at each time step
    E_vals = [E_lam(*state) for state in y_vals]
    
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(t_vals, E_vals, color='purple', linewidth=2, label="Total Energy $E(t)$")
    ax.set_title("Energy Variation Analysis")
    ax.set_xlabel("Time (t)")
    ax.set_ylabel("Energy")
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()
    return fig
