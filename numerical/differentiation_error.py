from numerical.validation import calculate_absolute_error, calculate_relative_error
from calculus.differentiation.numerical_derivative import NumericalDerivativeEngine
from calculus.differentiation.derivative_engine import DerivativeEngine
from typing import List, Dict

def generate_derivative_error_table(
    engine, x_val: float, h_values: List[float] = [0.1, 0.01, 0.001, 1e-4, 1e-5, 1e-8, 1e-12]
) -> List[Dict]:
    num_eng = NumericalDerivativeEngine(engine)
    sym_eng = DerivativeEngine(engine)
    
    exact = sym_eng.evaluate_derivative(x_val)
    if isinstance(exact, str):
        return []
        
    table = []
    for h in h_values:
        num_res = num_eng.evaluate_all(x_val, h)["Central"]
        if isinstance(num_res, float):
            table.append({
                "h step": h,
                "Approx (Central)": num_res,
                "Exact": exact,
                "Abs Error": calculate_absolute_error(exact, num_res),
                "Rel Error": calculate_relative_error(exact, num_res)
            })
    return table
