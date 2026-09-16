import sympy as sp
from typing import Dict, Any, Tuple

def analyze_2d_region(x_bounds: Tuple[Any, Any], y_bounds: Tuple[Any, Any], x_var: sp.Symbol, y_var: sp.Symbol) -> Dict[str, Any]:
    """Analyzes the integration region (rectangular, x-simple, or y-simple)."""
    x_lower, x_upper = sp.sympify(x_bounds[0]), sp.sympify(x_bounds[1])
    y_lower, y_upper = sp.sympify(y_bounds[0]), sp.sympify(y_bounds[1])
    
    is_x_constant = x_lower.is_number and x_upper.is_number
    is_y_constant = y_lower.is_number and y_upper.is_number
    
    if is_x_constant and is_y_constant:
        region_type = "Rectangular Region"
    elif is_x_constant and not is_y_constant:
        region_type = "y-simple Region (Type I: y bounded by functions of x)"
    elif is_y_constant and not is_x_constant:
        region_type = "x-simple Region (Type II: x bounded by functions of y)"
    else:
        region_type = "Complex Region (Both bounds variable - potentially invalid standard order)"
        
    return {
        "Type": region_type,
        "x_bounds": (x_lower, x_upper),
        "y_bounds": (y_lower, y_upper),
        "x_constant": is_x_constant,
        "y_constant": is_y_constant
    }
