import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

def plot_2d_vector_field(P_expr: str, Q_expr: str, x_range: tuple, y_range: tuple, density: int = 15) -> plt.Figure:
    x_vals = np.linspace(x_range[0], x_range[1], density)
    y_vals = np.linspace(y_range[0], y_range[1], density)
    X, Y = np.meshgrid(x_vals, y_vals)
    
    x, y = sp.symbols('x y')
    P_lam = sp.lambdify((x, y), sp.sympify(P_expr), modules=['numpy'])
    Q_lam = sp.lambdify((x, y), sp.sympify(Q_expr), modules=['numpy'])
    
    U, V = P_lam(X, Y), Q_lam(X, Y)
    
    # Normalize for better quiver visualization
    mag = np.hypot(U, V)
    mag[mag == 0] = 1 # Prevent division by zero
    U_norm, V_norm = U / mag, V / mag
    
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.quiver(X, Y, U_norm, V_norm, mag, cmap='viridis', pivot='mid')
    ax.set_title("2D Vector Field Map (Magnitude defines color)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, linestyle='--', alpha=0.5)
    return fig

def plot_parametric_curve_3d(x_expr: str, y_expr: str, z_expr: str, t_range: tuple) -> plt.Figure:
    t_vals = np.linspace(t_range[0], t_range[1], 500)
    t = sp.Symbol('t')
    
    x_lam = sp.lambdify(t, sp.sympify(x_expr), modules=['numpy'])
    y_lam = sp.lambdify(t, sp.sympify(y_expr), modules=['numpy'])
    z_lam = sp.lambdify(t, sp.sympify(z_expr), modules=['numpy'])
    
    X = x_lam(t_vals)
    Y = y_lam(t_vals)
    Z = z_lam(t_vals)
    
    if np.isscalar(X): X = np.full_like(t_vals, X)
    if np.isscalar(Y): Y = np.full_like(t_vals, Y)
    if np.isscalar(Z): Z = np.full_like(t_vals, Z)

    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(X, Y, Z, color='red', linewidth=2, label="Parametric Curve $r(t)$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.legend()
    return fig
