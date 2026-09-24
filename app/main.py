# ... [Keep Milestones 1 to 15 unchanged] ...

elif page == "Milestone 16: Adv. Differential Equations":
    st.title("Advanced Differential Equations & Dynamical Systems Laboratory")
    st.markdown("Analyze Matrix Systems, Characteristic Roots, Chaos (Sensitivity), Stiff ODEs, and Energy Conservation.")

    from calculus.differential_equations.second_order import analyze_constant_coeff_linear
    from calculus.differential_equations.systems import analyze_matrix_system, create_numerical_system
    from calculus.differential_equations.ode_analysis import verify_conservation
    from numerical.ode_solvers import solve_fixed_step, solve_adaptive
    from visualization.differential_equation_plots import plot_sensitivity, plot_energy_variation

    tabs = st.tabs([
        "2nd-Order & Matrix Systems", 
        "Conservation & Energy", 
        "Sensitivity (Chaos)", 
        "Stiffness Foundation"
    ])

    with tabs[0]:
        st.header("Linear Systems Analysis")
        st.subheader("1. Second-Order Linear ODEs ($ay'' + by' + cy = 0$)")
        c1, c2, c3 = st.columns(3)
        with c1: a_coef = st.number_input("a:", value=1.0)
        with c2: b_coef = st.number_input("b:", value=2.0)
        with c3: c_coef = st.number_input("c:", value=5.0)
        
        if st.button("Analyze Characteristic Equation"):
            res2 = analyze_constant_coeff_linear(a_coef, b_coef, c_coef)
            st.write(f"- **Roots:** `{res2['Roots']}`")
            st.write(f"- **Classification:** `{res2['Root Classification']}`")
            st.latex("y_h(x) = " + sp.latex(res2["Homogeneous Solution y_h(x)"]))

        st.divider()
        st.subheader("2. Matrix Systems ($X' = AX$)")
        st.markdown("Enter 2x2 Matrix elements row by row:")
        m1, m2 = st.columns(2)
        with m1: a11 = st.number_input("A_11", value=0.0); a21 = st.number_input("A_21", value=-1.0)
        with m2: a12 = st.number_input("A_12", value=1.0); a22 = st.number_input("A_22", value=-0.5)
        
        if st.button("Analyze Matrix System"):
            A_mat = [[a11, a12], [a21, a22]]
            res_mat = analyze_matrix_system(A_mat)
            st.latex(r"A = " + sp.latex(res_mat["Matrix A"]))
            st.write(f"- **Eigenvalues:** `{res_mat['Eigenvalues']}`")
            st.write(f"- **Trace ($\Delta$):** `{res_mat['Trace']}` | **Determinant ($D$):** `{res_mat['Determinant']}`")
            st.success(f"**Classification:** {res_mat['Classification']}")

    with tabs[1]:
        st.header("Conservation Laws & Energy")
        st.markdown("Symbolically verifies if a given invariant $I(X)$ is conserved ($dI/dt = 0$) along system trajectories.")
        
        eq1 = st.text_input("dx/dt = f(x,y):", "y", key="e1")
        eq2 = st.text_input("dy/dt = g(x,y):", "-sin(x)", key="e2")
        inv = st.text_input("Candidate Invariant I(x,y) (e.g. Energy):", "0.5*y^2 - cos(x)")
        
        if st.button("Verify Conservation"):
            con_res = verify_conservation([eq1, eq2], "x, y", inv)
            st.latex(r"\frac{dI}{dt} = \nabla I \cdot \vec{F} = " + sp.latex(con_res["Derivative dI/dt"]))
            if con_res["Is Conserved"]:
                st.success(f"✅ {con_res['Interpretation']}")
            else:
                st.warning(f"❌ {con_res['Interpretation']}")
                
        st.subheader("Numerical Energy Fluctuation")
        st.markdown("Visualizes numerical drift or dissipation in the Energy function over time.")
        if st.button("Plot Energy Variation (RK45)"):
            f_sys = create_numerical_system([eq1, eq2], "x, y")
            t_vals, y_vals, _ = solve_adaptive(lambda t, y: f_sys(t, y), 0, np.array([3.0, 0.0]), 20.0)
            st.pyplot(plot_energy_variation(t_vals, y_vals, inv, "x, y"))

    with tabs[2]:
        st.header("Sensitive Dependence (Chaos Foundation)")
        st.markdown("Measures trajectory divergence resulting from an infinitesimally shifted initial condition ($X_0 + \delta X$). Exponential separation strongly indicates chaos.")
        
        p1, p2 = st.columns(2)
        with p1: s_dx = st.text_input("dx/dt:", "10*(y - x)", key="sd1") # Lorenz X
        with p2: s_dy = st.text_input("dy/dt:", "x*(28 - z) - y", key="sd2") # Lorenz Y
        s_dz = st.text_input("dz/dt:", "x*y - 8/3*z", key="sd3") # Lorenz Z
        
        if st.button("Simulate Trajectory Separation"):
            f_chaos = create_numerical_system([s_dx, s_dy, s_dz], "x, y, z")
            def wrapper(t, Y): return f_chaos(t, Y)
            
            # Base trajectory
            t1, y1, _ = solve_adaptive(wrapper, 0, np.array([1.0, 1.0, 1.0]), 25.0)
            # Perturbed trajectory
            t2, y2, _ = solve_adaptive(wrapper, 0, np.array([1.0, 1.0, 1.00001]), 25.0)
            
            # Align times (Interpolation for direct subtraction)
            from scipy.interpolate import interp1d
            common_t = np.linspace(0, 25.0, 1000)
            y1_interp = interp1d(t1, y1, axis=0)(common_t)
            y2_interp = interp1d(t2, y2, axis=0)(common_t)
            
            st.pyplot(plot_sensitivity(common_t, y1_interp, y2_interp))

    with tabs[3]:
        st.header("Stiffness Foundation")
        st.markdown("Some equations possess drastically different timescales, causing explicit solvers (RK4) to fail unless step sizes are microscopically small. **Implicit solvers (BDF/Radau)** bypass this limit.")
        
        st.info("**Example Stiff ODE:** Van der Pol oscillator with high $\mu$ ($y'' - 1000(1-y^2)y' + y = 0$)")
        stiff_mode = st.radio("Select Solver Type:", ["Explicit (RK45) - Likely to crash/stall", "Implicit (BDF) - Stiff Stable"])
        
        if st.button("Solve Stiff System"):
            stiff = (stiff_mode == "Implicit (BDF) - Stiff Stable")
            # Van der Pol mu = 1000
            f_vdp = lambda t, Y: np.array([Y[1], 1000*(1 - Y[0]**2)*Y[1] - Y[0]])
            
            import time
            start_time = time.time()
            t_s, y_s, stat = solve_adaptive(f_vdp, 0, np.array([2.0, 0.0]), 3000.0, stiff=stiff)
            elapsed = time.time() - start_time
            
            if "SUCCESS" in stat:
                st.success(f"{stat} in {elapsed:.3f} seconds. ({len(t_s)} evaluation steps)")
                fig, ax = plt.subplots(figsize=(9, 4))
                ax.plot(t_s, y_s[:, 0], color='black')
                ax.set_title(f"Stiff System Solution ({stiff_mode})")
                st.pyplot(fig)
            else:
                st.error(f"Solver stalled or failed: {stat}. Elapsed: {elapsed:.2f}s")

