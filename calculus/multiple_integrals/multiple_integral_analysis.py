import numpy as np
import sympy as sp
from typing import Dict, Any, List
from calculus.multivariable.multivariable_engine import MultivariableEngine
from numerical.validation import calculate_absolute_error, calculate_relative_error

def monte_carlo_double_integral(engine: MultivariableEngine, x_bnds: Tuple[float, float], y_bnds: Tuple[float, float], N: int = 10000) -> Dict[str, Any]:
    """
    Estimates ∫∫_D f(x,y) dA using Monte Carlo stochastic sampling.
    Area(D) = (x_max - x_min) * (y_max - y_min)
    I ≈ Area(D) * average(f(x_i, y_i))
    """
    x_min, x_max = float(x_bnds[0]), float(x_bnds[1])
    y_min, y_max = float(y_bnds[0]), float(y_bnds[1])
    area_D = (x_max - x_min) * (y_max - y_min)
    
    # Generate uniform random points
    np.random.seed(42) # For reproducible experiments
    x_samples = np.random.uniform(x_min, x_max, N)
    y_samples = np.random.uniform(y_min, y_max, N)
    
    f_lam = sp.lambdify(engine.vars, engine.expression, modules=['numpy'])
    f_evals = f_lam(x_samples, y_samples)
    
    # Filter invalid evaluations (NaNs)
    valid_evals = f_evals[~np.isnan(f_evals) & ~np.isinf(f_evals)]
    valid_N = len(valid_evals)
    
    if valid_N == 0:
        return {"Status": "Failed", "Error": "All sampled points evaluated to undefined values."}
        
    mean_f = np.mean(valid_evals)
    variance_f = np.var(valid_evals)
    
    integral_estimate = area_D * mean_f
    standard_error = area_D * np.sqrt(variance_f / valid_N)
    
    return {
        "Status": "Success",
        "Samples (N)": valid_N,
        "Estimate": integral_estimate,
        "Statistical Uncertainty": standard_error,
        "x_samples": x_samples[:1000], # Return subset for plotting
        "y_samples": y_samples[:1000]
    }

def monte_carlo_convergence_study(engine: MultivariableEngine, x_bnds: Tuple[float, float], y_bnds: Tuple[float, float], exact_val: float) -> List[Dict]:
    """Demonstrates the slow O(1/sqrt(N)) convergence of Monte Carlo integration."""
    results = []
    for power in [2, 3, 4, 5, 6]:
        N = 10**power
        mc_res = monte_carlo_double_integral(engine, x_bnds, y_bnds, N=N)
        if mc_res["Status"] == "Success":
            est = mc_res["Estimate"]
            results.append({
                "N": N,
                "Estimate": est,
                "Abs Error": calculate_absolute_error(exact_val, est),
                "Rel Error": calculate_relative_error(exact_val, est),
                "Uncertainty": mc_res["Statistical Uncertainty"]
            })
    return results
