import sympy as sp
from typing import List, Dict, Union
from .multivariable_engine import MultivariableEngine

def compute_gradient(engine: MultivariableEngine) -> Dict[str, Union[List[sp.Expr], sp.Expr]]:
    """Calculates the gradient vector and its symbolic magnitude."""
    grad = [sp.simplify(sp.diff(engine.expression, v)) for v in engine.vars]
    magnitude = sp.simplify(sp.sqrt(sum(g**2 for g in grad)))
    return {"Gradient": grad, "Magnitude": magnitude}

def evaluate_gradient(engine: MultivariableEngine, point: List[float]) -> Dict[str, Union[List[float], float, str]]:
    """Evaluates the gradient and magnitude at a specific point."""
    grad_sym = compute_gradient(engine)["Gradient"]
    sub_map = dict(zip(engine.vars, point))
    try:
        grad_num = [float(g.subs(sub_map).evalf()) for g in grad_sym]
        mag_num = sum(g**2 for g in grad_num)**0.5
        return {"Gradient Vector": grad_num, "Magnitude": mag_num}
    except Exception:
        return {"Status": "Undefined at point."}
