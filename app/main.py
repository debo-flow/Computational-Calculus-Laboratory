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
from numerical.validation import calculate_absolute_error, calculate_relative_error
from calculus.limits.limit_engine import LimitEngine
from calculus.limits.numerical_limits import NumericalLimitEngine
from calculus.limits.limit_analysis import interpret_limit
from calculus.continuity.continuity_engine import ContinuityEngine
from calculus.continuity.discontinuity import classify_discontinuity
from calculus.continuity.continuity_analysis import generate_continuity_interpretation

st.set_page_config(page_title="Computational Calculus Laboratory", layout="wide")

page = st.sidebar.radio("Select Laboratory Module", [
    "Milestone 1: Function Engine", 
    "Milestone 2: Limits Laboratory",
    "Milestone 3: Continuity Laboratory"
])

if page == "Milestone 1: Function Engine":
    st.title("Foundation & Function Engine")
    expr_input = st.text_input("Enter a mathematical function f(x):", value="x^2 + 2*x - 5")
    try:
        engine = FunctionEngine(expr_input)
        st.latex(f"f(x) = {sp.latex(engine.expression)}")
        col1, col2 = st.columns(2)
        with col1:
            x_val = st.number_input("Enter x value:", value=3.0)
            exact, num = engine.evaluate(x_val)
            st.write(f"**Exact:** {exact} | **Numerical:** {num}")
            for name, expr in engine.get_symbolic_representations().items():
                if name != "Original":
                    st.markdown(f"**{name}:**")
                    st.latex(sp.latex(expr))
        with col2:
            st.pyplot(plot_function(engine, -10, 10))
    except Exception as e:
        st.error(f"Error: {str(e)}")

elif page == "Milestone 2: Limits Laboratory":
    st.title("Advanced Limits Laboratory")
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1: expr_input = st.text_input("Limit Expression f(x):", value="(x^2 - 1)/(x - 1)")
    with col2: point_input = st.text_input("Limit Point (a):", value="1")
    with col3: precision = st.slider("Refinement Steps", 3, 8, 5)

    try:
        engine = FunctionEngine(expr_input)
        lim_engine = LimitEngine(engine)
        num_engine = NumericalLimitEngine(engine)
        
        st.latex(r"\lim_{x \to " + point_input + r"} " + sp.latex(engine.expression))
        results = lim_engine.evaluate_limits(point_input)
        
        c1, c2, c3 = st.columns(3)
        c1.metric("LHL", str(results.get('Left-Hand Limit', 'N/A')))
        c2.metric("RHL", str(results.get('Right-Hand Limit', 'N/A')))
        c3.metric("Limit", str(results.get('Two-Sided Limit', 'N/A')))
        st.info(f"**Interpretation:** {interpret_limit(results, point_input)}")
        
        if point_input not in ['oo', '-oo']:
            st.pyplot(plot_limit(engine, float(point_input), span=3.0))
    except Exception as e:
        st.error(f"Error: {str(e)}")

elif page == "Milestone 3: Continuity Laboratory":
    st.title("Advanced Continuity Laboratory")
    st.markdown("Analyze mathematical continuity, detect discontinuities, and classify their types.")
    
    st.info("💡 **Hint for Piecewise Functions:** Use SymPy syntax. Example: `Piecewise((x**2, x < 1), (x + 3, True))`")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        expr_input = st.text_input("1. Function Input f(x):", value="(x^2 - 4)/(x - 2)")
    with col2:
        point_input = st.text_input("2. Analysis Point (x = a):", value="2")

    try:
        engine = FunctionEngine(expr_input)
        cont_engine = ContinuityEngine(engine)
        num_engine = NumericalLimitEngine(engine)
        
        st.latex(f"f(x) = {sp.latex(engine.expression)}")
        
        # --- 3 to 9: CONTINUITY CONDITIONS & RESULTS ---
        st.header("Point Continuity Analysis")
        results = cont_engine.evaluate_point_continuity(point_input)
        dis_type = classify_discontinuity(results)
        
        # Continuity Truth Table
        st.markdown("### Limit + Function Value Comparison")
        table_data = {
            "Quantity": ["f(a)", "Left-Hand Limit (LHL)", "Right-Hand Limit (RHL)", "Two-Sided Limit"],
            "Value": [str(results["f(a)"]), str(results["LHL"]), str(results["RHL"]), str(results["Limit"])],
            "Matches f(a)?": [
                "N/A", 
                "✅ YES" if results["Left Continuous"] else "❌ NO",
                "✅ YES" if results["Right Continuous"] else "❌ NO",
                "✅ YES" if results["Continuous"] else "❌ NO"
            ]
        }
        st.table(pd.DataFrame(table_data))
        
        # Classification & Interpretation
        if results["Continuous"]:
            st.success(f"✅ **CONTINUOUS** at x = {point_input}")
        else:
            st.error(f"❌ **DISCONTINUOUS** at x = {point_input} | Type: **{dis_type}**")
            
        st.info(f"**Mathematical Interpretation:** {generate_continuity_interpretation(results)}")

        # --- 10 & 13: NUMERICAL VERIFICATION ---
        st.divider()
        st.header("Numerical Continuity Verification")
        steps = st.slider("Samples / Precision", 3, 7, 5)
        
        num_tables = num_engine.generate_convergence_table(float(point_input), steps=steps)
        t_col1, t_col2 = st.columns(2)
        with t_col1:
            st.markdown("**Left Approach (x → a⁻)**")
            st.dataframe(pd.DataFrame(num_tables['left']), use_container_width=True)
        with t_col2:
            st.markdown("**Right Approach (x → a⁺)**")
            st.dataframe(pd.DataFrame(num_tables['right']), use_container_width=True)

        # --- 11: VISUALIZATION ---
        st.divider()
        st.header("Continuity Visualization")
        fig = plot_continuity(engine, float(point_input), results)
        st.pyplot(fig)

        # --- 7 & 12: INTERVAL ANALYSIS ---
        st.divider()
        st.header("Interval Discontinuity Map")
        st.markdown("Scan an interval `[start, end]` for candidate discontinuity points.")
        i_col1, i_col2 = st.columns(2)
        start_val = i_col1.number_input("Start Interval", value=-10.0)
        end_val = i_col2.number_input("End Interval", value=10.0)
        
        if st.button("Map Discontinuities"):
            sings = cont_engine.find_discontinuities_in_interval(start_val, end_val)
            if isinstance(sings, list) and len(sings) > 0 and not isinstance(sings[0], str):
                st.warning(f"Potential theoretical discontinuities found at: {', '.join([str(s) for s in sings])}")
            elif isinstance(sings, list) and len(sings) > 0 and isinstance(sings[0], str):
                st.info(sings[0])
            else:
                st.success("No theoretical discontinuities found within this interval based on standard domain mapping.")

    except Exception as e:
        st.error(f"Error evaluating continuity: {str(e)}")
