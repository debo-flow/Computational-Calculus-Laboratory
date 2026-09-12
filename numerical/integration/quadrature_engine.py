import numpy as np
from typing import Dict, Any, List
from calculus.functions.function_engine import FunctionEngine
from calculus.integration.integral_engine import IntegralEngine
from numerical.validation import calculate_absolute_error, calculate_relative_error
from .trapezoidal import composite_trapezoidal
from .simpson import composite_simpson_13, composite_simpson_38
from .gaussian_quadrature import gauss_legendre_quadrature
from .adaptive_quadrature import AdaptiveSimpson
from .error_analysis import theoretical_error_bound
from .integration_validation import classify_integration_reliability
import math

class NumericalIntegrationEngine:
    """Unified engine coordinating all numerical integration operations."""
    def __init__(self, engine: FunctionEngine):
        self.engine = engine
        
    def _get_exact(self, a: float, b: float) -> float:
        int_eng = IntegralEngine(self.engine)
        res = int_eng.integrate_definite(a, b)
        return res.get("Numerical", None) if isinstance(res.get("Numerical"), float) else None

    def execute_method(self, method: str, a: float, b: float, n: int = None, tol: float = 1e-5) -> Dict[str, Any]:
        exact = self._get_exact(a, b)
        
        try:
            if method == "Trapezoidal":
                res = composite_trapezoidal(self.engine, a, b, n)
            elif method == "Simpson 1/3":
                res = composite_simpson_13(self.engine, a, b, n)
            elif method == "Simpson 3/8":
                res = composite_simpson_38(self.engine, a, b, n)
            elif method == "Gauss-Legendre":
                res = gauss_legendre_quadrature(self.engine, a, b, n)
            elif method == "Adaptive Simpson":
                adapt = AdaptiveSimpson(self.engine, tol=tol)
                res = adapt.integrate(a, b)
            else:
                raise ValueError("Unknown method.")
        except Exception as e:
            res = {"Status": "Failed", "Reason": str(e)}

        report = {
            "Method": method,
            "Interval": f"[{a}, {b}]",
            "Approximation": res.get("Approximation", "N/A"),
            "Reference Exact": exact if exact is not None else "N/A",
            "Evaluations": res.get("Evaluations", "N/A"),
            "Status": res.get("Status", "Failed")
        }
        
        if exact is not None and res.get("Status") == "Success":
            approx = res["Approximation"]
            report["Absolute Error"] = calculate_absolute_error(exact, approx)
            report["Relative Error"] = calculate_relative_error(exact, approx)
            report["Reliability"] = classify_integration_reliability(exact, approx, res["Status"], res["Evaluations"])
        else:
            report["Reliability"] = "FAILED" if res.get("Status") == "Failed" else "CAUTION (No exact reference)"

        if method in ["Trapezoidal", "Simpson 1/3"] and res.get("Status") == "Success":
            report["Theoretical Bound"] = theoretical_error_bound(self.engine, a, b, n, method)

        if method == "Adaptive Simpson" and res.get("Status") == "Success":
            report["Subdivisions"] = res.get("Subdivisions")
            
        return report

    def data_integration(self, x_data: List[float], y_data: List[float]) -> float:
        """Integrates sampled data using non-uniform trapezoidal rule (NumPy trapz)."""
        if len(x_data) != len(y_data) or len(x_data) < 2:
            raise ValueError("Invalid data lengths.")
        return float(np.trapz(y_data, x_data))

    def cumulative_integration(self, a: float, b: float, n: int) -> Dict[str, List[float]]:
        """Numerically constructs F(x) = ∫_a^x f(t) dt over a grid."""
        x_vals = np.linspace(a, b, n)
        y_vals = []
        for x in x_vals:
            _, val = self.engine.evaluate(x)
            y_vals.append(val if isinstance(val, float) else 0.0)
            
        cum_int = np.zeros(n)
        for i in range(1, n):
            h = x_vals[i] - x_vals[i-1]
            cum_int[i] = cum_int[i-1] + (h/2.0) * (y_vals[i-1] + y_vals[i])
            
        return {"x": x_vals.tolist(), "f(x)": y_vals, "F(x)": cum_int.tolist()}

    def convergence_study(self, method: str, a: float, b: float, n_list: List[int]) -> List[Dict]:
        """Runs an n-stepping convergence order analysis."""
        exact = self._get_exact(a, b)
        results = []
        
        for n in n_list:
            res = self.execute_method(method, a, b, n=n)
            if res["Status"] == "Success" and exact is not None:
                err = res["Absolute Error"]
                results.append({"n": n, "h": (b-a)/n, "Approx": res["Approximation"], "Error": err})
                
        # Estimate p
        for i in range(1, len(results)):
            h1, h2 = results[i-1]["h"], results[i]["h"]
            e1, e2 = results[i-1]["Error"], results[i]["Error"]
            if e1 > 0 and e2 > 0 and h1 != h2:
                results[i]["Observed Order p"] = math.log(e1/e2) / math.log(h1/h2)
            else:
                results[i]["Observed Order p"] = "N/A"
        return results
