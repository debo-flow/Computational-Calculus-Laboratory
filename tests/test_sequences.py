import pytest
import sympy as sp
from calculus.sequences.sequence_engine import SequenceEngine
from calculus.sequences.convergence import analyze_sequence_limit
from calculus.sequences.sequence_analysis import analyze_monotonicity

def test_sequence_generation():
    engine = SequenceEngine("1/n")
    terms = engine.generate_terms(1, 3)
    assert terms[0]["a_n (Exact)"] == 1
    assert terms[1]["a_n (Exact)"] == sp.Rational(1, 2)

def test_sequence_limit():
    engine = SequenceEngine("(2*n + 1)/(n + 3)")
    res = analyze_sequence_limit(engine)
    assert res["Classification"] == "Convergent"
    assert res["Limit"] == 2

def test_monotonicity():
    engine = SequenceEngine("1/n")
    assert "Decreasing" in analyze_monotonicity(engine)
