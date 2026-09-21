import sympy as sp
import numpy as np

def convert_second_order_to_system(eq_str: str) -> dict:
    """Converts y'' = f(x, y, y') into u_1' = u_2, u_2' = f(x, u_1, u_2)"""
    x = sp.Symbol('x')
    y = sp.Function('y')(x)
    
    # Assume eq is given as "f(x, y, y')" equating to y''
    f_expr = sp.sympify(eq_str)
    
    u1, u2 = sp.symbols('u1 u2')
    f_sys = f_expr.subs({y.diff(x): u2, y: u1})
    
    return {
        "u1'": u2,
        "u2'": f_sys,
        "Vector Field": [u2, f_sys],
        "Interpretation": "y -> u1, y' -> u2"
    }

def create_numerical_system(exprs: list, vars_str: str):
    """Creates a callable f(t, Y) for NumPy/SciPy solvers."""
    variables = sp.symbols(vars_str)
    t = sp.Symbol('t')
    lambdified = [sp.lambdify((t, *variables), sp.sympify(e), modules=['numpy']) for e in exprs]
    
    def f(t_val, Y_val):
        return np.array([func(t_val, *Y_val) for func in lambdified])
    return f
