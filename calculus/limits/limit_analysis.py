import sympy as sp
from typing import Dict, Union

def interpret_limit(results: Dict[str, Union[sp.Expr, str]], point: str) -> str:
    """
    Provides a mathematical interpretation of the limit results.
    """
    lhl = results.get('Left-Hand Limit')
    rhl = results.get('Right-Hand Limit')
    tsl = results.get('Two-Sided Limit')

    if tsl == "Does Not Exist":
        if lhl == -sp.oo or rhl == sp.oo or lhl == sp.oo or rhl == -sp.oo:
            return "The two-sided limit does not exist because the function exhibits vertical asymptotic (infinite) behavior with differing signs on each side."
        if lhl != rhl:
            return f"The two-sided limit does not exist because the Left-Hand Limit ({lhl}) does not equal the Right-Hand Limit ({rhl}). This typically indicates a jump discontinuity."
        return "The limit does not exist due to oscillatory or undefined non-convergent behavior."
    
    if tsl == sp.oo or tsl == -sp.oo:
        return f"The limit is infinite ({tsl}). The function grows without bound as x approaches {point}."
        
    return f"The limit exists. The function approaches approximately {tsl} as x approaches {point} from both sides."
