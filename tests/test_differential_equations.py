from calculus.differential_equations.first_order import solve_exact_equation, solve_linear_first_order
from numerical.ode.bvp_solvers import finite_difference_bvp_linear

def test_exact_equation():
    # 2x + y^2 dx + 2xy dy = 0  => dM/dy = 2y, dN/dx = 2y
    res = solve_exact_equation("2*x + y^2", "2*x*y")
    assert res["Exact"] is True
    assert sp.simplify(res["Potential F(x,y)"] - sp.sympify("x^2 + x*y^2")) == 0

def test_linear_integrating_factor():
    # y' + (2/x)y = x
    res = solve_linear_first_order("2/x", "x")
    assert sp.simplify(res["Integrating Factor mu(x)"] - sp.sympify("x^2")) == 0
    assert sp.simplify(res["General Solution"] - sp.sympify("x^2/4 + C/x^2")) == 0

def test_bvp_finite_difference():
    # y'' = -y -> y'' + 0y' + 1y = 0. Boundary: y(0)=0, y(pi)=0. 
    p = lambda x: 0
    q = lambda x: 1
    r = lambda x: 0
    res = finite_difference_bvp_linear(p, q, r, 0, np.pi/2, 0, 1, n=20)
    assert res["Status"] == "Success"
    assert pytest.approx(res["y"][-1], 0.01) == 1.0 # sin(pi/2) = 1
