from typing import Dict, Union
from calculus.functions.function_engine import FunctionEngine

class NumericalDerivativeEngine:
    def __init__(self, engine: FunctionEngine):
        self.engine = engine

    def evaluate_all(self, x_val: float, h: float = 1e-5) -> Dict[str, Union[float, str]]:
        if h == 0:
            raise ValueError("Step size h cannot be zero.")
            
        try:
            _, fx = self.engine.evaluate(x_val)
            _, fxh = self.engine.evaluate(x_val + h)
            _, fx_minus_h = self.engine.evaluate(x_val - h)

            if any(isinstance(val, str) for val in [fx, fxh, fx_minus_h]):
                return {"Forward": "N/A", "Backward": "N/A", "Central": "N/A"}

            forward = (fxh - fx) / h
            backward = (fx - fx_minus_h) / h
            central = (fxh - fx_minus_h) / (2 * h)

            return {
                "Forward": forward,
                "Backward": backward,
                "Central": central
            }
        except Exception:
            return {"Forward": "Error", "Backward": "Error", "Central": "Error"}
