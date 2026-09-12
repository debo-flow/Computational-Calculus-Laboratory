import sympy as sp
from calculus.sequences.sequence_engine import SequenceEngine

def nth_term_test(engine: SequenceEngine) -> dict:
    """Necessary condition: lim a_n == 0."""
    n = engine.n
    try:
        lim = sp.limit(engine.expression, n, sp.oo)
        if lim != 0:
            return {"Limit": lim, "Classification": "Divergent", "Reason": "Limit of terms is not zero."}
        return {"Limit": 0, "Classification": "Inconclusive", "Reason": "a_n -> 0 is necessary but NOT sufficient for series convergence."}
    except:
        return {"Limit": "Unknown", "Classification": "Inconclusive", "Reason": "Limit could not be computed."}
