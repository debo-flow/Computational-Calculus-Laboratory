import sympy as sp
from .sequence_engine import SequenceEngine

def analyze_sequence_limit(engine: SequenceEngine) -> dict:
    """Evaluates lim (n->oo) a_n to determine sequence convergence."""
    n = engine.n
    try:
        limit_val = sp.limit(engine.expression, n, sp.oo)
        
        if limit_val.has(sp.oo):
            status = "Divergent to +∞"
        elif limit_val.has(-sp.oo):
            status = "Divergent to -∞"
        elif "AccumulationBounds" in str(limit_val) or limit_val.has(sp.zoo, sp.nan):
            status = "Oscillatory / Non-Convergent"
        else:
            status = "Convergent"
            
        return {
            "Limit": limit_val,
            "Classification": status,
            "Interpretation": f"The sequence is {status.lower()}."
        }
    except Exception as e:
        return {"Limit": "Unknown", "Classification": "Unable to determine symbolically", "Interpretation": str(e)}
