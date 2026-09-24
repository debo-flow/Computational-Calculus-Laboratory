import sympy as sp
import numpy as np
from typing import Dict, Any

def create_numerical_system(exprs: list, vars_str: str):
    variables = sp.symbols(vars_str)
    t = sp.Symbol('t')
    lambdified = [sp.lambdify((t, *variables), sp.sympify(e), modules=['numpy']) for e in exprs]
    def f(t_val, Y_val): return np.array([func(t_val, *Y_val) for func in lambdified])
    return f

CLASSIC_MODELS = {
    "Logistic Growth": {"sys": ["r*x * (1 - x/K)"], "vars": "x", "params": ["r", "K"]},
    "Harmonic Oscillator": {"sys": ["y", "-omega**2 * x"], "vars": "x, y", "params": ["omega"]},
    "Damped Oscillator": {"sys": ["y", "-2*gamma*y - omega**2 * x"], "vars": "x, y", "params": ["gamma", "omega"]},
    "Predator-Prey (Lotka-Volterra)": {"sys": ["alpha*x - beta*x*y", "delta*x*y - gamma*y"], "vars": "x, y", "params": ["alpha", "beta", "delta", "gamma"]}
}
