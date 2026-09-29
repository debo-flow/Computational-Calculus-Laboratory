import sympy as sp
from typing import Dict, List

def define_symbols_with_assumptions(var_names: List[str], assumptions: Dict[str, bool]) -> Dict[str, sp.Symbol]:
    """Generates symbols respecting mathematical constraints (e.g., real=True, positive=True)."""
    return {name: sp.Symbol(name, **assumptions) for name in var_names}

def apply_assumptions_to_expr(expr_str: str, var_names: List[str], assumptions: Dict[str, bool]) -> sp.Expr:
    """Parses an expression and maps restricted symbols into it."""
    from .expression_parser import safe_parse
    expr = safe_parse(expr_str, evaluate=False)
    
    symbols = define_symbols_with_assumptions(var_names, assumptions)
    sub_map = {sp.Symbol(name): sym for name, sym in symbols.items()}
    
    return expr.subs(sub_map)
