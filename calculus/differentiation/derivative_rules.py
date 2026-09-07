import sympy as sp

def identify_primary_rule(expr: sp.Expr) -> str:
    """Heuristically identifies the outer rule applied to the expression."""
    if expr.is_Add:
        return "Sum/Difference Rule"
    elif expr.is_Mul:
        return "Product Rule (and possibly Constant Multiple Rule)"
    elif isinstance(expr, sp.Pow):
        return "Power Rule / Chain Rule"
    elif isinstance(expr, sp.Function):
        return "Chain Rule (Outer function derivative)"
    elif expr.is_Number or expr.is_Symbol:
        return "Basic Power/Constant Rule"
    return "Combination of Rules"
