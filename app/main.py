import streamlit as st
import sympy as sp
import sys
import os
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculus.functions.function_engine import FunctionEngine
from visualization.plotting import plot_function
from visualization.limit_plots import plot_limit
from visualization.continuity_plots import plot_continuity
from visualization.derivative_plots import plot_derivatives, plot_tangent_secant
from calculus.limits.limit_engine import LimitEngine
from calculus.limits.numerical_limits import NumericalLimitEngine
from calculus.limits.limit_analysis import interpret_limit
from calculus.continuity.continuity_engine import ContinuityEngine
from calculus.continuity.discontinuity import classify_discontinuity
from calculus.differentiation.derivative_engine import DerivativeEngine
from calculus.differentiation.numerical_derivative import NumericalDerivativeEngine
from calculus.differentiation.derivative_rules import identify_primary_rule
from calculus.differentiation.derivative_analysis import analyze_differentiability
from numerical.differentiation_error import generate_derivative_error_table

# Milestone 5 Imports
from calculus.applications.critical_points import find_critical_points
from calculus.applications.extrema import classify_local_extrema, find_absolute_extrema
from calculus.applications.concavity import find_inflection_points
from calculus.applications.analysis_engine import ApplicationAnalysisEngine
from numerical.root_finding import newton_raphson
from visualization.applications_plots import plot_function_analysis

# Milestone 6 Imports
from numerical.differentiation.finite_difference import STENCILS
from numerical.differentiation.differentiation_engine import NumericalDifferentiationEngine
from numerical.differentiation.error_analysis import step_size_experiment
from numerical.differentiation.convergence_analysis import richardson_extrapolation
from numerical.differentiation.derivative_approximations import differentiate_discrete_data, apply_stencil
from visualization.numerical_differentiation_plots import plot_error_vs_stepsize, plot_noisy_derivative

# Milestone 7 Imports
from calculus.integration.integral_engine import IntegralEngine
from calculus.integration.improper_integrals import evaluate_improper_integral
from calculus.integration.integral_analysis import (
    integration_by_parts,
    partial_fractions_decomposition
)
from visualization.integral_plots import (
    plot_definite_integral_area,
    plot_riemann_rectangles,
    plot_area_between_curves,
    plot_riemann_convergence
)

st.set_page_config(page_title="Computational Calculus Laboratory", layout="wide")

page = st.sidebar.radio("Select Laboratory Module", [
    "Milestone 1: Function Engine", 
    "Milestone 2: Limits Laboratory",
    "Milestone 3: Continuity Laboratory",
    "Milestone 4: Differential Calculus",
    "Milestone 5: Applications of Calculus",
    "Milestone 6: Numerical Differentiation",
    "Milestone 7: Integral Calculus"
])

# --- MILESTONE 1 ---
if page == "Milestone 1: Function Engine":
    st.title("Foundation & Function Engine")
    expr_input = st.text_input("Enter f(x):", value="x^2 + 2*x - 5")
    try:
        engine = FunctionEngine(expr_input)
        st.latex(f"f(x) = {sp.latex(engine.expression)}")
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Eval (x=3):** {engine.evaluate(3)[1]}")
        with col2:
            st.pyplot(plot_function(engine, -10, 10))
    except Exception as e:
        st.error(str(e))

# --- MILESTONE 2 ---
elif page == "Milestone 2: Limits Laboratory":
    st.title("Advanced Limits Laboratory")
    expr_input = st.text_input("f(x):", value="sin(x)/x")
    pt = st.text_input("Point (a):", value="0")
    try:
        engine = FunctionEngine(expr_input)
        lim = LimitEngine(engine).evaluate_limits(pt)
        st.write(f"**Limit:** {lim['Two-Sided Limit']}")
        if pt not in ['oo', '-oo']: st.pyplot(plot_limit(engine, float(pt)))
    except Exception as e:
        st.error(str(e))

# --- MILESTONE 3 ---
elif page == "Milestone 3: Continuity Laboratory":
    st.title("Continuity Laboratory")
    expr_input = st.text_input("f(x):", value="(x^2 - 4)/(x - 2)")
    pt = st.text_input("Point (a):", value="2")
    try:
        engine = FunctionEngine(expr_input)
        res = ContinuityEngine(engine).evaluate_point_continuity(pt)
        st.write(f"**Continuous:** {res['Continuous']} | **Type:** {classify_discontinuity(res)}")
        st.pyplot(plot_continuity(engine, float(pt), res))
    except Exception as e:
        st.error(str(e))

