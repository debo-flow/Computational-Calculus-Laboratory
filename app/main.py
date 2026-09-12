# ... [Keep Milestones 1 to 7 unchanged] ...

elif page == "Milestone 8: Numerical Integration":
    st.title("Advanced Numerical Integration Laboratory")
    st.markdown("Quadrature methods, error bounding, adaptive refinement, and discrete data integration.")
    
    from numerical.integration.quadrature_engine import NumericalIntegrationEngine
    from visualization.numerical_integration_plots import plot_adaptive_subdivisions, plot_cumulative_integral
    
    tabs = st.tabs(["Quadrature Methods", "Error & Convergence", "Adaptive & High-Peak", "Discrete & Cumulative"])
    
    c1, c2, c3 = st.columns([2, 1, 1])
    with c1: expr_input = st.text_input("Test Function f(x):", value="exp(-10*x^2)")
    with c2: bound_a = st.number_input("Lower (a):", value=-2.0)
    with c3: bound_b = st.number_input("Upper (b):", value=2.0)
    
    try:
        engine = FunctionEngine(expr_input)
        num_int_eng = NumericalIntegrationEngine(engine)
    except Exception as e:
        st.error(f"Error initializing: {e}")
        st.stop()
        
    with tabs[0]:
        st.header("Newton-Cotes & Gaussian Quadrature Benchmarks")
        st.markdown("Compare rules by computational cost (evaluations) and resulting accuracy.")
        test_n = st.number_input("Subintervals/Nodes (n):", value=12, min_value=1)
        
        methods = ["Trapezoidal", "Simpson 1/3", "Simpson 3/8", "Gauss-Legendre"]
        results = []
        for m in methods:
            rep = num_int_eng.execute_method(m, bound_a, bound_b, n=test_n)
            results.append(rep)
            
        st.dataframe(pd.DataFrame(results).drop(columns=["Subdivisions", "Theoretical Bound"], errors="ignore"), use_container_width=True)

    with tabs[1]:
        st.header("Theoretical Bounds & Convergence Order")
        meth = st.selectbox("Method for Convergence Study:", ["Trapezoidal", "Simpson 1/3"])
        
        st.subheader(f"Theoretical Error Bounding ({meth})")
        single_run = num_int_eng.execute_method(meth, bound_a, bound_b, n=10)
        if "Theoretical Bound" in single_run:
            st.json(single_run["Theoretical Bound"])
            
        st.subheader(f"Observed Convergence (n-stepping)")
        st.markdown("As $n$ doubles, observe the theoretical scaling of absolute error.")
        conv_res = num_int_eng.convergence_study(meth, bound_a, bound_b, n_list=[4, 8, 16, 32, 64])
        st.dataframe(pd.DataFrame(conv_res))

    with tabs[2]:
        st.header("Adaptive Quadrature (Adaptive Simpson)")
        st.markdown("Efficiently handles highly peaked or oscillatory functions by subdividing only where local error requires it.")
        a_tol = st.number_input("Tolerance:", value=1e-5, format="%.6f")
        
        if st.button("Run Adaptive Integration"):
            adapt_res = num_int_eng.execute_method("Adaptive Simpson", bound_a, bound_b, tol=a_tol)
            if adapt_res["Status"] == "Success":
                c4, c5 = st.columns(2)
                with c4:
                    st.write(f"- **Approximation:** `{adapt_res['Approximation']}`")
                    st.write(f"- **Exact:** `{adapt_res['Reference Exact']}`")
                    st.write(f"- **Absolute Error:** `{adapt_res.get('Absolute Error')}`")
                    st.write(f"- **Evaluations Used:** `{adapt_res['Evaluations']}`")
                    st.write(f"- **Total Subdivisions:** `{len(adapt_res['Subdivisions'])}`")
                    st.success(f"Reliability: {adapt_res['Reliability']}")
                with c5:
                    st.pyplot(plot_adaptive_subdivisions(engine, bound_a, bound_b, adapt_res["Subdivisions"]))
            else:
                st.error(adapt_res["Reason"])

    with tabs[3]:
        st.header("Discrete Data & Cumulative Integration")
        
        st.subheader("1. Cumulative Numerical Integration $F(x) = \int_a^x f(t) dt$")
        c_n = st.slider("Grid Resolution (n)", 10, 500, 100)
        if st.button("Generate Cumulative F(x)"):
            cum_data = num_int_eng.cumulative_integration(bound_a, bound_b, c_n)
            st.pyplot(plot_cumulative_integral(cum_data))
            
        st.divider()
        st.subheader("2. Differentiate/Integrate Custom Sampled Data")
        st.markdown("Handles non-uniform arrays seamlessly using numerical trapz.")
        dx_str = st.text_input("X Data:", "0.0, 1.0, 1.5, 3.0")
        dy_str = st.text_input("Y Data:", "0.0, 2.0, 4.5, 18.0")
        
        if st.button("Integrate Data Array"):
            x_arr = [float(x.strip()) for x in dx_str.split(",")]
            y_arr = [float(y.strip()) for y in dy_str.split(",")]
            area = num_int_eng.data_integration(x_arr, y_arr)
            st.info(f"**Total Data Area:** `{area}`")

