import sympy as sp
from .polynomial import TaylorPolynomial

def verify_taylor_derivatives(poly: TaylorPolynomial, order: int) -> dict:
    """Verifies that T_n^(k)(a) == f^(k)(a) for k=0...n."""
    T_n = poly.generate(order)
    results = {}
    all_match = True
    
    current_T_deriv = T_n
    for k in range(order + 1):
        # Evaluate T_n^(k)(a)
        T_val = sp.simplify(current_T_deriv.subs(poly.x, poly.a))
        # Exact f^(k)(a)
        f_val = sp.simplify(poly.get_derivative(k).subs(poly.x, poly.a))
        
        match = sp.simplify(T_val - f_val) == 0
        results[k] = {"T_n^(k)(a)": T_val, "f^(k)(a)": f_val, "Match": match}
        if not match: all_match = False
        
        current_T_deriv = sp.diff(current_T_deriv, poly.x)
        
    return {"All Verified": all_match, "Derivatives": results}

def calculus_on_taylor(poly: TaylorPolynomial, order: int) -> dict:
    """Demonstrates derivative and integral of the Taylor polynomial."""
    T_n = poly.generate(order)
    
    T_prime = sp.diff(T_n, poly.x)
    f_prime = poly.get_derivative(1)
    
    T_int = sp.integrate(T_n, poly.x)
    f_int = sp.integrate(poly.engine.expression, poly.x)
    
    return {
        "Original T_n(x)": T_n,
        "d/dx [T_n(x)]": T_prime,
        "d/dx [f(x)]": f_prime,
        "∫ T_n(x) dx": T_int,
        "∫ f(x) dx": f_int
    }
