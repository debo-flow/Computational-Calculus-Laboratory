import sympy as sp
from typing import List, Dict
from calculus.sequences.sequence_engine import SequenceEngine

def calculate_partial_sums(engine: SequenceEngine, count: int) -> List[Dict]:
    """S_N = sum(a_n) from 1 to N"""
    results = []
    current_sum = 0.0
    
    for i in range(1, count + 1):
        term = engine.expression.subs(engine.n, i).evalf()
        if term.is_real:
            current_sum += float(term)
            results.append({"n": i, "a_n": float(term), "S_n (Partial Sum)": current_sum})
        else:
            break
    return results
