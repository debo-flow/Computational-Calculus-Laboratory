from typing import Dict, Union
from calculus.functions.function_engine import FunctionEngine
from calculus.differentiation.derivative_engine import DerivativeEngine
from numerical.differentiation.finite_difference import STENCILS
from numerical.differentiation.derivative_approximations import apply_stencil

class NumericalDifferentiationEngine:
    def __init__(self, engine: FunctionEngine):
        self.engine = engine
        self.sym_eng = DerivativeEngine(engine)

    def analyze_reliability(self, exact: float, approx: float, h: float) -> str:
        """Classifies numerical reliability based on absolute error and floating point limits."""
        if isinstance(approx, str): return "FAILED"
        err = abs(exact - approx)
        if err < 1e-6 and h > 1e-10: return "RELIABLE"
        if err < 1e-3: return "CAUTION (Moderate Error)"
        if h <= 1e-11: return "UNSTABLE (Floating-Point Round-Off / Cancellation)"
        return "FAILED (Divergence or Singularity)"

    def adaptive_step_size(self, x: float, stencil_name: str = "Central (2nd Order)", tol: float = 1e-6) -> Dict:
        """
        Searches for the optimal h by halving it until the difference between 
        successive approximations is below tolerance, or round-off is detected.
        """
        stencil = STENCILS[stencil_name]
        h = 0.1
        prev_approx = apply_stencil(self.engine, x, h, stencil)
        
        for _ in range(20): # Max 20 halvings
            h /= 2.0
            approx = apply_stencil(self.engine, x, h, stencil)
            
            if isinstance(approx, str) or isinstance(prev_approx, str):
                return {"Status": "Failed", "Reason": "Evaluation boundary hit"}
                
            diff = abs(approx - prev_approx)
            if diff < tol:
                return {"Status": "Converged", "Optimal h": h, "Approximation": approx, "Estimated Error": diff}
            
            # If difference starts growing, we hit round-off cancellation
            if diff > abs(prev_approx) * 1e-2 and h < 1e-6:
                return {"Status": "Round-off Detected", "Best h": h*2, "Approximation": prev_approx}
                
            prev_approx = approx
            
        return {"Status": "Unstable / Did not converge", "Final h": h, "Approximation": prev_approx}
