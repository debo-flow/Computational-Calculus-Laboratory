# ... [Keep Milestones 1 to 5 exactly as they are] ...

elif page == "Milestone 6: Numerical Differentiation":
    st.title("Advanced Numerical Differentiation Laboratory")
    st.markdown("Explore approximation theory, convergence, truncation vs round-off error, and discrete data.")
    
    from numerical.differentiation.finite_difference import STENCILS
    from numerical.differentiation.differentiation_engine import NumericalDifferentiationEngine
    from numerical.differentiation.error_analysis import step_size_experiment
    from numerical.differentiation.convergence_analysis import richardson_extrapolation
    from numerical.differentiation.derivative_approximations import differentiate_discrete_data
    from visualization.numerical_differentiation_plots import plot_error_vs_stepsize, plot_noisy_derivative
    from calculus.differentiation.derivative_engine import DerivativeEngine

    tabs = st.tabs(["Stencils & Reliability", "Error vs Step-Size (h)", "Richardson & Adaptive", "Discrete Data & Noise"])
    
    # Shared Input State for M6
    c1, c2 = st.columns([2, 1])
    with c1: expr_input = st.text_input("Test Function f(x):", value="exp(x) * sin(x)")
    with c2: eval_pt = st.number_input("Evaluate at x =", value=1.0)
    
    try:
        engine = FunctionEngine(expr_input)
        num_eng = NumericalDifferentiationEngine(engine)
        sym_eng = DerivativeEngine(engine)
    except Exception as e:
        st.error(f"Initialization Error: {e}")
        st.stop()
        
    with tabs[0]:
        st.header("Finite-Difference Method Benchmarking")
        exact_val = sym_eng.evaluate_derivative(eval_pt, 1)
        exact_val_2 = sym_eng.evaluate_derivative(eval_pt, 2)
        
        st.markdown(f"**Exact 1st Derivative:** `{exact_val}` | **Exact 2nd Derivative:** `{exact_val_2}`")
        
        test_h = st.number_input("Test Step Size (h)", value=0.01, format="%.5f")
        
        results = []
        for name, stencil in STENCILS.items():
            from numerical.differentiation.derivative_approximations import apply_stencil
            approx = apply_stencil(engine, eval_pt, test_h, stencil)
            
            ref_val = exact_val_2 if stencil.derivative_order > 1 else exact_val
            if isinstance(approx, float) and isinstance(ref_val, float):
                status = num_eng.analyze_reliability(ref_val, approx, test_h)
                err = abs(ref_val - approx)
            else:
                status, err = "FAILED", "N/A"
                
            results.append({
                "Method": name, "Order O(h^n)": stencil.theoretical_order_accuracy,
                "Approx": approx, "Abs Error": err, "Status": status
            })
            
        st.dataframe(pd.DataFrame(results), use_container_width=True)

    with tabs[1]:
        st.header("Truncation vs Round-off Error (Cancellation Analysis)")
        st.markdown("As $h \\to 0$, theoretical truncation error decreases, but floating-point cancellation (round-off error) violently increases.")
        
        if isinstance(exact_val, float):
            sel_stencil = st.selectbox("Select Stencil for Experiment:", list(STENCILS.keys()))
            exp_data = step_size_experiment(engine, exact_val, eval_pt, STENCILS[sel_stencil])
            
            st.pyplot(plot_error_vs_stepsize(exp_data))
            
            with st.expander("View Raw Experiment Data"):
                st.dataframe(pd.DataFrame(exp_data))
        else:
            st.error("Exact value undefined at this point.")

    with tabs[2]:
        st.header("Algorithmic Improvement Techniques")
        col_r, col_a = st.columns(2)
        
        with col_r:
            st.subheader("Richardson Extrapolation")
            st.markdown("Eliminates leading error terms to jump from $O(h^2)$ to $O(h^4)$.")
            r_h = st.number_input("Base step size (h)", value=0.1)
            if st.button("Extrapolate"):
                st.json(richardson_extrapolation(engine, eval_pt, r_h))
                
        with col_a:
            st.subheader("Adaptive Step-Size Selection")
            st.markdown("Automatically searches for the optimal $h$ without hitting round-off.")
            tol = st.number_input("Tolerance", value=1e-6, format="%.7f")
            if st.button("Run Adaptive Search"):
                st.json(num_eng.adaptive_step_size(eval_pt, tol=tol))

    with tabs[3]:
        st.header("Discrete & Noisy Data Differentiation")
        
        st.subheader("1. Noisy Data Simulation")
        st.markdown("Numerical differentiation amplifies high-frequency noise. See the comparison:")
        noise_mag = st.slider("Noise Magnitude", 0.0, 0.5, 0.05)
        st.pyplot(plot_noisy_derivative(engine, eval_pt-3, eval_pt+3, noise_magnitude=noise_mag))
        
        st.divider()
        st.subheader("2. Differentiate Custom Discrete Data")
        st.markdown("Enter comma-separated values. Non-uniform spacing is automatically supported.")
        x_str = st.text_input("X values:", "0.0, 1.0, 2.5, 3.0, 4.2")
        y_str = st.text_input("Y values:", "0.0, 1.0, 6.25, 9.0, 17.64") # x^2
        
        if st.button("Calculate Discrete Derivatives"):
            try:
                x_vals = [float(x.strip()) for x in x_str.split(",")]
                y_vals = [float(y.strip()) for y in y_str.split(",")]
                derivs = differentiate_discrete_data(x_vals, y_vals)
                
                df = pd.DataFrame({"X": x_vals, "Y": y_vals, "Estimated dy/dx": derivs})
                st.dataframe(df, use_container_width=True)
            except Exception as e:
                st.error(f"Error parsing or calculating data: {e}")
