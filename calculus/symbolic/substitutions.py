import sympy as sp
from typing import Dict

def symbolic_substitute(expr: sp.Expr, sub_map: Dict[str, str]) -> sp.Expr:
    """Performs simultaneous symbolic substitutions."""
    from .expression_parser import safe_parse
    
    parsed_map = {safe_parse(k): safe_parse(v) for k, v in sub_map.items()}
    return expr.subs(parsed_map, simultaneous=True)
