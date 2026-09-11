import sympy as sp
from typing import Dict, Any, Union
from calculus.functions.function_engine import FunctionEngine
from calculus.differentiation.derivative_engine import DerivativeEngine

def compute_indefinite_integral(engine: FunctionEngine) -> Dict[str, Any]:
    """
    Computes the symbolic antiderivative ∫ f(x) dx, explicitly appending the constant + C.
    Verifies the antiderivative using the Differentiation Engine: d/dx[F(x)] == f(x).
    """
    x = engine.x
    expr = engine.expression
    C = sp.Symbol('C')

    try:
        raw_antiderivative = sp.integrate(expr, x)
        
        # Check for non-elementary representations
        has_unevaluated_integral = raw_antiderivative.has(sp.Integral)
        
        simplified_antiderivative = sp.simplify(raw_antiderivative)
        full_expression = simplified_antiderivative + C
        
        # Verification via differentiation
        derivative_of_antiderivative = sp.diff(raw_antiderivative, x)
        simplified_diff = sp.simplify(derivative_of_antiderivative - expr)
        is_verified = (simplified_diff == 0)

        return {
            "Status": "Success",
            "Antiderivative": raw_antiderivative,
            "Simplified": simplified_antiderivative,
            "FullWithConstant": full_expression,
            "Constant": "+ C",
            "IsElementary": not has_unevaluated_integral,
            "VerificationDerivative": derivative_of_antiderivative,
            "Verified": is_verified,
            "Explanation": "Antiderivative computed symbolically and verified via differentiation."
        }
    except Exception as e:
        return {
            "Status": "Failed",
            "Error": str(e),
            "Antiderivative": None,
            "Simplified": None,
            "FullWithConstant": None,
            "Verified": False
        }
