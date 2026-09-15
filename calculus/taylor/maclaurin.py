from .polynomial import TaylorPolynomial
from calculus.functions.function_engine import FunctionEngine

class MaclaurinPolynomial(TaylorPolynomial):
    """Special case of Taylor Polynomial where expansion point a = 0."""
    def __init__(self, engine: FunctionEngine):
        super().__init__(engine, a=0.0)
