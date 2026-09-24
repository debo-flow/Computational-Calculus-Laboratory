import numpy as np
import sympy as sp

def compute_direction_field(eq_str: str, x_range: tuple, y_range: tuple, res: int = 20):
    """Generates normalized vector data for dy/dx = f(x,y)."""
    x, y = sp.symbols('x y')
    f_lam = sp.lambdify((x, y), sp.sympify(eq_str), modules=['numpy'])
    
    X, Y = np.meshgrid(np.linspace(*x_range, res), np.linspace(*y_range, res))
    U = np.ones_like(X)
    V = f_lam(X, Y)
    
    mag = np.hypot(U, V)
    mag[mag == 0] = 1.0
    return X, Y, U / mag, V / mag
