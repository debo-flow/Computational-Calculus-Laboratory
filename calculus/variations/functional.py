import sympy as sp
from typing import Dict

class Functional:
    """Represents a functional J[y] = ∫ F(x, y, y') dx."""
    def __init__(self, f_str: str):
        self.x = sp.Symbol('x', real=True)
        self.y = sp.Function('y')(self.x)
        self.yp = self.y.diff(self.x)
        self.ypp = self.yp.diff(self.x)
        
        # Safe string parsing: map 'yp' to y' and 'ypp' to y''
        clean_str = f_str.replace("y''", "ypp").replace("y'", "yp").replace("^", "**")
        raw_expr = sp.sympify(clean_str)
        
        # Substitute dummy variables with actual function dependencies
        sym_y, sym_yp, sym_ypp = sp.symbols('y yp ypp')
        self.integrand = raw_expr.subs({sym_ypp: self.ypp, sym_yp: self.yp, sym_y: self.y})

    def evaluate_trial_function(self, trial_str: str, a: float, b: float) -> Dict:
        """Evaluates J[y] for a specific trial function y(x)."""
        trial_func = sp.sympify(trial_str.replace("^", "**"))
        trial_yp = sp.diff(trial_func, self.x)
        
        eval_integrand = self.integrand.subs({self.y: trial_func, self.yp: trial_yp}).doit()
        
        try:
            exact_val = sp.integrate(eval_integrand, (self.x, a, b))
            num_val = float(exact_val.evalf()) if exact_val.is_real else "Complex/Undefined"
            return {"Trial y(x)": trial_func, "Evaluated Integrand": eval_integrand, "Exact J": exact_val, "Numerical J": num_val}
        except Exception as e:
            return {"Error": str(e)}
