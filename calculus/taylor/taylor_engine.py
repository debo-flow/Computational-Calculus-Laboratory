from calculus.functions.function_engine import FunctionEngine
from .polynomial import TaylorPolynomial
from .maclaurin import MaclaurinPolynomial
from .remainder import calculate_remainder_bounds
from .convergence import analyze_radius_of_convergence
from .taylor_analysis import verify_taylor_derivatives, calculus_on_taylor
from .approximation import estimate_order_for_tolerance

class TaylorEngine:
    """Central coordinator for Taylor Series Laboratory."""
    def __init__(self, engine: FunctionEngine, a: float = 0.0):
        self.engine = engine
        self.a = a
        self.poly = MaclaurinPolynomial(engine) if a == 0 else TaylorPolynomial(engine, a)

    def get_polynomial(self, order: int):
        return self.poly.generate(order)

    def get_coefficients(self, order: int):
        return self.poly.get_coefficient_table(order)

    def get_remainder_analysis(self, x_eval: float, order: int):
        return calculate_remainder_bounds(self.poly, x_eval, order)

    def get_convergence(self):
        return analyze_radius_of_convergence(self.engine.expression, self.engine.x, self.a)
        
    def verify_polynomial(self, order: int):
        return verify_taylor_derivatives(self.poly, order)
        
    def find_target_order(self, x_eval: float, tol: float):
        return estimate_order_for_tolerance(self.poly, x_eval, tol)
