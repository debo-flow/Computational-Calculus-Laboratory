import sympy as sp
from calculus.functions.function_engine import FunctionEngine
from calculus.differentiation.derivative_engine import DerivativeEngine

class ApplicationAnalysisEngine:
    """Coordinates theorems, tangent properties, and approximations."""
    def __init__(self, engine: FunctionEngine):
        self.engine = engine
        self.dev_eng = DerivativeEngine(engine)

    def tangent_and_normal(self, a: float) -> dict:
        _, f_a = self.engine.evaluate(a)
        f_prime_a = self.dev_eng.evaluate_derivative(a, 1)
        
        if isinstance(f_prime_a, str) or isinstance(f_a, str):
            return {"Error": "Tangent undefined at this point."}
            
        tangent_eq = f"{f_a} + {f_prime_a}*(x - {a})"
        normal_m = "Undefined (Vertical)" if f_prime_a == 0 else -1/f_prime_a
        normal_eq = f"{f_a} + ({normal_m})*(x - {a})" if f_prime_a != 0 else f"x = {a}"
        
        return {
            "Point": (a, f_a),
            "Tangent Slope": f_prime_a,
            "Tangent Equation": tangent_eq,
            "Normal Slope": normal_m,
            "Normal Equation": normal_eq
        }

    def mean_value_theorem(self, a: float, b: float) -> dict:
        _, f_a = self.engine.evaluate(a)
        _, f_b = self.engine.evaluate(b)
        
        if isinstance(f_a, str) or isinstance(f_b, str):
            return {"Status": "Failed", "Reason": "Function undefined at boundaries."}
            
        secant_slope = (f_b - f_a) / (b - a)
        f_prime = self.dev_eng.get_derivative(1)
        
        try:
            candidates = sp.solve(sp.Eq(f_prime, secant_slope), self.engine.x)
            valid_c = [float(c.evalf()) for c in candidates if c.is_real and a < float(c.evalf()) < b]
            return {"Status": "Verified", "Secant Slope": secant_slope, "Valid c": valid_c}
        except Exception:
            return {"Status": "Error", "Reason": "Could not solve f'(c) = slope symbolically."}

    def linear_approximation(self, a: float, x_eval: float) -> dict:
        _, f_a = self.engine.evaluate(a)
        f_prime_a = self.dev_eng.evaluate_derivative(a, 1)
        _, f_x_actual = self.engine.evaluate(x_eval)
        
        if any(isinstance(v, str) for v in [f_a, f_prime_a, f_x_actual]):
            return {"Error": "Undefined values in calculation."}
            
        l_x = f_a + f_prime_a * (x_eval - a)
        return {
            "L(x) Equation": f"{f_a} + {f_prime_a}*(x - {a})",
            "Approx Value L(x)": l_x,
            "Exact Value f(x)": f_x_actual,
            "Absolute Error": abs(f_x_actual - l_x)
        }
