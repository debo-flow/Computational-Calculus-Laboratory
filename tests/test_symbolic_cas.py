import pytest
import sympy as sp
from calculus.symbolic.expression_parser import safe_parse
from calculus.symbolic.algebra import algebraic_manipulate
from calculus.symbolic.equations import solve_equation, solve_inequality
from calculus.symbolic.symbolic_validation import check_equivalence
from calculus.symbolic.symbolic_engine import CASRouter

def test_safe_parser():
    expr = safe_parse("x^2 + 2*x")
    assert sp.simplify(expr - sp.sympify("x**2 + 2*x")) == 0
    with pytest.raises(ValueError):
        safe_parse("import os; os.system('clear')")

def test_algebraic_manipulation():
    expr = safe_parse("(x+1)**2")
    expanded = algebraic_manipulate(expr, "expand")
    assert expanded == sp.sympify("x**2 + 2*x + 1")
    
    factored = algebraic_manipulate(expanded, "factor")
    assert factored == sp.sympify("(x+1)**2")

def test_inequality_solver():
    res = solve_inequality(sp.sympify("x**2 - 4 > 0"))
    assert "Status" in res and res["Status"] == "Success"

def test_symbolic_equivalence():
    expr_a = safe_parse("sin(x)**2 + cos(x)**2")
    expr_b = safe_parse("1")
    res = check_equivalence(expr_a, expr_b)
    assert res["Equivalence"] == "Equivalent"

def test_cas_router_laplacian():
    lap = CASRouter.calculus_route("laplacian", "x**2 + y**2 + z**2", "x, y, z")
    assert lap == 6
