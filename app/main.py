# ... [Keep Milestones 1 to 17 unchanged] ...

elif page == "Milestone 18: Adv. Differential Equations":
    st.title("Advanced Differential Equations & Dynamical Systems Laboratory")
    st.markdown("Solve BVPs/IVPs, benchmark numerical steppers (Euler to RK4), and dissect Phase Space topology.")

    from calculus.differential_equations.ode_analysis import classify_ode, compute_error_metrics, step_size_convergence_study
    from calculus.differential_equations.symbolic_solver import solve_symbolic_ode
    from calculus.differential_equations.numerical_solver import solve_fixed_step, solve_adaptive
    from calculus.differential_equations.systems import create_numerical_system
    from calculus.differential_equations.equilibrium import find_equilibria
    from calculus.differential_equations.stability import analyze_stability
    from visualization.dynamical_system_plots import plot_direction_field, plot_solver_comparison, plot_phase_portrait_complete

    tabs = st.tabs([
        "ODE Classification & Symbolic", 
        "Numerical Solvers & Convergence", 
        "Dynamical Systems & Phase Space", 
        "Stiffness & Stability"
    ])

    with tabs[0]:
        st.header("Symbolic Integration & Classification")
        c1, c2 = st.columns([2, 1])
        with c1: eq_input = st.text_input("ODE (use y' and y''):", "y'' + 4*y = 0")
        with c2: ivp_input = st.text_input("IVP (e.g. y(0)=1, y'(0)=0):", "y(0)=1, y'(0)=0")
        
        class_res = classify_ode(eq_input)
        if "Error" not in class_res:
            st.write(f"- **Order:** `{class_res['Order']}` | **Linearity:** `{class_res['Linearity']}`")
            st.write(f"- **Type:** `{class_res['Homogeneity']}`, `{class_res['Autonomous']}`")
            st.caption(f"Methods: {', '.join(class_res['Supported Methods'][:3])}...")
        
        if st.button("Solve Symbolically (SymPy)"):
            ivp_dict = {k.strip(): float(v.strip()) for k, v in [cond.split('=') for cond in ivp_input.split(',')] if cond} if ivp_input else {}
            sol_res = solve_symbolic_ode(eq_input, ivp=ivp_dict)
            if sol_res["Status"] == "Success":
                st.success("✅ Analytical Solution Found & Verified via Residual Check")
                st.latex(sp.latex(sol_res["General/Particular Solution"]))
            else:
                st.error(sol_res["Error"])

    with tabs[1]:
        st.header("Numerical Steppers & Error Analysis")
        n1, n2, n3 = st.columns(3)
        with n1: f_input = st.text_input("dy/dx = f(x,y):", "y", key="n_f")
        with n2: h_val = st.number_input("Base Step Size (h):", value=0.5)
        with n3: x_end = st.number_input("Final x:", value=5.0)
        
        f_num = create_numerical_system([f_input], "y")
        def f_wrap(x, y): return f_num(x, y)[0]
        
        if st.button("Compare All Solvers"):
            exact_y = np.exp(np.linspace(0, x_end, int(np.ceil(x_end/h_val)) + 1)) if f_input.strip() == "y" else None
            results = {}
            for method in ["Euler", "Heun", "RK2 (Midpoint)", "RK3", "RK4"]:
                x_num, y_num, stat = solve_fixed_step(f_wrap, 0.0, np.array([1.0]), x_end, h_val, method)
                if stat == "SUCCESS": results[method] = y_num
                
            st.pyplot(plot_solver_comparison(x_num, results, exact_y))
            
            if exact_y is not None:
                st.subheader("Convergence Study: Order Estimation $p$")
                st.markdown("For $y'=y$, halving $h$ reveals the characteristic experimental convergence order.")
                study = step_size_convergence_study(f_wrap, lambda x: np.exp(x), 0.0, np.array([1.0]), x_end, h_val, "RK4")
                st.dataframe(pd.DataFrame(study), use_container_width=True)

    with tabs[2]:
        st.header("Phase Space & Nullclines")
        s1, s2 = st.columns(2)
        with s1: dx_dt = st.text_input("dx/dt = f(x,y):", "x - x*y")
        with s2: dy_dt = st.text_input("dy/dt = g(x,y):", "x*y - y")
        
        eqs = [dx_dt, dy_dt]
        equilibria = find_equilibria(eqs, "x, y")
        st.pyplot(plot_phase_portrait_complete(eqs, "x, y", (-1, 3), (-1, 3), equilibria))
        
        if equilibria:
            st.subheader("Linearized Stability (Jacobian Eigenvalues)")
            for eq in equilibria:
                stab = analyze_stability(eqs, "x, y", eq)
                st.write(f"- **Point `{eq}`:** Classification $\\rightarrow$ `{stab.get('Classification')}`")
                st.caption(f"Eigenvalues: {stab.get('Eigenvalues')}")

    with tabs[3]:
        st.header("Direction Fields & Stiffness")
        df_eq = st.text_input("dy/dx = f(x,y):", "sin(x) - y")
        st.pyplot(plot_direction_field(df_eq, (-5, 5), (-5, 5)))
        
        st.divider()
        st.subheader("Stiffness & Adaptive Integration")
        st.markdown("Explicit solvers (RK4) crash when integrating stiff equations. Implicit adaptive methods (BDF) adjust $h$ dynamically.")
        if st.button("Run Stiff Simulation (Van der Pol, $\mu=1000$)"):
            f_vdp = lambda t, Y: np.array([Y[1], 1000*(1 - Y[0]**2)*Y[1] - Y[0]])
            _, _, stat_rk45 = solve_adaptive(f_vdp, 0, np.array([2.0, 0.0]), 10.0, stiff=False)
            t_bdf, y_bdf, stat_bdf = solve_adaptive(f_vdp, 0, np.array([2.0, 0.0]), 3000.0, stiff=True)
            
            st.error(f"**Explicit (RK45) Status:** {stat_rk45['Status']} - Step size became too small.")
            st.success(f"**Implicit (BDF) Status:** {stat_bdf['Status']} - Integrated successfully over 3000s in {stat_bdf['Accepted Steps']} steps.")
