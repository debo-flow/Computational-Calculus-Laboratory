import sympy as sp
import numpy as np
from typing import Dict, Any

def analyze_matrix_system(A_matrix: list) -> Dict[str, Any]:
    """Analyzes X' = AX linear systems and their stability."""
    A = sp.Matrix(A_matrix)
    eigenvals = A.eigenvals()
    eigenvects = A.eigenvects()
    
    det = A.det()
    trace = A.trace()
    
    stability = "Unclassified / Mixed"
    if A.shape == (2, 2):
        disc = trace**2 - 4*det
        if det < 0: stability = "Saddle (Unstable)"
        elif det > 0:
            if trace < 0: stability = "Stable Node" if disc >= 0 else "Stable Spiral"
            elif trace > 0: stability = "Unstable Node" if disc >= 0 else "Unstable Spiral"
            else: stability = "Center (Marginally Stable)"
        else:
            stability = "Degenerate (Zero Determinant)"
            
    return {
        "Matrix A": A,
        "Trace": trace,
        "Determinant": det,
        "Eigenvalues": list(eigenvals.keys()),
        "Eigenvectors": eigenvects,
        "Classification": stability
    }
    
def convert_second_order_to_system(eq_str: str) -> dict:
    x = sp.Symbol('x')
    y = sp.Function('y')(x)
    f_expr = sp.sympify(eq_str)
    u1, u2 = sp.symbols('u1 u2')
    f_sys = f_expr.subs({y.diff(x): u2, y: u1})
    return {"u1'": u2, "u2'": f_sys}

def create_numerical_system(exprs: list, vars_str: str):
    variables = sp.symbols(vars_str)
    t = sp.Symbol('t')
    lambdified = [sp.lambdify((t, *variables), sp.sympify(e), modules=['numpy']) for e in exprs]
    def f(t_val, Y_val): return np.array([func(t_val, *Y_val) for func in lambdified])
    return f
