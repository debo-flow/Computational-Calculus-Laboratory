# ... [Keep Milestones 1 to 21 unchanged] ...

elif page == "Milestone 22: Scientific Computing":
    st.title("Advanced Numerical Calculus & Scientific Computing Laboratory")
    st.markdown("Analyze arbitrary precision, discrete linear algebra (SVD/Eigen), cubic splines, and finite-difference PDE foundations.")

    from numerical.scientific.precision import compare_precision
    from numerical.scientific.error_analysis import compute_condition_number
    from numerical.scientific.differentiation import richardson_extrapolation
    from numerical.scientific.linear_algebra import analyze_svd, analyze_eigen
    from numerical.scientific.interpolation import cubic_spline_interpolation
    from numerical.scientific.numerical_engine import solve_1d_heat_pde
    from numerical.scientific.benchmarking import generate_scientific_report
    from visualization.scientific_computing_plots import plot_cubic_spline, plot_pde_evolution

    tabs = st.tabs([
        "Precision & Error", 
        "Linear Algebra (SVD & Eigen)", 
        "Spline Interpolation", 
        "PDE Foundations & Stability",
        "Scientific Reporting"
    ])

    with tabs[0]:
        st.header("Conditioning, Extrapolation & Arbitrary Precision")
        
        st.subheader("1. Problem Conditioning")
        st.markdown(r"Relative Condition Number $K = \left\vert{} \frac{x \cdot f'(x)}{f(x)} \right\vert{}$. High $K$ indicates inherent mathematical sensitivity to input variance.")
        c1, c2 = st.columns(2)
        with c1: f_str = st.text_input("Function f(x):", "exp(x) - 1")
        with c2: p_val = st.number_input("Evaluation Point x:", value=1e-5, format="%.6f")
        if st.button("Calculate Condition Number"):
            st.json(compute_condition_number(f_str, p_val))
            
        st.divider()
        st.subheader("2. Arbitrary Precision Evaluation")
        st.markdown("Compares standard 64-bit IEEE 754 floats against multi-precision libraries (mpmath).")
        dps_val = st.slider("Target Decimal Places (dps):", 15, 100, 50)
        if st.button("Compare Precision"):
            st.json(compare_precision(f_str, p_val, dps=dps_val))
            
        st.divider()
        st.subheader("3. Richardson Extrapolation")
        st.markdown(r"Eliminates lowest-order truncation errors by combining discrete steps: $A \approx \frac{4D(h/2) - D(h)}{3}$")
        if st.button("Extrapolate Derivative"):
            f_eval = lambda x: np.exp(x) - 1 # from defaults
            st.json(richardson_extrapolation(f_eval, p_val, 0.1))

    with tabs[1]:
        st.header("Numerical Linear Algebra")
        mat_in = st.text_area("Input Matrix (Comma separated, rows on new lines):", "1, 2\n3, 4")
        
        try:
            mat_data = [[float(v) for v in row.split(',')] for row in mat_in.strip().split('\n')]
            
            s1, s2 = st.columns(2)
            with s1:
                st.subheader("Singular Value Decomposition (SVD)")
                if st.button("Compute SVD ($A = U \Sigma V^T$)"):
                    st.json(analyze_svd(mat_data))
            with s2:
                st.subheader("Eigenvalue Analysis")
                if st.button("Compute Eigen system ($Av = \lambda v$)"):
                    if len(mat_data) == len(mat_data[0]):
                        st.json(analyze_eigen(mat_data))
                    else:
                        st.error("Matrix must be square for Eigenvalue analysis.")
        except Exception as e:
            st.error(f"Matrix parsing error: {e}")

    with tabs[2]:
        st.header("Cubic Spline Interpolation")
        i1, i2 = st.columns(2)
        with i1: x_pts = st.text_input("X Data Points:", "0, 1, 2, 3, 4")
        with i2: y_pts = st.text_input("Y Data Points:", "0, 0.8, 0.9, 0.1, -0.8")
        
        if st.button("Generate Spline"):
            x_d = [float(v) for v in x_pts.split(',')]
            y_d = [float(v) for v in y_pts.split(',')]
            
            x_eval = np.linspace(min(x_d), max(x_d), 200).tolist()
            spline_res = cubic_spline_interpolation(x_d, y_d, x_eval, 'natural')
            
            st.pyplot(plot_cubic_spline(x_d, y_d, x_eval, spline_res["y_eval"]))

    with tabs[3]:
        st.header("PDE Foundation: 1D Heat Equation")
        st.markdown(r"Numerical integration of $u_t = \alpha u_{xx}$ via Forward-Time Central-Space (FTCS) finite differences.")
        
        p1, p2, p3 = st.columns(3)
        with p1: alpha = st.number_input("Thermal Diffusivity $\alpha$:", value=0.01)
        with p2: nt = st.number_input("Time Steps ($N_t$):", value=100)
        with p3: T_end = st.number_input("End Time (T):", value=1.0)
        
        if st.button("Simulate PDE & Check CFL Stability"):
            pde_res = solve_1d_heat_pde(1.0, T_end, 50, nt, alpha)
            st.write(f"- **CFL Stability Parameter:** `{pde_res['CFL Stability Parameter']:.4f}` (Must be $\le 0.5$)")
            
            if pde_res["Stable"]:
                st.success("Scheme is numerically stable.")
                st.pyplot(plot_pde_evolution(pde_res["x_grid"], pde_res["History"]))
            else:
                st.error(f"Scheme is UNSTABLE. $\Delta t$ exceeds the critical limit `{pde_res['Required dt Limit']:.5f}`. The numerical error will amplify exponentially.")

    with tabs[4]:
        st.header("Reproducible Benchmarking Reports")
        st.markdown("Appends hardware profiles, execution times, and strict formatting guarantees to experimental runs.")
        if st.button("Run Benchmark (SVD Decomposition)"):
            bench = generate_scientific_report(analyze_svd, [[1,2,3],[4,5,6],[7,8,9]])
            st.json(bench)
