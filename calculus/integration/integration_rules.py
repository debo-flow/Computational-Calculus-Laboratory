import sympy as sp
from typing import Dict, Any

def identify_integration_rule(expr: sp.Expr, x: sp.Symbol) -> Dict[str, str]:
    """
    Identifies the primary integration rule matching the mathematical structure of f(x).
    """
    if not expr.has(x):
        return {
            "Rule": "Constant Rule",
            "Formula": r"\int c \, dx = c x + C",
            "Explanation": "The integrand contains no variable terms. The integral scales linearly with x."
        }

    if expr.is_Pow and expr.base == x:
        power = expr.exp
        if power == -1:
            return {
                "Rule": "Logarithmic Rule",
                "Formula": r"\int \frac{1}{x} \, dx = \ln|x| + C",
                "Explanation": "Special rational case where n = -1 yields a natural logarithm."
            }
        return {
            "Rule": "Power Rule",
            "Formula": r"\int x^n \, dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1)",
            "Explanation": f"Polynomial power term integrated with power increment {power} + 1."
        }

    if expr.is_Add:
        return {
            "Rule": "Sum / Difference Rule",
            "Formula": r"\int [f(x) \pm g(x)] \, dx = \int f(x) \, dx \pm \int g(x) \, dx",
            "Explanation": "The integral of a finite sum is the sum of the individual antiderivatives."
        }

    if expr.is_Mul:
        # Check constant multiple
        coeffs, non_coeffs = expr.as_coeff_Mul()
        if coeffs != 1 and non_coeffs != expr:
            return {
                "Rule": "Constant Multiple Rule",
                "Formula": r"\int c \cdot f(x) \, dx = c \int f(x) \, dx",
                "Explanation": f"Constant factor {coeffs} is factored outside the integral."
            }
        return {
            "Rule": "Product Structure / By Parts Candidate",
            "Formula": r"\int u \, dv = uv - \int v \, du",
            "Explanation": "Multiplicative integrand suitable for Integration by Parts or substitution."
        }

    if isinstance(expr, (sp.sin, sp.cos, sp.tan, sp.sec, sp.csc, sp.cot)):
        return {
            "Rule": "Trigonometric Rule",
            "Formula": r"\int \text{trig}(x) \, dx",
            "Explanation": "Standard direct trigonometric antiderivative identity."
        }

    if isinstance(expr, sp.exp):
        return {
            "Rule": "Exponential Rule",
            "Formula": r"\int e^x \, dx = e^x + C",
            "Explanation": "Natural exponential function is invariant under differentiation and integration."
        }

    return {
        "Rule": "General Symbolic Integration",
        "Formula": r"\int f(x) \, dx = F(x) + C",
        "Explanation": "Evaluated using SymPy's Risch algorithm or heuristic integration pattern matching."
    }
