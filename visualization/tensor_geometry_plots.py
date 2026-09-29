import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp
from numerical.ode_solvers import solve_adaptive

def plot_surface_with_curvature(x_str: str, y_str: str, z_str: str, uv_vars: str, u_bounds: tuple, v_bounds: tuple, K_expr: sp.Expr) -> plt.Figure:
    """Plots a 3D parametrized surface, color-mapped by its scalar Gaussian Curvature K."""
    u, v = sp.symbols(uv_vars)
    u_vals = np.linspace(u_bounds[0], u_bounds[1], 40)
    v_vals = np.linspace(v_bounds[0], v_bounds[1], 40)
    U, V = np.meshgrid(u_vals, v_vals)
    
    x_lam = sp.lambdify((u, v), sp.sympify(x_str), modules=['numpy'])
    y_lam = sp.lambdify((u, v), sp.sympify(y_str), modules=['numpy'])
    z_lam = sp.lambdify((u, v), sp.sympify(z_str), modules=['numpy'])
    K_lam = sp.lambdify((u, v), K_expr, modules=['numpy'])
    
    X, Y, Z = x_lam(U, V), y_lam(U, V), z_lam(U, V)
    
    # Evaluate curvature for color mapping
    K_vals = K_lam(U, V)
    if np.isscalar(K_vals): K_vals = np.full_like(X, K_vals)
    
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    
    # Normalize curvature for colormap
    norm = plt.Normalize(np.nanmin(K_vals), np.nanmax(K_vals))
    colors = plt.cm.coolwarm(norm(K_vals))
    
    surf = ax.plot_surface(X, Y, Z, facecolors=colors, shade=False, alpha=0.9)
    m = plt.cm.ScalarMappable(cmap=plt.cm.coolwarm, norm=norm)
    m.set_array([])
    fig.colorbar(m, ax=ax, label="Gaussian Curvature (K)", shrink=0.6)
    
    ax.set_title("Surface Geometry & Intrinsic Curvature Map")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    return fig
