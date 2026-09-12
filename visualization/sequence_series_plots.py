import numpy as np
import matplotlib.pyplot as plt
from typing import List, Dict

def plot_sequence_and_series(data: List[Dict]) -> plt.Figure:
    """Plots the discrete sequence terms (a_n) and partial sums (S_n)."""
    n_vals = [d["n"] for d in data]
    a_vals = [d["a_n"] for d in data]
    s_vals = [d["S_n (Partial Sum)"] for d in data]

    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Discrete points for sequence
    ax.scatter(n_vals, a_vals, color='blue', label='$a_n$ (Sequence Terms)', zorder=3)
    
    # Step plot for partial sums
    ax.step(n_vals, s_vals, where='mid', color='red', label='$S_n$ (Partial Sums)', linewidth=2, alpha=0.7)
    
    ax.axhline(0, color='black', linewidth=1)
    ax.set_title("Sequence Terms vs Series Partial Sums", fontsize=14)
    ax.set_xlabel("Index (n)", fontsize=12)
    ax.set_ylabel("Value", fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()
    
    return fig
