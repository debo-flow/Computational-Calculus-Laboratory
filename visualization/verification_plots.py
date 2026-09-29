import matplotlib.pyplot as plt
import numpy as np

def plot_error_scaling(step_sizes: list, errors: list, theoretical_order: int = None) -> plt.Figure:
    """Log-Log plot demonstrating empirical numerical convergence rates."""
    fig, ax = plt.subplots(figsize=(8, 5))
    
    ax.loglog(step_sizes, errors, marker='o', color='blue', label='Observed Error')
    
    if theoretical_order and len(step_sizes) > 1:
        # Plot reference slope
        ref_h = np.array(step_sizes)
        ref_err = errors[0] * (ref_h / ref_h[0])**theoretical_order
        ax.loglog(ref_h, ref_err, linestyle='--', color='gray', label=f'O(h^{theoretical_order}) Theoretical')
        
    ax.set_title("Numerical Convergence Scaling (Log-Log)")
    ax.set_xlabel("Step Size (h)")
    ax.set_ylabel("Absolute Error")
    ax.grid(True, which="both", linestyle='--', alpha=0.5)
    ax.legend()
    
    return fig

def plot_benchmark_scaling(scaling_data: list, x_key: str = "Degree", y_key: str = "Runtime (s)") -> plt.Figure:
    """Plots computational scaling benchmarks."""
    x_vals = [d[x_key] for d in scaling_data]
    y_vals = [d[y_key] for d in scaling_data]
    
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x_vals, y_vals, marker='s', color='purple', linewidth=2)
    ax.set_title(f"Computational Scaling: {y_key} vs {x_key}")
    ax.set_xlabel(x_key)
    ax.set_ylabel(y_key)
    ax.grid(True, linestyle='--', alpha=0.6)
    
    return fig
