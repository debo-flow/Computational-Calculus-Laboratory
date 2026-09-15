import sympy as sp
from .multivariable_engine import MultivariableEngine

def compute_partial(engine: MultivariableEngine, wrt_vars: List[sp.Symbol]) -> sp.Expr:
    """Computes high-order or mixed partial derivatives."""
    expr = engine.expression
    for var in wrt_vars:
        expr = sp.diff(expr, var)
    return sp.simplify(expr)

def compare_mixed_partials(engine: MultivariableEngine, v1: sp.Symbol, v2: sp.Symbol) -> dict:
    """Demonstrates Clairaut's Theorem on equality of mixed partials."""
    f_v1_v2 = sp.simplify(sp.diff(sp.diff(engine.expression, v1), v2))
    f_v2_v1 = sp.simplify(sp.diff(sp.diff(engine.expression, v2), v1))
    return {
        "f_xy": f_v1_v2,
        "f_yx": f_v2_v1,
        "Equality": f_v1_v2 == f_v2_v1,
        "Note": "Equality holds if the mixed partials are continuous (Clairaut's Theorem)."
    }
