import numpy as np
import matplotlib.pyplot as plt

def plot_cubic_spline(x_data: list, y_data: list, x_eval: list, y_eval: list) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.scatter(x_data, y_data, color='red', zorder=5, label='Discrete Data Nodes')
    ax.plot(x_eval, y_eval, color='blue', label='Cubic Spline Interpolation')
    ax.set_title("Interpolation: Natural Cubic Spline")
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()
    return fig

def plot_pde_evolution(x_grid: list, u_history: list) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(9, 5))
    
    # Plot initial, mid, and final states
    ax.plot(x_grid, u_history[0], label='t=0 (Initial Condition)', linestyle='--')
    mid_idx = len(u_history) // 2
    ax.plot(x_grid, u_history[mid_idx], label=f't=mid', alpha=0.7)
    ax.plot(x_grid, u_history[-1], label='t=final', color='red', linewidth=2)
    
    ax.set_title("1D Heat Equation: FTCS Time Evolution")
    ax.set_xlabel("Domain (x)")
    ax.set_ylabel("u(x,t)")
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()
    return fig
