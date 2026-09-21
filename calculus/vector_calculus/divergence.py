import sympy as sp
from .vector_fields import VectorFieldEngine

def compute_divergence(engine: VectorFieldEngine) -> sp.Expr:
    """∇ · F = P_x + Q_y + R_z"""
    div = sum(sp.diff(comp, var) for comp, var in zip(engine.components, engine.vars))
    return sp.simplify(div)
