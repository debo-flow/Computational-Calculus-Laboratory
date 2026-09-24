import sympy as sp
import numpy as np

def compute_nullclines(sys_exprs: list, vars_str: str, x_range: tuple, y_range: tuple, res: int = 100):
    """Evaluates f(x,y)=0 and g(x,y)=0 over a grid for plotting nullclines."""
    variables = sp.symbols(vars_str)
    if len(variables) != 2:
        raise ValueError("Nullclines strictly supported for 2D systems.")
        
    X, Y = np.meshgrid(np.linspace(x_range[0], x_range[1], res),
                       np.linspace(y_range[0], y_range[1], res))
                       
    f_lam = sp.lambdify(variables, sp.sympify(sys_exprs[0]), modules=['numpy'])
    g_lam = sp.lambdify(variables, sp.sympify(sys_exprs[1]), modules=['numpy'])
    
    Z_f = f_lam(X, Y)
    Z_g = g_lam(X, Y)
    
    return X, Y, Z_f, Z_g
