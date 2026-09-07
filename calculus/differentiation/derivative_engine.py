import sympy as sp
from typing import Dict, Union, Tuple
from calculus.functions.function_engine import FunctionEngine

class DerivativeEngine:
    """
    Symbolic engine for calculating derivatives, higher-order derivatives,
    and advanced differentiation techniques.
    """
    def __init__(self, engine: FunctionEngine):
        self.engine = engine
        self.x = engine.x
        self.expr = engine.expression

    def get_derivative(self, order: int = 1) -> sp.Expr:
        """Calculates the n-th order symbolic derivative."""
        if order < 1:
            raise ValueError("Derivative order must be >= 1.")
        return sp.diff(self.expr, self.x, order)

    def evaluate_derivative(self, point: float, order: int = 1) -> Union[float, str]:
        """Evaluates the n-th derivative at a specific point."""
        deriv = self.get_derivative(order)
        val = deriv.subs(self.x, point)
        if val.has(sp.zoo, sp.nan, sp.oo, -sp.oo) or not val.is_real:
            return "Undefined"
        return float(val.evalf())

    @staticmethod
    def implicit_differentiation(eq_str: str) -> sp.Expr:
        """
        Performs implicit differentiation dy/dx for an equation string.
        Equation should be formatted like 'x**2 + y**2 = 25' or 'x**2 + y**2 - 25'.
        """
        x, y = sp.symbols('x y')
        if '=' in eq_str:
            lhs, rhs = eq_str.split('=')
            expr = sp.sympify(lhs) - sp.sympify(rhs)
        else:
            expr = sp.sympify(eq_str)
            
        y_func = sp.Function('y')(x)
        expr_func = expr.subs(y, y_func)
        return sp.idiff(expr_func, y_func, x)

    @staticmethod
    def parametric_differentiation(x_t_str: str, y_t_str: str) -> Dict[str, sp.Expr]:
        """
        Calculates dy/dx for parametric equations x(t), y(t).
        """
        t = sp.Symbol('t')
        x_t = sp.sympify(x_t_str)
        y_t = sp.sympify(y_t_str)
        
        dx_dt = sp.diff(x_t, t)
        dy_dt = sp.diff(y_t, t)
        
        if dx_dt == 0:
            dy_dx = sp.zoo # Infinity / Vertical tangent
        else:
            dy_dx = sp.simplify(dy_dt / dx_dt)
            
        return {"dx/dt": dx_dt, "dy/dt": dy_dt, "dy/dx": dy_dx}

    def logarithmic_differentiation(self) -> Dict[str, sp.Expr]:
        """
        Applies logarithmic differentiation: y = f(x) -> ln(y) = ln(f(x)) -> y' = f(x) * d/dx[ln(f(x))]
        """
        ln_f = sp.log(self.expr)
        deriv_ln = sp.diff(ln_f, self.x)
        dy_dx = sp.simplify(self.expr * deriv_ln)
        return {"ln(y)": ln_f, "d/dx[ln(y)]": deriv_ln, "dy/dx": dy_dx}
