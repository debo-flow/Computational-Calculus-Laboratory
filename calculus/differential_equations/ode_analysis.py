import sympy as sp
import numpy as np
from typing import Dict, Any, List
from numerical.ode_solvers import solve_adaptive

def classify_single_ode(eq_str: str, func_name: str = 'y', var_name: str = 'x') -> dict:
    """Classifies a symbolic ODE (Order, Linearity, Homogeneity)."""
    x = sp.Symbol(var_name, real=True)
    y = sp.Function(func_name)(x)
    
    eq_parts = eq_str.split('=')
    lhs = sp.sympify(eq_parts[0])
    rhs = sp.sympify(eq_parts[1]) if len(eq_parts) > 1 else sp.S.Zero
    ode_expr = sp.simplify(lhs - rhs)
    
    try:
        classifications = sp.classify_ode(sp.Eq(ode_expr, 0), y)
        order = sp.ode_order(ode_expr, y)
        is_linear = any("linear" in str(c).lower() for c in classifications)
        is_homogeneous = any("homogeneous" in str(c).lower() for c in classifications)
        
        return {
            "Equation": sp.Eq(ode_expr, 0),
            "Order": order,
            "Linear": is_linear,
            "Homogeneous": is_homogeneous,
            "Is Autonomous": not ode_expr.has(x),
            "Classifications": classifications
        }
    except Exception as e:
        return {"Error": f"Classification inconclusive: {e}"}

def parameter_sweep_equilibria(sys_exprs: List[str], vars_str: str, param_str: str, param_vals: List[float]) -> List[Dict]:
    """Evaluates equilibria as a parameter mu changes (Bifurcation Foundation)."""
    from .equilibrium import find_equilibria
    results = []
    param = sp.Symbol(param_str)
    
    for val in param_vals:
        subbed_exprs = [str(sp.sympify(e).subs(param, val)) for e in sys_exprs]
        eqs = find_equilibria(subbed_exprs, vars_str)
        results.append({"Parameter Value": val, "Equilibria": eqs})
        
    return results

def sensitivity_analysis(f_sys, t_end: float, Y0: np.ndarray, delta: float = 1e-5) -> Tuple[np.ndarray, np.ndarray]:
    """Calculates trajectory separation D(t) = |X1(t) - X2(t)| for nearby initial conditions."""
    t1, y1, _ = solve_adaptive(f_sys, 0, Y0, t_end)
    
    # Perturb initial condition slightly
    Y0_pert = Y0.copy()
    Y0_pert[0] += delta
    t2, y2, _ = solve_adaptive(f_sys, 0, Y0_pert, t_end)
    
    # Interpolate onto a common time grid
    from scipy.interpolate import interp1d
    common_t = np.linspace(0, t_end, 1000)
    y1_interp = interp1d(t1, y1, axis=0)(common_t)
    y2_interp = interp1d(t2, y2, axis=0)(common_t)
    
    separation = np.linalg.norm(y1_interp - y2_interp, axis=1)
    return common_t, separation