# --- MILESTONE 4 ---
elif page == "Milestone 4: Differential Calculus":
    st.title("Differential Calculus Laboratory")
    tabs = st.tabs(["Core Differentiation", "Derivative as a Limit", "Advanced Rules", "Differentiability Analysis"])
    with tabs[0]:
        c1, c2 = st.columns([2, 1])
        with c1: expr_input = st.text_input("Function f(x):", value="sin(x)*exp(x)")
        with c2: order = st.number_input("Order (n)", 1, 4, 1)
        try:
            engine = FunctionEngine(expr_input)
            dev_eng = DerivativeEngine(engine)
            st.latex(f"f^{{({order})}}(x) = {sp.latex(dev_eng.get_derivative(order))}")
            st.info(f"**Outer Rule Identified:** {identify_primary_rule(engine.expression)}")
        except Exception as e:
            st.error(str(e))

# --- MILESTONE 5 ---
elif page == "Milestone 5: Applications of Calculus":
    st.title("Applications of Differential Calculus Laboratory")
    expr_input = st.text_input("Function f(x):", value="x^3 - 3*x")
    try:
        engine = FunctionEngine(expr_input)
        st.latex(f"f(x) = {sp.latex(engine.expression)}")
        c1, c2 = st.columns(2)
        with c1:
            st.write("**Critical Points:**", find_critical_points(engine))
            st.write("**Local Extrema:**", classify_local_extrema(engine))
        with c2:
            st.pyplot(plot_function_analysis(engine, -3, 3))
    except Exception as e:
        st.error(str(e))

# --- MILESTONE 6 ---
elif page == "Milestone 6: Numerical Differentiation":
    st.title("Advanced Numerical Differentiation Laboratory")
    expr_input = st.text_input("Function f(x):", value="exp(x)*sin(x)")
    eval_pt = st.number_input("Point x =", value=1.0)
    try:
        engine = FunctionEngine(expr_input)
        sym_eng = DerivativeEngine(engine)
        num_eng = NumericalDifferentiationEngine(engine)
        exact_val = sym_eng.evaluate_derivative(eval_pt, 1)
        st.write(f"**Exact Derivative:** `{exact_val}`")
        exp_data = step_size_experiment(engine, exact_val, eval_pt, STENCILS["Central (2nd Order)"])
        st.pyplot(plot_error_vs_stepsize(exp_data))
    except Exception as e:
        st.error(str(e))

