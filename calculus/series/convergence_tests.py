import sympy as sp
from calculus.sequences.sequence_engine import SequenceEngine

def ratio_test(engine: SequenceEngine) -> dict:
    """L = lim (n->oo) |a_{n+1} / a_n|"""
    n = engine.n
    a_n = engine.expression
    a_n1 = a_n.subs(n, n + 1)
    
    try:
        ratio = sp.simplify(sp.Abs(a_n1 / a_n))
        L = sp.limit(ratio, n, sp.oo)
        
        if L < 1: cls = "Absolutely Convergent"
        elif L > 1 or L == sp.oo: cls = "Divergent"
        else: cls = "Inconclusive"
        
        return {"Limit L": L, "Classification": cls}
    except:
        return {"Limit L": "Error", "Classification": "Inconclusive"}

def root_test(engine: SequenceEngine) -> dict:
    """L = lim (n->oo) |a_n|^(1/n)"""
    n = engine.n
    try:
        root_expr = sp.Abs(engine.expression)**(1/n)
        L = sp.limit(root_expr, n, sp.oo)
        
        if L < 1: cls = "Absolutely Convergent"
        elif L > 1 or L == sp.oo: cls = "Divergent"
        else: cls = "Inconclusive"
        
        return {"Limit L": L, "Classification": cls}
    except:
        return {"Limit L": "Error", "Classification": "Inconclusive"}

def alternating_series_test(engine: SequenceEngine) -> dict:
    """Checks if b_n -> 0 and decreases, where a_n = (-1)^n b_n"""
    n = engine.n
    b_n = sp.Abs(engine.expression)
    try:
        lim_b = sp.limit(b_n, n, sp.oo)
        if lim_b == 0:
            return {"Condition": "b_n -> 0", "Classification": "Convergent (Conditionally)"}
        return {"Condition": "b_n does not approach 0", "Classification": "Divergent"}
    except:
        return {"Condition": "Unknown", "Classification": "Inconclusive"}
        
def integral_test(engine: SequenceEngine) -> dict:
    """Compares Σ a_n to ∫_1^oo f(x) dx."""
    x = sp.Symbol('x', positive=True)
    f_x = engine.expression.subs(engine.n, x)
    try:
        integral_val = sp.integrate(f_x, (x, 1, sp.oo))
        if integral_val.is_real and not integral_val.has(sp.oo, -sp.oo):
            return {"Integral": integral_val, "Classification": "Convergent"}
        return {"Integral": integral_val, "Classification": "Divergent"}
    except:
        return {"Integral": "Evaluation Failed", "Classification": "Inconclusive"}
