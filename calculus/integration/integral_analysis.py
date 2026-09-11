import sympy as sp
import numpy as np
from typing import Dict, Any, List, Tuple
from calculus.functions.function_engine import FunctionEngine
from calculus.differentiation.derivative_engine import DerivativeEngine

def compute_riemann_sum(engine: FunctionEngine, a: float, b: float, n: int, method: str = 'midpoint') -> Dict[str, Any]:
    """
    Computes Left, Right, or Midpoint Riemann sums:
    S_n = sum_{i=0}^{n-1} f(x_i*) Delta x
    """
    if n <= 0:
        raise ValueError("Number of subintervals n must be positive.")
    if a == b:
        return {"Sum": 0.0, "DeltaX": 0.0, "x_eval": [], "rect_heights": []}

    dx = (b - a) / n
    x_eval = []
    
    for i in range(n):
        if method == 'left':
            xi = a + i * dx
        elif method == 'right':
            xi = a + (i + 1) * dx
        elif method == 'midpoint':
            xi = a + (i + 0.5) * dx
        else:
            raise ValueError(f"Unknown Riemann method: {method}")
        x_eval.append(xi)

    rect_heights = []
    for xi in x_eval:
        _, val = engine.evaluate(xi)
        if isinstance(val, (int, float)):
            rect_heights.append(val)
        else:
            rect_heights.append(0.0)

    approx_sum = sum(rect_heights) * dx

    return {
        "Method": method.capitalize(),
        "n": n,
        "DeltaX": dx,
        "x_eval": x_eval,
        "rect_heights": rect_heights,
        "Approximation": approx_sum
    }

def riemann_convergence_series(engine: FunctionEngine, a: float, b: float, n_list: List[int] = [4, 8, 16, 32, 64, 128]) -> List[Dict[str, Any]]:
    """
    Demonstrates the convergence of Riemann sums toward the exact integral as n -> inf.
    """
    x = engine.x
    exact_sym = sp.integrate(engine.expression, (x, a, b))
    exact_val = float(exact_sym.evalf()) if exact_sym.is_real else None

    table = []
    for n in n_list:
        res = compute_riemann_sum(engine, a, b, n, method='midpoint')
        approx = res["Approximation"]
        
        abs_err = abs(exact_val - approx) if exact_val is not None else "N/A"
        rel_err = (abs_err / abs(exact_val)) if (exact_val is not None and exact_val != 0) else "N/A"
        
        table.append({
            "n": n,
            "Delta x": res["DeltaX"],
            "Approximation": approx,
            "Exact": exact_val,
            "Absolute Error": abs_err,
            "Relative Error": rel_err
        })
    return table

def verify_fundamental_theorem_part1(engine: FunctionEngine, a_val: float = 0.0) -> Dict[str, Any]:
    """
    Verifies FTC Part 1: d/dx [∫_a^x f(t) dt] = f(x).
    """
    x = engine.x
    t = sp.Symbol('t')
    f_t = engine.expression.subs(x, t)
    
    F_x = sp.integrate(f_t, (t, a_val, x))
    dF_dx = sp.diff(F_x, x)
    diff_check = sp.simplify(dF_dx - engine.expression)

    return {
        "OriginalFunction": engine.expression,
        "AccumulationFunction_F": F_x,
        "DerivativeOfAccumulation": dF_dx,
        "IdentityHolds": (diff_check == 0),
        "Explanation": "F'(x) strictly recovers f(x), verifying Part 1 of the Fundamental Theorem."
    }

def verify_fundamental_theorem_part2(engine: FunctionEngine, a: float, b: float) -> Dict[str, Any]:
    """
    Verifies FTC Part 2: ∫_a^b f(x) dx = F(b) - F(a).
    """
    x = engine.x
    F = sp.integrate(engine.expression, x)
    F_b = F.subs(x, b)
    F_a = F.subs(x, a)
    endpoint_diff = sp.simplify(F_b - F_a)
    
    definite_val = sp.integrate(engine.expression, (x, a, b))
    identity_holds = sp.simplify(endpoint_diff - definite_val) == 0

    return {
        "Antiderivative_F": F,
        "F(b)": float(F_b.evalf()),
        "F(a)": float(F_a.evalf()),
        "F(b) - F(a)": float(endpoint_diff.evalf()),
        "DefiniteIntegral": float(definite_val.evalf()),
        "IdentityHolds": identity_holds
    }

def area_between_curves(engine1: FunctionEngine, engine2: FunctionEngine, a: float, b: float) -> Dict[str, Any]:
    """
    Computes the area between f(x) and g(x) over [a, b].
    Identifies intersection points within [a, b] to compute exact geometric area.
    """
    x = engine1.x
    diff_expr = engine1.expression - engine2.expression
    
    # Check intersections
    intersections = []
    try:
        sol = sp.solve(diff_expr, x)
        intersections = [float(s.evalf()) for s in sol if s.is_real and a <= float(s.evalf()) <= b]
        intersections = sorted(list(set(intersections)))
    except Exception:
        pass

    signed_diff = sp.integrate(diff_expr, (x, a, b))
    geom_area = sp.integrate(sp.Abs(diff_expr), (x, a, b))

    return {
        "f(x)": engine1.expression,
        "g(x)": engine2.expression,
        "Intersections": intersections,
        "SignedIntegral": float(signed_diff.evalf()),
        "GeometricArea": float(geom_area.evalf())
    }

def integration_by_parts(u_str: str, dv_str: str) -> Dict[str, Any]:
    """
    Demonstrates ∫ u dv = uv - ∫ v du symbolically.
    """
    x = sp.Symbol('x')
    u = sp.sympify(u_str)
    dv = sp.sympify(dv_str)
    
    du = sp.diff(u, x)
    v = sp.integrate(dv, x)
    v_du = sp.integrate(v * du, x)
    
    final_result = sp.simplify(u * v - v_du)

    return {
        "u": u,
        "dv": dv,
        "du": du,
        "v": v,
        "uv": u * v,
        "Integral_v_du": v_du,
        "Result": final_result
    }

def partial_fractions_decomposition(rational_str: str) -> Dict[str, Any]:
    """
    Decomposes a rational function into partial fractions and integrates each term.
    """
    x = sp.Symbol('x')
    expr = sp.sympify(rational_str)
    decomp = sp.apart(expr, x)
    antiderivative = sp.integrate(decomp, x)

    return {
        "Original": expr,
        "Decomposition": decomp,
        "Antiderivative": antiderivative + sp.Symbol('C')
    }
