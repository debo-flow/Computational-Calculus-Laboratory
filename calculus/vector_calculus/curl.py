import sympy as sp
from typing import List
from .vector_fields import VectorFieldEngine

def compute_curl(engine: VectorFieldEngine) -> List[sp.Expr]:
    """∇ × F"""
    if engine.dim == 2:
        P, Q = engine.components
        x, y = engine.vars[:2]
        return [sp.S.Zero, sp.S.Zero, sp.simplify(sp.diff(Q, x) - sp.diff(P, y))]
    elif engine.dim == 3:
        P, Q, R = engine.components
        x, y, z = engine.vars
        return [
            sp.simplify(sp.diff(R, y) - sp.diff(Q, z)),
            sp.simplify(sp.diff(P, z) - sp.diff(R, x)),
            sp.simplify(sp.diff(Q, x) - sp.diff(P, y))
        ]
    return ["Unsupported dimension"]
