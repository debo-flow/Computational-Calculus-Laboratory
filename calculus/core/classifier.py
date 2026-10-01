import re
from typing import Dict

def classify_problem(input_str: str) -> Dict[str, str]:
    """
    Automatically classifies mathematical input without unsafe execution.
    Returns the target engine and confidence classification.
    """
    input_str = input_str.strip().lower()
    
    # Differential Equations
    if re.search(r"d\^?2?y/dx\^?2?|y''|y'", input_str) and "=" in input_str:
        return {"Type": "Differential Equation", "Engine": "ode", "Confidence": "High"}
    
    # Calculus of Variations (Functionals)
    if re.search(r"j\[y\]|int.*f\(x,y,y'\)", input_str):
        return {"Type": "Variational Functional", "Engine": "variations", "Confidence": "High"}
    
    # Limits
    if "lim" in input_str or "->" in input_str:
        return {"Type": "Limit", "Engine": "limit", "Confidence": "High"}
    
    # Integration
    if "int" in input_str or "integral" in input_str:
        return {"Type": "Integration", "Engine": "integration", "Confidence": "High"}
        
    # Vector Calculus / Multivariable
    if "nabla" in input_str or "curl" in input_str or "div" in input_str:
        return {"Type": "Vector Calculus", "Engine": "vector_calculus", "Confidence": "High"}
        
    if "," in input_str and ("f(x,y)" in input_str or "z=" in input_str):
        return {"Type": "Multivariable Function", "Engine": "multivariable", "Confidence": "Medium"}
        
    # Default to single variable expression
    return {"Type": "Expression / Function", "Engine": "symbolic", "Confidence": "Low"}
