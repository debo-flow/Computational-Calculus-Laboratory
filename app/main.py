import streamlit as st
import sympy as sp
import sys
import os
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculus.functions.function_engine import FunctionEngine
from visualization.plotting import plot_function
from visualization.limit_plots import plot_limit
from numerical.validation import calculate_absolute_error, calculate_relative_error
from calculus.limits.limit_engine import LimitEngine
from calculus.limits.numerical_limits import NumericalLimitEngine
from calculus.limits.limit_analysis import interpret_limit

st.set_page_config(page_title="Computational Calculus Laboratory", layout="wide")

# --- NAVIGATION ---
page = st.sidebar.radio("Select Laboratory Module", ["Milestone 1: Function Engine", "Milestone 2: Limits Laboratory"])

if page == "Milestone 1: Function Engine":
    st.title("Foundation & Function Engine")
    st.markdown("Build mathematical expressions, evaluate them, and graph them safely.")
    
    expr_input = st.text_input("Enter a mathematical function f(x):", value="x^2 + 2*x - 5")
    
    try:
        engine = FunctionEngine(expr_input)
        st.latex(f"f(x) = {sp.latex(engine.expression)}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.header("Evaluation")
            x_val = st.number_input("Enter x value:", value=3.0)
            exact, num = engine.evaluate(x_val)
            st.write(f"**Exact:** {exact} | **Numerical:** {num}")
            
            st.header("Simplification")
            for name, expr in engine.get_symbolic_representations().items():
                if name != "Original":
                    st.markdown(f"**{name}:**")
                    st.latex(sp.latex(expr))
                    
        with col2:
            st.header("Visualization")
            fig = plot_function(engine, -10, 10)
            st.pyplot(fig)
            
    except Exception as e:
        st.error(f"Error: {str(e)}")

elif page == "Milestone 2: Limits Laboratory":
    st.title("Advanced Limits Laboratory")
    st.markdown("Analyze symbolic limits, explore one-sided limits numerically, and evaluate limits at infinity.")
    
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        expr_input = st.text_input("1. Limit Expression f(x):", value="(x^2 - 1)/(x - 1)")
    with col2:
        point_input = st.text_input("2. Limit Point (a):", value="1", help="Use 'oo' for infinity or '-oo' for negative infinity")
    with col3:
        precision = st.slider("Refinement Steps", min_value=3, max_value=8, value=5)

    try:
        engine = FunctionEngine(expr_input)
        st.latex(r"\lim_{x \to " + point_input + r"} " + sp.latex(engine.expression))
        
        # Initialize Limit Engines
        lim_engine = LimitEngine(engine)
        num_engine = NumericalLimitEngine(engine)
        
        # --- SYMBOLIC RESULTS ---
        st.header("4. Symbolic Results")
        results = lim_engine.evaluate_limits(point_input)
        
        res_c1, res_c2, res_c3 = st.columns(3)
        res_c1.metric("Left-Hand Limit", str(results.get('Left-Hand Limit', 'N/A')))
        res_c2.metric("Right-Hand Limit", str(results.get('Right-Hand Limit', 'N/A')))
        res_c3.metric("Two-Sided Limit", str(results.get('Two-Sided Limit', 'N/A')))
        
        st.info(f"**Mathematical Interpretation:** {interpret_limit(results, point_input)}")
        
        # --- NUMERICAL CONVERGENCE & VISUALIZATION ---
        st.divider()
        col_viz, col_tab = st.columns(2)
        
        with col_viz:
            st.header("7. Graph Visualization")
            if point_input not in ['oo', '-oo']:
                pt = float(point_input)
                fig = plot_limit(engine, pt, span=3.0)
                st.pyplot(fig)
            else:
                st.warning("Visualization is currently optimized for finite limits. Use standard plotter for infinity.")
                
        with col_tab:
            st.header("6. Numerical Convergence Table")
            
            if point_input in ['oo', '-oo']:
                is_pos = (point_input == 'oo')
                tab_data = num_engine.generate_infinity_table(positive_infinity=is_pos, steps=precision)
                st.dataframe(pd.DataFrame(tab_data), use_container_width=True)
            else:
                pt = float(point_input)
                tables = num_engine.generate_convergence_table(pt, steps=precision)
                
                st.markdown("**Approaching from the Left (LHL):**")
                st.dataframe(pd.DataFrame(tables['left']), use_container_width=True)
                
                st.markdown("**Approaching from the Right (RHL):**")
                st.dataframe(pd.DataFrame(tables['right']), use_container_width=True)
                
        # --- ERROR ANALYSIS ---
        st.divider()
        st.header("8. Error Analysis & Verification")
        st.markdown("Compare the highest precision numerical approximation against the symbolic result (if finite).")
        
        exact_lim = results.get('Two-Sided Limit')
        if exact_lim != "Does Not Exist" and exact_lim.is_real:
            # Get last numeric value from table
            if point_input in ['oo', '-oo']:
                approx_val = tab_data[-1]["f(x)"]
            else:
                approx_val = tables['right'][-1]["f(x)"]
                
            if isinstance(approx_val, float):
                exact_float = float(exact_lim.evalf())
                abs_e = calculate_absolute_error(exact_float, approx_val)
                rel_e = calculate_relative_error(exact_float, approx_val)
                
                st.markdown(f"- **Exact Value:** `{exact_float}`")
                st.markdown(f"- **Final Approximation:** `{approx_val}`")
                st.markdown(f"- **Absolute Error:** `{abs_e}`")
                st.markdown(f"- **Relative Error:** `{rel_e}`")
        else:
            st.markdown("*Error analysis is only available for existing, finite limits.*")

    except Exception as e:
        st.error(f"Error processing limit: {str(e)}")
