import pytest
import sympy as sp
from calculus.sequences.sequence_engine import SequenceEngine
from calculus.series.series_engine import SeriesEngine
from calculus.series.divergence_tests import nth_term_test
from calculus.series.convergence_tests import ratio_test, alternating_series_test

def test_nth_term_divergence():
    engine = SequenceEngine("n/(n+1)")
    res = nth_term_test(engine)
    assert res["Classification"] == "Divergent"
    assert res["Limit"] == 1

def test_ratio_test_convergent():
    engine = SequenceEngine("1/factorial(n)")
    res = ratio_test(engine)
    assert res["Classification"] == "Absolutely Convergent"
    assert res["Limit L"] == 0

def test_alternating_harmonic():
    engine = SequenceEngine("(-1)**n / n")
    res = alternating_series_test(engine)
    assert "Convergent" in res["Classification"]

