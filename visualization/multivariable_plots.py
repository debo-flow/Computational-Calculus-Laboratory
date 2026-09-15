import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp
from calculus.multivariable.multivariable_engine import MultivariableEngine

def plot_3d_surface(engine: MultivariableEngine, x_range: tuple, y_range: tuple, res: int = 50) -> plt.Figure:
    x_vals = np.linspace(x_range[0], x_range[1], res)
    y_vals = np.linspace(y_range[0], y_range[1], res)
    X, Y = np.meshgrid(x_vals, y_vals)
    
    f_lam = sp.lambdify(engine.vars, engine.expression, modules=['numpy'])
    Z = f_lam(X, Y)
    
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.9)
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
    
    ax.set_title(f"Surface Plot: $z = {sp.latex(engine.expression)}$")
    ax.set_xlabel(str(engine.vars[0]))
    ax.set_ylabel(str(engine.vars[1]))
    ax.set_zlabel("z")
    return fig

def plot_contours_and_gradients(engine: MultivariableEngine, x_range: tuple, y_range: tuple, res: int = 30) -> plt.Figure:
    x_vals = np.linspace(x_range[0], x_range[1], res)
    y_vals = np.linspace(y_range[0], y_range[1], res)
    X, Y = np.meshgrid(x_vals, y_vals)
    
    f_lam = sp.lambdify(engine.vars, engine.expression, modules=['numpy'])
    Z = f_lam(X, Y)
    
    fx = sp.diff(engine.expression, engine.vars[0])
    fy = sp.diff(engine.expression, engine.vars[1])
    fx_lam = sp.lambdify(engine.vars, fx, modules=['numpy'])
    fy_lam = sp.lambdify(engine.vars, fy, modules=['numpy'])
    
    # Quiver grid (less dense than surface)
    xq_vals = np.linspace(x_range[0], x_range[1], 15)
    yq_vals = np.linspace(y_range[0], y_range[1], 15)
    XQ, YQ = np.meshgrid(xq_vals, yq_vals)
    U = fx_lam(XQ, YQ)
    V = fy_lam(XQ, YQ)
    
    fig, ax = plt.subplots(figsize=(8, 6))
    contour = ax.contourf(X, Y, Z, levels=20, cmap='viridis', alpha=0.8)
    fig.colorbar(contour, ax=ax)
    ax.quiver(XQ, YQ, U, V, color='white', alpha=0.8, scale_units='xy')
    
    ax.set_title("Level Curves & Gradient Vector Field")
    ax.set_xlabel(str(engine.vars[0]))
    ax.set_ylabel(str(engine.vars[1]))
    return fig
