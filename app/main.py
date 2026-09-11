# ... [Keep Milestones 1 to 4 logic exactly as they were] ...

elif page == "Milestone 5: Applications of Calculus":
    st.title("Applications of Differential Calculus Laboratory")
    st.markdown("Analyze critical points, extrema, mathematical theorems, and roots.")
    
    # Import M5 dependencies dynamically to avoid cluttering global scope
    from calculus.applications.critical_points import find_critical_points
    from calculus.applications.extrema import classify_local_extrema, find_absolute_extrema
    from calculus.applications.concavity import find_inflection_points
    from calculus.applications.analysis_engine import ApplicationAnalysisEngine
    from numerical.root_finding import newton_raphson
    from visualization.applications_plots import plot_function_analysis
    
    tabs = st.tabs(["Function Analysis", "Optimization (Extrema)", "Theorems & Approximations", "Newton's Method"])
    
    with tabs[0]:
        st.header("Comprehensive Function Analysis")
        expr_input = st.text_input("Analyze Function f(x):", value="x^3 - 3*x")
        try:
            engine = FunctionEngine(expr_input)
            st.latex(f"f(x) = {sp.latex(engine.expression)}")
            
            c1, c2 = st.columns(2)
            with c1:
                st.subheader("Critical & Stationary Points")
                crits = find_critical_points(engine)
                st.write("Candidates where $f'(x) = 0$:")
                st.json(crits)
                
                st.subheader("Concavity & Inflection")
                infs = find_inflection_points(engine)
                st.json(infs)
            with c2:
                st.pyplot(plot_function_analysis(engine, -3, 3))
        except Exception as e:
            st.error(str(e))
            
    with tabs[1]:
        st.header("Optimization & Extrema")
        if 'engine' in locals():
            st.subheader("Local Extrema (2nd Derivative Test)")
            st.json(classify_local_extrema(engine))
            
            st.subheader("Absolute Extrema (Closed Interval)")
            col_a, col_b = st.columns(2)
            a_val = col_a.number_input("Interval [a]", value=-2.0)
            b_val = col_b.number_input("Interval [b]", value=2.0)
            st.json(find_absolute_extrema(engine, a_val, b_val))
            
    with tabs[2]:
        st.header("Calculus Theorems & Approximations")
        if 'engine' in locals():
            app_eng = ApplicationAnalysisEngine(engine)
            
            st.subheader("Mean Value Theorem")
            st.markdown("Verifies existence of $c$ such that $f'(c) = \\frac{f(b)-f(a)}{b-a}$")
            c3, c4 = st.columns(2)
            mvt_a = c3.number_input("MVT start (a)", value=0.0)
            mvt_b = c4.number_input("MVT end (b)", value=2.0)
            st.json(app_eng.mean_value_theorem(mvt_a, mvt_b))
            
            st.divider()
            st.subheader("Linear Approximation (Tangent Line)")
            c5, c6 = st.columns(2)
            lin_a = c5.number_input("Center point (a)", value=1.0)
            lin_x = c6.number_input("Estimate at (x)", value=1.1)
            st.json(app_eng.linear_approximation(lin_a, lin_x))
            
    with tabs[3]:
        st.header("Newton-Raphson Root Finding")
        if 'engine' in locals():
            st.markdown(r"Iterative root finding: $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$")
            c7, c8 = st.columns(2)
            x_init = c7.number_input("Initial Guess ($x_0$)", value=2.0)
            iters = c8.slider("Max Iterations", 5, 50, 15)
            
            if st.button("Find Root"):
                root_res = newton_raphson(engine, x_init, max_iter=iters)
                if root_res["Status"] == "Converged":
                    st.success(f"Root found at: **{root_res['Root']}** in {root_res['Iterations']} iterations.")
                else:
                    st.error(root_res["Status"])
                st.dataframe(pd.DataFrame(root_res["History"]), use_container_width=True)
