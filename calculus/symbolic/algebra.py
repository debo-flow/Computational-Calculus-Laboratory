import sympy as sp
from typing import Dict

def algebraic_manipulate(expr: sp.Expr, operation: str, **kwargs) -> sp.Expr:
    """Routes an expression to the correct symbolic algebraic transformation."""
    if operation == "expand": return sp.expand(expr)
    if operation == "factor": return sp.factor(expr)
    if operation == "collect": return sp.collect(expr, kwargs.get('var', sp.Symbol('x')))
    if operation == "cancel": return sp.cancel(expr)
    if operation == "together": return sp.together(expr)
    if operation == "apart": return sp.apart(expr) # Partial fractions
    raise ValueError(f"Unsupported algebraic operation: {operation}")

def extract_polynomial_info(expr: sp.Expr, var: sp.Symbol) -> Dict:
    poly = sp.poly(expr, var)
    if poly is None:
        return {"Status": "Not a polynomial in the given variable."}
    return {
        "Degree": poly.degree(),
        "Leading Coefficient": poly.LC(),
        "Coefficients": poly.all_coeffs()
    }
