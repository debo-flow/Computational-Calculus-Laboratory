import sympy as sp
from typing import Dict, Any
from sympy.calculus.singularities import singularities

def analyze_complexity(expr: sp.Expr) -> Dict[str, Any]:
    """Calculates expression tree metrics."""
    def get_depth(e):
        if not e.args: return 1
        return 1 + max(get_depth(arg) for arg in e.args)
        
    return {
        "Node Count": sp.count_ops(expr) + 1,
        "Variables": list(expr.free_symbols),
        "Tree Depth": get_depth(expr)
    }

def build_expression_tree(expr: sp.Expr) -> dict:
    """Recursively builds an AST dictionary for visualization."""
    if not expr.args:
        return {"name": str(expr)}
    return {"name": type(expr).__name__, "children": [build_expression_tree(arg) for arg in expr.args]}

def find_domain_restrictions(expr: sp.Expr, var: sp.Symbol) -> Dict[str, Any]:
    """Finds singular points and valid continuous domains over the Reals."""
    try:
        sings = singularities(expr, var)
        valid_domain = sp.ContinuousDomain(expr, var)
        return {"Singularities": sings, "Continuous Domain": valid_domain}
    except Exception as e:
        return {"Status": f"Domain analysis inconclusive: {str(e)}"}
