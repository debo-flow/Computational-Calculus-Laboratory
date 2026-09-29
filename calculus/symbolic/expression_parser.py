import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

def safe_parse(expr_str: str, evaluate: bool = True) -> sp.Expr:
    """
    Safely parses a mathematical string into a SymPy expression.
    Explicitly disables arbitrary code execution and restricts locals/globals.
    """
    if not isinstance(expr_str, str) or not expr_str.strip():
        raise ValueError("Empty or invalid expression string.")
        
    transformations = standard_transformations + (implicit_multiplication_application,)
    
    # Safe dictionary restricting available functions to SymPy math functions
    safe_dict = {"__builtins__": None}
    safe_dict.update({k: v for k, v in vars(sp).items() if not k.startswith('_')})
    
    try:
        clean_str = expr_str.replace("^", "**")
        expr = parse_expr(clean_str, local_dict=safe_dict, global_dict={}, 
                          transformations=transformations, evaluate=evaluate)
        return expr
    except Exception as e:
        raise ValueError(f"Syntax error in expression: {str(e)}")
