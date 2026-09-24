import sympy as sp
from typing import Dict, Any

def analyze_constant_coeff_linear(a: float, b: float, c: float) -> Dict[str, Any]:
    """Analyzes ay'' + by' + cy = 0 via characteristic equation ar^2 + br + c = 0."""
    r = sp.Symbol('r')
    char_eq = a*r**2 + b*r + c
    roots = sp.solve(char_eq, r)
    
    x = sp.Symbol('x')
    C1, C2 = sp.symbols('C1 C2')
    
    if len(roots) == 1: # Repeated real root
        r1 = roots[0]
        root_type = "Repeated Real Roots"
        gen_sol = C1*sp.exp(r1*x) + C2*x*sp.exp(r1*x)
    else:
        r1, r2 = roots
        if r1.is_real and r2.is_real:
            root_type = "Distinct Real Roots"
            gen_sol = C1*sp.exp(r1*x) + C2*sp.exp(r2*x)
        else:
            root_type = "Complex Conjugate Roots"
            alpha, beta = sp.re(r1), sp.Abs(sp.im(r1))
            gen_sol = sp.exp(alpha*x) * (C1*sp.cos(beta*x) + C2*sp.sin(beta*x))
            
    return {
        "Characteristic Equation": sp.Eq(char_eq, 0),
        "Roots": roots,
        "Root Classification": root_type,
        "Homogeneous Solution y_h(x)": gen_sol
    }
