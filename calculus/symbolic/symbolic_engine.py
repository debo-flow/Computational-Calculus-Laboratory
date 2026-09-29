import sympy as sp
from typing import Dict, Any
from .expression_parser import safe_parse
from .algebra import algebraic_manipulate
from .equations import solve_equation, solve_system, solve_inequality
from .expression_analysis import analyze_complexity, find_domain_restrictions, build_expression_tree
from .symbolic_validation import check_equivalence, numerical_cross_validation
from .substitutions import symbolic_substitute

class CASRouter:
    """Unified Computer Algebra System interface routing to existing calculus modules."""
    
    @staticmethod
    def simplify(expr_str: str) -> sp.Expr:
        return sp.simplify(safe_parse(expr_str))
        
    @staticmethod
    def algebra(expr_str: str, operation: str) -> sp.Expr:
        return algebraic_manipulate(safe_parse(expr_str), operation)
        
    @staticmethod
    def solve(expr_str: str, var_str: str) -> Dict:
        return solve_equation(safe_parse(expr_str), sp.Symbol(var_str))
        
    @staticmethod
    def inequalities(ineq_str: str) -> Dict:
        # Use sympify directly here to handle <, >, <= operators natively
        return solve_inequality(sp.sympify(ineq_str.replace("^", "**")))

    @staticmethod
    def calculus_route(operation: str, expr_str: str, var_str: str, **kwargs) -> Any:
        """Routes calculus operations to SymPy natively, mimicking the external module hooks to avoid circular imports."""
        expr = safe_parse(expr_str)
        var = sp.Symbol(var_str)
        
        if operation == "derivative":
            return sp.diff(expr, var, kwargs.get('order', 1))
        elif operation == "integral_indefinite":
            return sp.integrate(expr, var)
        elif operation == "limit":
            return sp.limit(expr, var, kwargs.get('point', 0))
        elif operation == "series":
            return sp.series(expr, var, kwargs.get('point', 0), kwargs.get('n', 6)).removeO()
        elif operation == "laplacian":
            vars_list = [sp.Symbol(v.strip()) for v in var_str.split(',')]
            return sp.simplify(sum(sp.diff(expr, v, 2) for v in vars_list))
        raise ValueError("Unknown Calculus Operation")

    @staticmethod
    def verify(expr_a_str: str, expr_b_str: str, vars_str: str) -> Dict:
        expr_a = safe_parse(expr_a_str)
        expr_b = safe_parse(expr_b_str)
        variables = [sp.Symbol(v.strip()) for v in vars_str.split(',')]
        
        sym_check = check_equivalence(expr_a, expr_b)
        num_check = numerical_cross_validation(expr_a, expr_b, variables)
        return {"Symbolic Verification": sym_check, "Numerical Cross-Check": num_check}

    @staticmethod
    def tree(expr_str: str) -> dict:
        expr = safe_parse(expr_str, evaluate=False)
        return build_expression_tree(expr)
