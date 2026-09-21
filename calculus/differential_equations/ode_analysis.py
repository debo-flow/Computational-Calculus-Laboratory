import sympy as sp

def classify_single_ode(eq_str: str, func_name: str = 'y', var_name: str = 'x') -> dict:
    """Classifies a symbolic ODE (Order, Linearity, Homogeneity)."""
    x = sp.Symbol(var_name, real=True)
    y = sp.Function(func_name)(x)
    
    # Parse equation: support "y'' + y = 0" or just "y'' + y"
    eq_parts = eq_str.split('=')
    lhs = sp.sympify(eq_parts[0])
    rhs = sp.sympify(eq_parts[1]) if len(eq_parts) > 1 else sp.S.Zero
    ode_expr = lhs - rhs
    
    try:
        classifications = sp.classify_ode(sp.Eq(ode_expr, 0), y)
        order = sp.ode_order(ode_expr, y)
        return {
            "Equation": sp.Eq(ode_expr, 0),
            "Order": order,
            "Classifications": classifications,
            "Is Autonomous": not ode_expr.has(x)
        }
    except Exception as e:
        return {"Error": f"Classification failed: {e}"}
