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

st.set_page_config(page_title="Computational Calculus Laboratory", layout="wide")

page = st.sidebar.radio("Select Laboratory Module", [
    "Milestone 1: Function Engine", 
    "Milestone 2: Limits Laboratory",
    "Milestone 3: Continuity Laboratory",
    "Milestone 4: Differential Calculus"
])

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

elif page == "Milestone 4: Differential Calculus":
    st.title("Differential Calculus Laboratory")
    st.markdown("Analyze symbolic derivatives, tangent limits, numerical errors, and differentiability.")
    
    tabs = st.tabs(["Core Differentiation", "Derivative as a Limit", "Advanced Rules", "Differentiability Analysis"])
    
    with tabs[0]:
        st.header("Symbolic & Numerical Differentiation")
        c1, c2 = st.columns([2,1])
        with c1: expr_input = st.text_input("Function f(x):", value="sin(x)*exp(x)")
        with c2: order = st.number_input("Derivative Order (n)", 1, 4, 1)
        
        try:
            engine = FunctionEngine(expr_input)
            dev_eng = DerivativeEngine(engine)
            
            f_expr = engine.expression
            df_expr = dev_eng.get_derivative(order)
            
            st.latex(f"f(x) = {sp.latex(f_expr)}")
            st.latex(f"f^{{({order})}}(x) = {sp.latex(df_expr)}")
            
            st.info(f"**Outer Rule Identified:** {identify_primary_rule(f_expr)}")
            
            st.divider()
            c3, c4 = st.columns(2)
            with c3:
                eval_pt = st.number_input("Evaluate at x =", value=0.0)
                exact_val = dev_eng.evaluate_derivative(eval_pt, order)
                st.write(f"**Exact Derivative at x={eval_pt}:** `{exact_val}`")
                
                if order == 1:
                    num_eng = NumericalDerivativeEngine(engine)
                    st.write("**Numerical Approximations (h=1e-5):**")
                    st.json(num_eng.evaluate_all(eval_pt))
            with c4:
                plot_order = [0, 1] if order == 1 else [0, 1, 2]
                st.pyplot(plot_derivatives(engine, eval_pt-3, eval_pt+3, plot_order))
                
            if order == 1 and isinstance(exact_val, float):
                st.divider()
                st.subheader("Numerical Instability & Error Analysis")
                st.markdown("Observe how reducing `h` too much causes floating-point cancellation errors.")
                err_table = generate_derivative_error_table(engine, eval_pt)
                st.dataframe(pd.DataFrame(err_table), use_container_width=True)
                
        except Exception as e:
            st.error(f"Error: {str(e)}")

    with tabs[1]:
        st.header("Geometric Interpretation: Secant to Tangent")
        try:
            lim_c1, lim_c2 = st.columns(2)
            a_val = lim_c1.number_input("Point a", value=1.0, key='lim_a')
            h_val = lim_c2.slider("Difference h", -2.0, 2.0, 1.0, step=0.01)
            
            st.pyplot(plot_tangent_secant(engine, a_val, h_val))
            st.markdown(r"The derivative is defined as: $f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$")
        except Exception as e:
            st.error("Select valid function in Core tab.")
            
    with tabs[2]:
        st.header("Implicit & Parametric Differentiation")
        st.subheader("Implicit Differentiation")
        imp_eq = st.text_input("Equation (e.g. x^2 + y^2 = 25):", "x^2 + y^2 = 25")
        if st.button("Calculate Implicit"):
            res = DerivativeEngine.implicit_differentiation(imp_eq)
            st.latex(r"\frac{dy}{dx} = " + sp.latex(res))
            
        st.subheader("Parametric Differentiation")
        p_c1, p_c2 = st.columns(2)
        with p_c1: x_t = st.text_input("x(t):", "cos(t)")
        with p_c2: y_t = st.text_input("y(t):", "sin(t)")
        if st.button("Calculate Parametric"):
            res = DerivativeEngine.parametric_differentiation(x_t, y_t)
            st.latex(r"\frac{dx}{dt} = " + sp.latex(res['dx/dt']) + r" \quad \frac{dy}{dt} = " + sp.latex(res['dy/dt']))
            st.latex(r"\frac{dy}{dx} = " + sp.latex(res['dy/dx']))

    with tabs[3]:
        st.header("Differentiability vs Continuity")
        diff_expr = st.text_input("Test Function:", "Abs(x)")
        diff_pt = st.number_input("Test Point:", value=0.0)
        if st.button("Analyze Function"):
            test_eng = FunctionEngine(diff_expr)
            res = analyze_differentiability(test_eng, diff_pt)
            
            st.markdown(f"- **Continuous:** {res['Continuous']}")
            st.markdown(f"- **Differentiable:** {res['Differentiable']}")
            st.markdown(f"- **Classification:** {res['Classification']}")
            st.markdown(f"- **LHL Derivative:** {res['Left Derivative']} | **RHL Derivative:** {res['Right Derivative']}")
            if res['Continuous'] and not res['Differentiable']:
                st.warning("Notice: This function is continuous, but not differentiable. Continuity does not guarantee differentiability!")