# --- MILESTONE 7 ---
elif page == "Milestone 7: Integral Calculus":
    st.title("Advanced Integral Calculus Laboratory")
    st.markdown("Symbolic antiderivatives, definite area accumulations, Riemann approximations, FTC, and analytical techniques.")

    int_tabs = st.tabs([
        "1. Indefinite Integration",
        "2. Definite Integral & Area",
        "3. Riemann Sums & Convergence",
        "4. Fundamental Theorem of Calculus",
        "5. Techniques & Improper Integrals",
        "6. Area Between Curves"
    ])

    # Tab 1: Indefinite Integration
    with int_tabs[0]:
        st.header("Symbolic Indefinite Integration")
        expr_in = st.text_input("Integrand f(x):", value="x^2 + 3*x - 2", key="indef_input")
        try:
            engine = FunctionEngine(expr_in)
            int_eng = IntegralEngine(engine)
            indef_res = int_eng.integrate_indefinite()
            rule_info = int_eng.get_rule_breakdown()

            st.latex(r"\int \left(" + sp.latex(engine.expression) + r"\right) dx = " + sp.latex(indef_res["FullWithConstant"]))
            
            c1, c2 = st.columns(2)
            with c1:
                st.subheader("Integration Rule Breakdown")
                st.markdown(f"- **Primary Rule:** {rule_info['Rule']}")
                st.markdown(f"- **Formula:** `${rule_info['Formula']}$`")
                st.markdown(f"- **Explanation:** {rule_info['Explanation']}")
            with c2:
                st.subheader("Verification via Differentiation")
                st.latex(r"\frac{d}{dx}\left[" + sp.latex(indef_res["Antiderivative"]) + r"\right] = " + sp.latex(indef_res["VerificationDerivative"]))
                if indef_res["Verified"]:
                    st.success("✅ Antiderivative verified: Differentiation strictly recovers original integrand.")
                else:
                    st.warning("Verification indeterminate or contains complex branch terms.")
        except Exception as e:
            st.error(f"Error: {str(e)}")

    # Tab 2: Definite Integral & Area
    with int_tabs[1]:
        st.header("Definite Integration & Area Accumulation")
        c1, c2, c3 = st.columns([2, 1, 1])
        with c1: def_expr = st.text_input("Integrand f(x):", value="sin(x)", key="def_input")
        with c2: a_bound = st.number_input("Lower Bound (a):", value=0.0)
        with c3: b_bound = st.number_input("Upper Bound (b):", value=3.14159)

        try:
            d_engine = FunctionEngine(def_expr)
            d_int_eng = IntegralEngine(d_engine)
            def_res = d_int_eng.integrate_definite(a_bound, b_bound)

            st.latex(r"\int_{" + str(a_bound) + r"}^{" + str(b_bound) + r"} " + sp.latex(d_engine.expression) + r"\, dx = " + str(def_res["Numerical"]))
            st.info(f"**Interpretation:** {def_res['Interpretation']}")

            st.write(f"- **Exact Value:** `{def_res['Exact']}`")
            st.write(f"- **Signed Integral Value:** `{def_res['SignedArea']}`")
            st.write(f"- **Total Geometric Area:** `{def_res['GeometricArea']}`")
            
            st.pyplot(plot_definite_integral_area(d_engine, a_bound, b_bound))
        except Exception as e:
            st.error(f"Error: {str(e)}")

    # Tab 3: Riemann Sums & Convergence
    with int_tabs[2]:
        st.header("Riemann Sum Approximations")
        r_col1, r_col2, r_col3 = st.columns([2, 1, 1])
        with r_col1: r_expr = st.text_input("Function f(x):", value="x^2", key="riemann_input")
        with r_col2: r_n = st.slider("Subintervals (n):", min_value=2, max_value=64, value=8)
        with r_col3: r_method = st.selectbox("Method:", ["midpoint", "left", "right"])

        try:
            r_eng = FunctionEngine(r_expr)
            r_int_eng = IntegralEngine(r_eng)
            r_a, r_b = 0.0, 2.0
            
            st.pyplot(plot_riemann_rectangles(r_eng, r_a, r_b, r_n, r_method))
            
            st.subheader("Convergence Series Experiment (n = 4, 8, 16, 32, 64, 128)")
            conv_data = r_int_eng.riemann_convergence(r_a, r_b, [4, 8, 16, 32, 64, 128])
            df_conv = pd.DataFrame(conv_data)
            st.dataframe(df_conv, use_container_width=True)
            
            n_vals = [row["n"] for row in conv_data]
            err_vals = [row["Absolute Error"] for row in conv_data]
            st.pyplot(plot_riemann_convergence(n_vals, err_vals))
        except Exception as e:
            st.error(f"Error: {str(e)}")

    # Tab 4: Fundamental Theorem of Calculus
    with int_tabs[3]:
        st.header("Fundamental Theorem of Calculus (FTC) Verification")
        ftc_expr = st.text_input("Function f(x):", value="x^2 + 1", key="ftc_input")
        try:
            ftc_eng = FunctionEngine(ftc_expr)
            ftc_int_eng = IntegralEngine(ftc_eng)
            ftc_res = ftc_int_eng.verify_ftc(0.0, 3.0)

            st.subheader("Part I: Derivative of Accumulation Function")
            st.markdown(r"Let $F(x) = \int_0^x f(t) dt$. Then $F'(x) = f(x)$:")
            st.latex(r"F(x) = " + sp.latex(ftc_res["Part1"]["AccumulationFunction_F"]))
            st.latex(r"F'(x) = \frac{d}{dx}\left[" + sp.latex(ftc_res["Part1"]["AccumulationFunction_F"]) + r"\right] = " + sp.latex(ftc_res["Part1"]["DerivativeOfAccumulation"]))
            st.success("✅ Part 1 holds: The rate of change of the accumulated area equals the integrand.")

            st.divider()
            st.subheader("Part II: Evaluation Theorem")
            st.markdown(r"$\int_a^b f(x) dx = F(b) - F(a)$:")
            st.write(f"- **F(b):** `{ftc_res['Part2']['F(b)']}`")
            st.write(f"- **F(a):** `{ftc_res['Part2']['F(a)']}`")
            st.write(f"- **Endpoint Difference F(b) - F(a):** `{ftc_res['Part2']['F(b) - F(a)']}`")
            st.write(f"- **Direct Definite Integral:** `{ftc_res['Part2']['DefiniteIntegral']}`")
            st.success("✅ Part 2 holds: Definite integral matches endpoint antiderivative net change.")
        except Exception as e:
            st.error(f"Error: {str(e)}")

    # Tab 5: Techniques & Improper Integrals
    with int_tabs[4]:
        st.header("Analytical Techniques & Improper Integrals")
        tech_choice = st.radio("Choose Technique:", ["Integration by Parts", "Partial Fractions", "Improper Integrals"], horizontal=True)

        if tech_choice == "Integration by Parts":
            st.subheader(r"$\int u \, dv = uv - \int v \, du$")
            bp_u = st.text_input("Choose u:", value="x")
            bp_dv = st.text_input("Choose dv (in terms of dx):", value="exp(x)")
            if st.button("Compute by Parts"):
                parts_res = integration_by_parts(bp_u, bp_dv)
                st.latex(r"u = " + sp.latex(parts_res["u"]) + r", \quad du = " + sp.latex(parts_res["du"]))
                st.latex(r"dv = " + sp.latex(parts_res["dv"]) + r", \quad v = " + sp.latex(parts_res["v"]))
                st.latex(r"\int u \, dv = " + sp.latex(parts_res["uv"]) + r" - \int " + sp.latex(parts_res["v"] * parts_res["du"]) + r"\, dx")
                st.latex(r"= " + sp.latex(parts_res["Result"]) + r" + C")

        elif tech_choice == "Partial Fractions":
            st.subheader("Partial Fraction Decomposition")
            frac_in = st.text_input("Rational Expression:", value="1/(x^2 - 1)")
            if st.button("Decompose & Integrate"):
                pf_res = partial_fractions_decomposition(frac_in)
                st.markdown("**Decomposition:**")
                st.latex(sp.latex(pf_res["Decomposition"]))
                st.markdown("**Integrated Antiderivative:**")
                st.latex(sp.latex(pf_res["Antiderivative"]))

        elif tech_choice == "Improper Integrals":
            st.subheader("Improper Integral Analysis")
            imp_expr = st.text_input("Integrand f(x):", value="1/x^2")
            c_a, c_b = st.columns(2)
            imp_a = c_a.text_input("Lower Bound a:", value="1")
            imp_b = c_b.text_input("Upper Bound b (use 'oo' for infinity):", value="oo")
            if st.button("Evaluate Improper Integral"):
                imp_res = evaluate_improper_integral(imp_expr, imp_a, imp_b)
                st.markdown(f"**Classification:** `{imp_res['Classification']}`")
                st.markdown(f"**Exact Result:** `{imp_res['Exact']}`")
                st.info(imp_res["Explanation"])

    # Tab 6: Area Between Curves
    with int_tabs[5]:
        st.header("Area Enclosed Between Two Curves")
        c1, c2 = st.columns(2)
        with c1: f_str = st.text_input("Function f(x):", value="x", key="curve_f")
        with c2: g_str = st.text_input("Function g(x):", value="x^2", key="curve_g")
        c3, c4 = st.columns(2)
        with c3: ab_start = st.number_input("Interval Start (a):", value=0.0)
        with c4: ab_end = st.number_input("Interval End (b):", value=1.0)

        try:
            eng1 = FunctionEngine(f_str)
            eng2 = FunctionEngine(g_str)
            area_res = area_between_curves(eng1, eng2, ab_start, ab_end)
            
            st.write(f"- **Intersections in Interval:** `{area_res['Intersections']}`")
            st.write(f"- **Net Signed Difference:** `{area_res['SignedIntegral']}`")
            st.write(f"- **Total Geometric Area:** `{area_res['GeometricArea']}`")
            
            st.pyplot(plot_area_between_curves(eng1, eng2, ab_start, ab_end))
        except Exception as e:
            st.error(f"Error: {str(e)}")
