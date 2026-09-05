import sympy as sp
from typing import Dict, Union

def classify_discontinuity(results: Dict[str, Union[sp.Expr, str, bool]]) -> str:
    """
    Classifies the type of discontinuity based on limit and function values.
    """
    if results["Continuous"]:
        return "None (Function is Continuous)"

    lhl = results["LHL"]
    rhl = results["RHL"]
    f_a = results["f(a)"]

    # Check for Infinite Discontinuity
    if lhl in [sp.oo, -sp.oo, sp.zoo] or rhl in [sp.oo, -sp.oo, sp.zoo]:
        return "Infinite Discontinuity"

    # Check for Oscillatory Discontinuity (AccumulationBounds in SymPy)
    if "AccumulationBounds" in str(lhl) or "AccumulationBounds" in str(rhl):
        return "Oscillatory Discontinuity"

    # Both one-sided limits exist and are finite real numbers
    if hasattr(lhl, 'is_real') and lhl.is_real and hasattr(rhl, 'is_real') and rhl.is_real:
        if lhl == rhl:
            # Limits are equal, but function is undefined or unequal to limit
            return "Removable Discontinuity"
        else:
            # Limits are finite but unequal
            return "Jump Discontinuity"

    return "Essential / Unclassified Discontinuity"
