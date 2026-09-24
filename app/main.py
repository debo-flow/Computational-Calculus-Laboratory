# ... [Keep Milestones 1 to 16 unchanged] ...

elif page == "Milestone 17: Adv. Differential Equations":
    st.title("Advanced Differential Equations & Dynamical Systems")
    st.markdown("Solve ODEs analytically, benchmark convergence rates, and analyze nonlinear chaos/bifurcations.")

    from calculus.differential_equations.ode_analysis import classify_single_ode, sensitivity_analysis, parameter_sweep_equilibria
    from calculus.differential_equations.symbolic_solutions import solve_symbolic_ode
    from calculus.differential_equations.systems import create_numerical_system
    from calculus.differential_equations.equilibrium import find_equilibria
    from calculus.differential_equations.stability import analyze_stability
    from calculus.differential_equations.numerical_solvers import run_convergence_study
    from numerical.ode_solvers import solve_fixed_step, solve_adaptive
    from visualization.ode_plots import plot_solution_comparison, plot_phase_portrait_with_nullclines, plot_3d_trajectory, plot_sensitivity_separation

    tabs = st.tabs([
        "ODE Classification & Analytical",
        "Numerical Solvers & Convergence", 
        "Dynamical Systems & Nullclines", 
        "Bifurcation & Chaos",
        "Classic System Sandbox"
    ])

    with tabs[0]:
        st.header("ODE Classification & Symbolic Solution")
        c1, c2 = st.columns(2)
        with c1: eq_input = st.text_input("Equation (e.g. y' + y = x):", "y'' + 4*y = 0")
        with c2: ivp_input = st.text_input("Initial Conditions (e.g. y(0)=1, y'(0)=0):", "y(0)=1")
        
        class_res = classify_single_ode(eq_input)
        st.write(f"- **Order:** `{class_res.get('Order')}` | **Linear:** `{class_res.get('Linear')}`")
        st.write(f"- **Homogeneous:** `{class_res.get('Homogeneous')}` | **Autonomous:** `{class_res.get('Is Autonomous')}`")
        
        if st.button("Solve Symbolically"):
            ivp_dict = {}
            if ivp_input.strip():
                for cond in ivp_input.split(','):
                    k, v = cond.split('=')
                    ivp_dict[k.strip()] = float(v.strip())
            sol_res = solve_symbolic_ode(eq_input, ivp=ivp_dict)
            if sol_res["Status"] == "Success":
                st.success("Analytical Solution Verified")
                st.latex(sp.latex(sol_res["General/Particular Solution"]))
            else:
                st.error(sol_res["Error"])

    with tabs[1]:
        st.header("Numerical Convergence Study")
        st.markdown("Analyzes empirical convergence order $p \approx \log(E_1/E_2) / \log(h_1/h_2)$ against exact solutions.")
        
        conv_method = st.selectbox("Solver:", ["Euler", "Heun", "Midpoint", "RK4"], index=3)
        if st.button(f"Run Convergence Study ({conv_method})"):
            # Using standard test: y' = y, y(0)=1 -> Exact: e^x
            f = lambda x, y: y
            exact = lambda x: np.exp(x)
            
            study = run_convergence_study(f, exact, 0.0, np.array([1.0]), 2.0, 0.4, conv_method)
            st.dataframe(pd.DataFrame(study), use_container_width=True)
            st.info(f"Theoretical orders: Euler $O(h)$, Midpoint/Heun $O(h^2)$, RK4 $O(h^4)$. Observe the 'Observed Order (p)'.")

    with tabs[2]:
        st.header("Phase Space, Equilibria & Nullclines")
        s1, s2 = st.columns(2)
        with s1: dx_dt = st.text_input("dx/dt = f(x,y):", "x - x*y")
        with s2: dy_dt = st.text_input("dy/dt = g(x,y):", "x*y - y")
        
        st.pyplot(plot_phase_portrait_with_nullclines([dx_dt, dy_dt], "x, y", (-1, 3), (-1, 3)))
        
        eqs = [dx_dt, dy_dt]
        eq_points = find_equilibria(eqs, "x, y")
        if eq_points:
            for pt in eq_points:
                stab = analyze_stability(eqs, "x, y", pt)
                st.write(f"**Equilibrium `{pt}`** -> `{stab.get('Classification')}`")

    with tabs[3]:
        st.header("Chaos (Sensitivity) & Bifurcations")
        st.subheader("1. Sensitive Dependence on Initial Conditions")
        st.markdown("In chaotic systems (like Lorenz), an infinitesimal change $\delta$ in $X_0$ causes exponential divergence.")
        
        l_x = st.text_input("dx/dt:", "10*(y - x)")
        l_y = st.text_input("dy/dt:", "x*(28 - z) - y")
        l_z = st.text_input("dz/dt:", "x*y - 8/3*z")
        
        if st.button("Simulate 3D Chaotic System"):
            f_sys = create_numerical_system([l_x, l_y, l_z], "x, y, z")
            t, y_vals, _ = solve_adaptive(lambda t, Y: f_sys(t, Y), 0, np.array([1.0, 1.0, 1.0]), 30.0)
            
            c3, c4 = st.columns(2)
            with c3:
                st.pyplot(plot_3d_trajectory(t, y_vals, "x, y, z"))
            with c4:
                t_sep, sep = sensitivity_analysis(lambda t, Y: f_sys(t, Y), 30.0, np.array([1.0, 1.0, 1.0]), delta=1e-5)
                st.pyplot(plot_sensitivity_separation(t_sep, sep))
                st.caption("Exponential growth of separation proves chaotic sensitivity.")
                
        st.divider()
        st.subheader("2. Bifurcation Parameter Sweep")
        st.markdown("Track how equilibrium locations change or appear/disappear as a parameter $\mu$ sweeps.")
        bif_eq = st.text_input("System (use 'mu'):", "mu*x - x^3")
        if st.button("Sweep mu = [-1.0, 0.0, 1.0]"):
            sweep = parameter_sweep_equilibria([bif_eq], "x", "mu", [-1.0, 0.0, 1.0])
            for res in sweep:
                st.write(f"- $\mu = {res['Parameter Value']}$  $\Rightarrow$ Equilibria at: `{res['Equilibria']}`")
            st.info("Notice Pitchfork Bifurcation: At mu < 0, 1 root. At mu > 0, 3 roots.")

    with tabs[4]:
        st.header("Classic Dynamical Models Sandbox")
        preset = st.selectbox("Load Classic System:", [
            "Harmonic Oscillator (Center)",
            "Damped Oscillator (Stable Spiral)",
            "Van der Pol Oscillator (Limit Cycle)",
            "Lotka-Volterra (Predator-Prey)"
        ])
        
        if "Harmonic" in preset:
            st.code("dx/dt = y\ndy/dt = -x")
        elif "Damped" in preset:
            st.code("dx/dt = y\ndy/dt = -x - 0.5*y")
        elif "Van der Pol" in preset:
            st.code("dx/dt = y\ndy/dt = (1 - x^2)*y - x")
        elif "Lotka-Volterra" in preset:
            st.code("dx/dt = x - x*y\ndy/dt = x*y - y")
        st.info("Input these equations into the Phase Space or Bifurcation tabs to explore their dynamics.")
