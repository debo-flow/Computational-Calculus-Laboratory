from typing import Dict, Union
from calculus.functions.function_engine import FunctionEngine

class AdaptiveSimpson:
    def __init__(self, engine: FunctionEngine, tol: float = 1e-6, max_depth: int = 50):
        self.engine = engine
        self.tol = tol
        self.max_depth = max_depth
        self.evals = 0
        self.subdivisions = []
        
    def _simpson_step(self, a: float, b: float, fa: float, fm: float, fb: float) -> float:
        h = (b - a) / 2.0
        return (h / 3.0) * (fa + 4 * fm + fb)
        
    def _adaptive_recursive(self, a: float, b: float, fa: float, fm: float, fb: float, whole: float, depth: int) -> float:
        m = (a + b) / 2.0
        lm = (a + m) / 2.0
        rm = (m + b) / 2.0
        
        _, flm = self.engine.evaluate(lm)
        _, frm = self.engine.evaluate(rm)
        self.evals += 2
        
        if isinstance(flm, str) or isinstance(frm, str):
            raise ValueError("Singularity encountered during adaptive subdivision.")
            
        left = self._simpson_step(a, m, fa, flm, fm)
        right = self._simpson_step(m, b, fm, frm, fb)
        
        # Error estimate: |S(a,b) - (S(a,m) + S(m,b))| / 15
        error_est = abs(left + right - whole) / 15.0
        
        if error_est <= self.tol or depth >= self.max_depth:
            self.subdivisions.append((a, b))
            return left + right + (left + right - whole) / 15.0 # Richardson extrapolation applied
            
        return (self._adaptive_recursive(a, m, fa, flm, fm, left, depth + 1) +
                self._adaptive_recursive(m, b, fm, frm, fb, right, depth + 1))

    def integrate(self, a: float, b: float) -> Dict[str, Union[float, str, int, list]]:
        self.evals = 0
        self.subdivisions = []
        
        m = (a + b) / 2.0
        _, fa = self.engine.evaluate(a)
        _, fm = self.engine.evaluate(m)
        _, fb = self.engine.evaluate(b)
        self.evals += 3
        
        if any(isinstance(v, str) for v in [fa, fm, fb]):
            return {"Status": "Failed", "Reason": "Singularity at initial boundaries or midpoint."}
            
        whole = self._simpson_step(a, b, fa, fm, fb)
        
        try:
            result = self._adaptive_recursive(a, b, fa, fm, fb, whole, 1)
            return {
                "Status": "Success",
                "Approximation": result,
                "Evaluations": self.evals,
                "Subdivisions": sorted(self.subdivisions)
            }
        except ValueError as e:
            return {"Status": "Failed", "Reason": str(e)}
