import streamlit as st
import sympy as sp
import sys
import os

# Ensure the root directory is in the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculus.functions.function_engine import FunctionEngine
from visualization.plotting import plot_function
from numerical.validation import calculate_absolute_error, calculate_relative_error

st.set_page_config(page_title="Computational Calculus Laboratory", layout="wide")

st.title("Computational Calculus Laboratory")
st.markdown("**Milestone 1 — Mathematical Function Engine & Foundation**")
st.divider()

# --- 1. FUNCTION INPUT ---
st.header("1. Function Input")
expr_input = st.text_input("Enter a mathematical function f(x):", value="x^2 + 2*x - 5")

try:
    engine = FunctionEngine(expr_input)
    
    st.latex(f"f(x) = {sp.latex(engine.expression)}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # --- 2. FUNCTION EVALUATION ---
        st.header("2. Function Evaluation")
        x_val = st.number_input("Enter x value to evaluate:", value=3.0, step=0.5)
        
        exact, num = engine.evaluate(x_val)
        st.markdown(f"**Exact Result:**")
        if isinstance(exact, sp.Expr):
            st.latex(sp.latex(exact))
        else:
            st.write(exact)
            
        st.markdown(f"**Numerical Approximation:** `{num}`")
        
        # --- 3. SYMBOLIC REPRESENTATION ---
        st.header("3. Function Simplification")
        forms = engine.get_symbolic_representations()
        for name, expr in forms.items():
            if name != "Original":
                st.markdown(f"**{name}:**")
                st.latex(sp.latex(expr))

        # --- 6. NUMERICAL INFORMATION ---
        st.header("6. Numerical Information")
        analysis = engine.analyze()
        for key, val in analysis.items():
            if "Exact" in key:
                st.markdown(f"**{key}:**")
                st.latex(val)
            else:
                st.markdown(f"**{key}:** {val}")
                
    with col2:
        # --- 5. FUNCTION PLOT ---
        st.header("5. Function Plot")
        plot_start = st.number_input("Plot start x:", value=-10.0)
        plot_end = st.number_input("Plot end x:", value=10.0)
        
        if plot_start < plot_end:
            fig = plot_function(engine, plot_start, plot_end)
            st.pyplot(fig)
        else:
            st.error("Plot start must be less than plot end.")

    st.divider()
    
    # --- 4. FUNCTION TABLE ---
    st.header("4. Function Table")
    col_t1, col_t2, col_t3 = st.columns(3)
    t_start = col_t1.number_input("Table Start x:", value=-5.0)
    t_end = col_t2.number_input("Table End x:", value=5.0)
    t_step = col_t3.number_input("Step size:", value=1.0, min_value=0.01)
    
    if t_start <= t_end and t_step > 0:
        table_data = engine.generate_table(t_start, t_end, t_step)
        st.dataframe(table_data, use_container_width=True)
        
    st.divider()

    # --- ERROR VALIDATION DEMO ---
    st.header("Error Validation Foundation")
    st.markdown("Demonstration of the numerical validation module comparing an Exact vs Approximation.")
    col_e1, col_e2 = st.columns(2)
    exact_err_val = col_e1.number_input("Simulated Exact Value:", value=3.14159)
    approx_err_val = col_e2.number_input("Simulated Approximation:", value=3.14)
    
    abs_err = calculate_absolute_error(exact_err_val, approx_err_val)
    rel_err = calculate_relative_error(exact_err_val, approx_err_val)
    
    st.markdown(f"- **Absolute Error:** `{abs_err}`")
    st.markdown(f"- **Relative Error:** `{rel_err}`")

except Exception as e:
    st.error(f"Error parsing or evaluating function: {str(e)}")
    st.info("Please ensure your function is a valid mathematical expression using 'x' as the variable (e.g., sin(x), x^2, exp(x)).")

