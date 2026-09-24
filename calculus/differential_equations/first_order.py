import sympy as sp
from typing import Dict, Union

def solve_exact_equation(M_str: str, N_str: str, vars_str: str = "x, y") -> Dict[str, Union[bool, sp.Expr]]:
    """Checks exactness ∂M/∂y = ∂N/∂x and computes the potential F(x,y) = C."""
    x, y = sp.symbols(vars_str)
    M, N = sp.sympify(M_str), sp.sympify(N_str)
    
    dM_dy = sp.simplify(sp.diff(M, y))
    dN_dx = sp.simplify(sp.diff(N, x))
    
    is_exact = (sp.simplify(dM_dy - dN_dx) == 0)
    
    if not is_exact:
        return {"Exact": False, "dM/dy": dM_dy, "dN/dx": dN_dx}
        
    # Potential Function F(x,y) = ∫ M dx + g(y)
    int_M = sp.integrate(M, x)
    # g'(y) = N - ∂/∂y(∫ M dx)
    g_prime = sp.simplify(N - sp.diff(int_M, y))
    g_y = sp.integrate(g_prime, y)
    
    potential = sp.simplify(int_M + g_y)
    
    return {
        "Exact": True,
        "dM/dy": dM_dy,
        "Potential F(x,y)": potential,
        "General Solution": sp.Eq(potential, sp.Symbol('C'))
    }

def solve_linear_first_order(P_str: str, Q_str: str, x_var: str = "x") -> Dict[str, sp.Expr]:
    """Solves dy/dx + P(x)y = Q(x) using the Integrating Factor method."""
    x = sp.Symbol(x_var)
    P, Q = sp.sympify(P_str), sp.sympify(Q_str)
    
    int_P = sp.integrate(P, x)
    mu = sp.simplify(sp.exp(int_P))
    
    rhs_int = sp.integrate(Q * mu, x)
    C = sp.Symbol('C')
    y_sol = sp.simplify((rhs_int + C) / mu)
    
    return {
        "Integrating Factor mu(x)": mu,
        "Integral of Q*mu": rhs_int,
        "General Solution": y_sol
    }
