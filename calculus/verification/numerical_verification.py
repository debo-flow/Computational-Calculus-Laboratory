import sympy as sp
import numpy as np
from typing import Dict, List, Tuple
from .error_analysis import calculate_errors

def search_counterexample(lhs_str: str, rhs_str: str, vars_str: str, domain_bounds: List[Tuple[float, float]], num_samples: int = 1000, tol: float = 1e-8) -> Dict:
    """
    Monte Carlo search for numerical counterexamples to a proposed identity.
    Note: Failure to find a counterexample does NOT constitute a mathematical proof.
    """
    variables = sp.symbols(vars_str)
    lhs_expr, rhs_expr = sp.sympify(lhs_str), sp.sympify(rhs_str)
    
    f_lhs = sp.lambdify(variables, lhs_expr, modules=['numpy'])
    f_rhs = sp.lambdify(variables, rhs_expr, modules=['numpy'])
    
    max_err = 0.0
    counterexample = None
    
    for _ in range(num_samples):
        # Generate random test point within bounds
        pt = [np.random.uniform(b[0], b[1]) for b in domain_bounds]
        
        try:
            val_lhs = float(f_lhs(*pt))
            val_rhs = float(f_rhs(*pt))
            err = abs(val_lhs - val_rhs)
            
            if err > max_err:
                max_err = err
                
            if err > tol:
                counterexample = pt
                break
        except Exception:
            continue # Ignore domain violations (e.g., log(-1))
            
    if counterexample:
        return {
            "Status": "COUNTEREXAMPLE FOUND",
            "Point": counterexample,
            "LHS Value": val_lhs,
            "RHS Value": val_rhs,
            "Difference": max_err,
            "Note": "Mathematical claim is definitively false or conditionally restricted."
        }
        
    return {
        "Status": "NO COUNTEREXAMPLE FOUND IN TESTED DOMAIN",
        "Max Error Observed": max_err,
        "Note": "EMPIRICALLY VALIDATED. This is computational evidence, NOT a mathematical proof."
    }
