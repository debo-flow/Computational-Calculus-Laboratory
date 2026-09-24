import sympy as sp
import numpy as np

def compute_phase_data(sys_exprs: list, vars_str: str, x_range: tuple, y_range: tuple, res: int = 20):
    """Generates U, V vector grids and Nullcline contour fields."""
    variables = sp.symbols(vars_str)
    X, Y = np.meshgrid(np.linspace(x_range[0], x_range[1], res),
                       np.linspace(y_range[0], y_range[1], res))
                       
    u_lam = sp.lambdify(variables, sp.sympify(sys_exprs[0]), modules=['numpy'])
    v_lam = sp.lambdify(variables, sp.sympify(sys_exprs[1]), modules=['numpy'])
    
    U, V = u_lam(X, Y), v_lam(X, Y)
    
    # Nullcline high-res grids
    X_nc, Y_nc = np.meshgrid(np.linspace(x_range[0], x_range[1], 150),
                             np.linspace(y_range[0], y_range[1], 150))
    U_nc, V_nc = u_lam(X_nc, Y_nc), v_lam(X_nc, Y_nc)
    
    return X, Y, U, V, X_nc, Y_nc, U_nc, V_nc
