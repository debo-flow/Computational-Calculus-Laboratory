import sympy as sp
from .sequence_engine import SequenceEngine
from .convergence import analyze_sequence_limit

def analyze_monotonicity(engine: SequenceEngine) -> str:
    """Uses the continuous derivative extension to prove eventual monotonicity."""
    x = sp.Symbol('x', positive=True)
    f_x = engine.expression.subs(engine.n, x)
    
    try:
        f_prime = sp.diff(f_x, x)
        lim_prime = sp.limit(f_prime, x, sp.oo)
        
        if lim_prime > 0: return "Eventually Strictly Increasing"
        if lim_prime < 0: return "Eventually Strictly Decreasing"
        if lim_prime == 0: return "Eventually Constant or Asymptotically Flat"
    except:
        pass
    return "Monotonicity requires further analysis (likely oscillatory or complex)"

def analyze_boundedness(engine: SequenceEngine) -> str:
    """Deduces boundedness from convergence status."""
    lim_res = analyze_sequence_limit(engine)
    if lim_res["Classification"] == "Convergent":
        return "Bounded (All convergent sequences are bounded)"
    elif lim_res["Classification"] == "Divergent to +∞":
        return "Bounded below, Unbounded above"
    elif lim_res["Classification"] == "Divergent to -∞":
        return "Bounded above, Unbounded below"
    return "Unbounded or Oscillatory"
