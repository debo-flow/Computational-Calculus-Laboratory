import sympy as sp
from typing import Dict, Any

def analyze_bernoulli(P_str: str, Q_str: str, n_val: float, var_name: str = 'x') -> Dict[str, Any]:
    """Analyzes dy/dx + P(x)y = Q(x)y^n via substitution v = y^(1-n)."""
    if n_val == 0 or n_val == 1:
        return {"Status": "Not a strict Bernoulli case (n=0 is linear, n=1 is separable/linear)."}
        
    x = sp.Symbol(var_name)
    P, Q = sp.sympify(P_str), sp.sympify(Q_str)
    
    # Transformation: v = y^(1-n) -> v' + (1-n)P(x)v = (1-n)Q(x)
    P_new = sp.simplify((1 - n_val) * P)
    Q_new = sp.simplify((1 - n_val) * Q)
    
    # Integrating factor for v
    int_P = sp.integrate(P_new, x)
    mu = sp.simplify(sp.exp(int_P))
    
    rhs_int = sp.integrate(Q_new * mu, x)
    C = sp.Symbol('C')
    v_sol = sp.simplify((rhs_int + C) / mu)
    
    # Back substitution: y = v^(1 / (1-n))
    y_sol = sp.simplify(v_sol ** (1 / (1 - n_val)))
    
    return {
        "Status": "Success",
        "Substitution": f"v = y^{1 - n_val}",
        "Linearized v Equation": sp.Eq(sp.Function('v')(x).diff(x) + P_new * sp.Function('v')(x), Q_new),
        "Integrating Factor mu(x)": mu,
        "Solution v(x)": v_sol,
        "Final Implicit/Explicit y(x)": sp.Eq(sp.Function('y')(x), y_sol)
    }

def analyze_exact(M_str: str, N_str: str, x_var: str = 'x', y_var: str = 'y') -> Dict[str, Any]:
    """Analyzes M(x,y)dx + N(x,y)dy = 0 for exactness and constructs F(x,y)=C."""
    x, y = sp.symbols(f"{x_var} {y_var}")
    M, N = sp.sympify(M_str), sp.sympify(N_str)
    
    dM_dy = sp.simplify(sp.diff(M, y))
    dN_dx = sp.simplify(sp.diff(N, x))
    
    is_exact = (sp.simplify(dM_dy - dN_dx) == 0)
    if not is_exact:
        return {"Exact": False, "dM/dy": dM_dy, "dN/dx": dN_dx}
        
    int_M = sp.integrate(M, x)
    g_prime = sp.simplify(N - sp.diff(int_M, y))
    g_y = sp.integrate(g_prime, y)
    potential = sp.simplify(int_M + g_y)
    
    return {
        "Exact": True,
        "dM/dy": dM_dy,
        "Potential F(x,y)": potential,
        "Implicit Solution": sp.Eq(potential, sp.Symbol('C'))
    }
