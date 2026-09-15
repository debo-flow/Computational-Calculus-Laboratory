import sympy as sp
from typing import Dict, Any

def analyze_radius_of_convergence(expr: sp.Expr, x: sp.Symbol, a: float) -> Dict[str, Any]:
    """
    Estimates the Radius of Convergence (R) by finding the distance to the 
    nearest singularity in the complex plane.
    """
    a_sym = sp.sympify(a)
    try:
        from sympy.calculus.singularities import singularities
        sings = singularities(expr, x)
        
        if sings == sp.S.EmptySet:
            return {"R": sp.oo, "Interval": "(-∞, ∞)", "Note": "Function is entire (analytic everywhere)."}
            
        # Check distance to singularities
        distances = []
        for s in sings:
            dist = sp.Abs(s - a_sym)
            distances.append(dist)
            
        R = min(distances) if distances else sp.oo
        
        if R == sp.oo:
            interval = "(-∞, ∞)"
        elif R == 0:
            interval = f"[{a_sym}, {a_sym}] (Converges only at expansion point)"
        else:
            interval = f"({a_sym - R}, {a_sym + R}) (Endpoints require manual testing)"
            
        return {"R": R, "Interval": interval, "Note": "Radius determined via distance to nearest complex/real singularity."}
    except Exception as e:
        return {"R": "Unknown", "Interval": "Unknown", "Note": f"Symbolic singularity detection failed: {e}"}
