import sympy as sp

def compute_scalar_laplacian(expr_str: str, vars_str: str = "x, y, z") -> sp.Expr:
    """∇²f = f_xx + f_yy + f_zz"""
    expr = sp.sympify(expr_str.replace('^', '**'))
    vars = sp.symbols(vars_str)
    laplacian = sum(sp.diff(expr, v, 2) for v in vars)
    return sp.simplify(laplacian)
