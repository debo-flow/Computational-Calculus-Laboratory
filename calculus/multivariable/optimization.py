import sympy as sp
from typing import Dict, List
from .multivariable_engine import MultivariableEngine

def lagrange_multipliers(obj_engine: MultivariableEngine, constraint_str: str) -> Dict:
    """Sets up and solves grad f = lambda * grad g."""
    lam = sp.Symbol('lambda')
    g = sp.sympify(constraint_str)
    
    grad_f = [sp.diff(obj_engine.expression, v) for v in obj_engine.vars]
    grad_g = [sp.diff(g, v) for v in obj_engine.vars]
    
    equations = [gf - lam * gg for gf, gg in zip(grad_f, grad_g)]
    equations.append(g) # Constraint must be equal to 0
    
    try:
        sols = sp.solve(equations, list(obj_engine.vars) + [lam], dict=True)
        valid_pts = []
        for s in sols:
            if all(v.is_real for v in s.values()):
                pt = [float(s[v].evalf()) for v in obj_engine.vars]
                val = obj_engine.evaluate(pt)
                valid_pts.append({"Point": pt, "Lambda": float(s[lam].evalf()), "f(x,y)": val})
        return {"Status": "Success", "Solutions": valid_pts}
    except Exception as e:
        return {"Status": "Failed / Too Complex for Symbolic Solver", "Error": str(e)}

