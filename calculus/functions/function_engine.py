import sympy as sp
import numpy as np
from typing import Tuple, List, Dict, Optional, Union

class FunctionEngine:
    """
    Core mathematical engine for safely parsing, evaluating, and manipulating
    single-variable mathematical expressions.
    """
    
    def __init__(self, expression_str: str):
        self.x = sp.Symbol('x')
        self.expression_str = expression_str
        self.expression = self._parse_expression(expression_str)
        
    def _parse_expression(self, expr_str: str) -> sp.Expr:
        """Safely parses a string into a SymPy expression."""
        if not expr_str or not expr_str.strip():
            raise ValueError("Expression cannot be empty.")
            
        # Standardize input (e.g., convert ^ to ** for Python syntax)
        expr_str = expr_str.replace('^', '**')
        
        try:
            # sympify safely evaluates mathematical strings into SymPy objects
            return sp.sympify(expr_str, evaluate=False)
        except (sp.SympifyError, TypeError, SyntaxError) as e:
            raise ValueError(f"Invalid mathematical expression: {expr_str}. Error: {str(e)}")

    def evaluate(self, value: float) -> Tuple[sp.Expr, Union[float, str]]:
        """
        Evaluates the function at a specific x value.
        Returns a tuple of (Exact Symbolic Result, Numerical Approximation).
        """
        try:
            exact_result = self.expression.subs(self.x, value)
            
            if exact_result.is_infinite or exact_result == sp.zoo:
                return exact_result, "Undefined/Infinity"
            
            # Evaluate to float
            num_result = float(exact_result.evalf())
            return exact_result, num_result
        except Exception as e:
            raise ValueError(f"Evaluation failed at x={value}: {str(e)}")

    def get_symbolic_representations(self) -> Dict[str, sp.Expr]:
        """Returns simplified, expanded, and factorized forms."""
        return {
            "Original": self.expression,
            "Simplified": sp.simplify(self.expression),
            "Expanded": sp.expand(self.expression),
            "Factorized": sp.factor(self.expression)
        }

    def analyze(self) -> Dict[str, str]:
        """Performs basic function analysis."""
        analysis = {"Validity": "Valid Expression"}
        
        # Domain (Exact where practical)
        try:
            from sympy.calculus.util import continuous_domain
            domain = continuous_domain(self.expression, self.x, sp.S.Reals)
            analysis["Exact Domain (Reals)"] = sp.latex(domain)
        except Exception:
            analysis["Exact Domain (Reals)"] = "Domain calculation too complex for basic analysis."

        return analysis

    def generate_table(self, start: float, end: float, step: float) -> List[Dict[str, Union[float, str]]]:
        """Generates a numerical table for the function."""
        if step <= 0:
            raise ValueError("Step size must be strictly positive.")
        if start > end:
            raise ValueError("Start value must be less than or equal to end value.")

        table = []
        current = start
        
        # Using a while loop to avoid float precision issues with numpy arange
        while current <= end + 1e-9:  # Small epsilon for float comparison
            exact, num = self.evaluate(current)
            table.append({
                "x": round(current, 5),
                "f(x)": round(num, 5) if isinstance(num, float) else num
            })
            current += step
            
        return table

