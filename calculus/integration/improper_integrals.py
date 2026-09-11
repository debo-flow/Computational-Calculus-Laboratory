import sympy as sp
from typing import Dict, Any

def evaluate_improper_integral(expr_str: str, a_val: Any, b_val: Any) -> Dict[str, Any]:
    """
    Evaluates improper integrals involving infinite bounds or singularities.
    Classifies convergence behavior: Convergent, Divergent, or Indeterminate.
    """
    x = sp.Symbol('x')
    try:
        expr = sp.sympify(expr_str.replace('^', '**'))
        
        # Parse infinite bounds
        a = sp.oo if str(a_val).lower() in ['inf', 'oo', 'infinity'] else (-sp.oo if str(a_val).lower() in ['-inf', '-oo', '-infinity'] else sp.sympify(a_val))
        b = sp.oo if str(b_val).lower() in ['inf', 'oo', 'infinity'] else (-sp.oo if str(b_val).lower() in ['-inf', '-oo', '-infinity'] else sp.sympify(b_val))

        result = sp.integrate(expr, (x, a, b))

        if result.has(sp.oo, -sp.oo, sp.zoo) or isinstance(result, sp.Integral):
            classification = "Divergent"
            explanation = "The limiting area grows without bound or oscillates indefinitely."
            num_val = "Undefined / Infinity"
        else:
            classification = "Convergent"
            num_val = float(result.evalf()) if result.is_real else str(result.evalf())
            explanation = f"The infinite region converges to a finite limiting value of {result}."

        return {
            "Status": "Success",
            "Expression": expr,
            "LowerBound": a,
            "UpperBound": b,
            "Classification": classification,
            "Exact": result,
            "Numerical": num_val,
            "Explanation": explanation
        }
    except Exception as e:
        return {
            "Status": "Failed",
            "Classification": "Unable to determine reliably",
            "Error": str(e)
        }
