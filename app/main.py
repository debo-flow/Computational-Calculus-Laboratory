# ... [Keep Milestones 1 to 18 unchanged] ...

elif page == "Milestone 19: Adv. Differential Equations":
    st.title("Advanced Differential Equations & Dynamical Systems Laboratory")
    st.markdown("Solve First-Order systems symbolically, benchmark convergence, and map multidimensional Phase Space.")

    from calculus.differential_equations.ode_analysis import classify_ode, empirical_convergence_study
    from calculus.differential_equations.first_order import analyze_bernoulli, analyze_exact
    from calculus.differential_equations.symbolic_solver import solve_symbolic_ode
    from calculus.differential_equations.numerical_solver import solve_fixed_step, solve_adaptive
    from calculus.differential_equations.systems import create_numerical_system, CLASSIC_MODELS
    from calculus.differential_equations.equilibrium import find_equilibria
    from calculus.differential_equations.stability import analyze_stability
    from visualization.ode_plots import plot_direction_field_with_trajectories, plot_solver_comparison, plot_phase_portrait_complete

    tabs = st.tabs([
        "ODE Classification & Symbolic", 
        "First-Order Deep Analysis",
        "Numerical Solvers & Convergence", 
        "Phase Space & Nullclines",
        "Dynamical Systems Explorer"
    ])

    with tabs[0]:
        st.header("Symbolic Classification & Solutions")
        c1, c2 = st.columns([2, 1])
        with c1: eq_input = st.text_input("ODE (use y' and y''):", "y'' + y = 0")
        with c2: ivp_input = st.text_input("IVP (e.g. y(0)=1, y'(0)=0):", "y(0)=1, y'(0)=0")
        
        class_res = classify_ode(eq_input)
        if "Error" not in class_res:
            st.write(f"- **Order:** `{class_res['Order']}` | **Type:** `{class_res['Linearity']}`, `{class_res['Homogeneity']}`")
            st.write(f"- **Properties:** Exact: `{class_res['Exact']}`, Separable: `{class_res['Separable']}`, Bernoulli: `{class_res['Bernoulli']}`")
        
        if st.button("Solve Symbolically & Verify"):
            ivp_dict = {k.strip(): float(v.strip()) for k, v in [cond.split('=') for cond in ivp_input.split(',')] if cond} if ivp_input else {}
            sol_res = solve_symbolic_ode(eq_input, ivp=ivp_dict)
            if sol_res["Status"] == "Success":
                st.success("✅ Analytical Solution Verified via Substitution (Residual = 0)")
                st.latex(sp.latex(sol_res["Solution"]))
            else:
                st.error(sol_res["Error"])

    with tabs[1]:
        st.header("First-Order Equation Sub-Analysis")
        anal_type = st.radio("Select Analysis Type:", ["Exact Equation Check", "Bernoulli Substitution"])
        
        if anal_type == "Exact Equation Check":
            st.markdown(r"Forms $M(x,y)dx + N(x,y)dy = 0$")
            e1, e2 = st.columns(2)
            with e1: m_str = st.text_input("M(x,y):", "2*x*y")
            with e2: n_str = st.text_input("N(x,y):", "x^2 + 3*y^2")
            ex_res = analyze_exact(m_str, n_str)
            st.write(f"$\partial M / \partial y = {sp.latex(ex_res['dM/dy'])}$, $\partial N / \partial x = {sp.latex(ex_res.get('dN/dx', 'N/A'))}$")
            if ex_res["Exact"]:
                st.success("Equation is Exact.")
                st.latex(r"F(x,y) = " + sp.latex(ex_res["Potential F(x,y)"]) + r" = C")
            else:
                st.warning("Equation is not Exact.")
                
        elif anal_type == "Bernoulli Substitution":
            st.markdown(r"Forms $y' + P(x)y = Q(x)y^n$")
            b1, b2, b3 = st.columns(3)
            with b1: bp_str = st.text_input("P(x):", "1/x")
            with b2: bq_str = st.text_input("Q(x):", "x")
            with b3: bn_val = st.number_input("n:", value=2.0)
            ber_res = analyze_bernoulli(bp_str, bq_str, bn_val)
            if ber_res["Status"] == "Success":
                st.latex(sp.latex(ber_res["Linearized v Equation"]))
                st.latex(sp.latex(ber_res["Final Implicit/Explicit y(x)"]))

    with tabs[2]:
        st.header("Numerical Error & Direction Fields")
        st.markdown(r"Compare Euler $O(h)$, Heun $O(h^2)$, Midpoint $O(h^2)$, and RK4 $O(h^4)$.")
        
        n_eq = st.text_input("dy/dx = f(x,y):", "x - y")
        f_num = create_numerical_system([n_eq], "y")
        def f_wrap(x, y): return f_num(x, y)[0]
        
        if st.button("Generate Direction Field & Compare Solvers"):
            results = {}
            for method in ["Euler", "Heun", "Midpoint", "RK4"]:
                x_num, y_num, _ = solve_fixed_step(f_wrap, 0.0, np.array([1.0]), 3.0, 0.5, method)
                results[method] = y_num
            
            st.pyplot(plot_solver_comparison(x_num, results))
            # Direction Field with RK4 Trajectory
            t_x, t_y, _ = solve_fixed_step(f_wrap, -3.0, np.array([0.0]), 3.0, 0.1, "RK4")
            st.pyplot(plot_direction_field_with_trajectories(n_eq, (-3, 3), (-3, 3), [(t_x, t_y[:, 0])]))

    with tabs[3]:
        st.header("Phase Space, Nullclines & Stability")
        s1, s2 = st.columns(2)
        with s1: dx_dt = st.text_input("dx/dt = f(x,y):", "x - x*y")
        with s2: dy_dt = st.text_input("dy/dt = g(x,y):", "x*y - y")
        
        eqs = [dx_dt, dy_dt]
        equilibria = find_equilibria(eqs, "x, y")
        st.pyplot(plot_phase_portrait_complete(eqs, "x, y", (-1, 3), (-1, 3), equilibria))
        
        if equilibria:
            for eq in equilibria:
                stab = analyze_stability(eqs, "x, y", eq)
                st.write(f"- **Equilibrium `{eq}`:** `{stab.get('Classification')}` (Eigenvalues: `{stab.get('Eigenvalues')}`)")

    with tabs[4]:
        st.header("Classical Parameter Explorer")
        model = st.selectbox("Select Model:", list(CLASSIC_MODELS.keys()))
        data = CLASSIC_MODELS[model]
        
        params = {}
        cols = st.columns(len(data["params"]))
        for i, p in enumerate(data["params"]):
            params[p] = cols[i].number_input(f"Parameter '{p}':", value=1.0)
            
        sys_subbed = [str(sp.sympify(eq).subs(params)) for eq in data["sys"]]
        st.latex("System: " + ", ".join([sp.latex(sp.sympify(eq)) for eq in sys_subbed]))
        
        if len(data["vars"].split(',')) == 2:
            eqs2 = find_equilibria(sys_subbed, data["vars"])
            st.pyplot(plot_phase_portrait_complete(sys_subbed, data["vars"], (-2, 2), (-2, 2), eqs2))
