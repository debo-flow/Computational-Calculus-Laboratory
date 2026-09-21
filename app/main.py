# ... [Keep Milestones 1 to 13 unchanged] ...

elif page == "Milestone 14: Differential Equations":
    st.title("Advanced Differential Equations & Dynamical Systems")
    st.markdown("Solve Initial Value Problems, compare Numerical Steppers, and classify Nonlinear Phase Spaces.")

    from calculus.differential_equations.ode_analysis import classify_single_ode
    from calculus.differential_equations.symbolic_solutions import solve_symbolic_ode
    from calculus.differential_equations.systems import create_numerical_system, convert_second_order_to_system
    from calculus.differential_equations.equilibrium import find_equilibria
    from calculus.differential_equations.stability import analyze_stability
    from numerical.ode.rk4 import solve_fixed_step
    from numerical.ode.adaptive import solve_adaptive_rk45
    from visualization.ode_plots import plot_slope_field, plot_phase_portrait, plot_solution_comparison

    tabs = st.tabs([
        "Symbolic ODEs & IVPs", 
        "Numerical Solvers & Error", 
        "Systems & Phase Space", 
        "Equilibrium & Stability",
        "Physics Examples"
    ])

    with tabs[0]:
        st.header("Symbolic ODE Analysis & Initial Value Problems")
        st.info("Format: use `y'` for first derivative, `y''` for second. E.g., `y'' + 4*y = 0`")
        
        c1, c2 = st.columns(2)
        with c1: eq_input = st.text_input("Differential Equation:", "y' + 2*x*y = x")
        with c2: ivp_input = st.text_input("Initial Conditions (e.g. y(0)=1, y'(0)=0):", "y(0)=1")
        
        if st.button("Solve Symbolically"):
            class_res = classify_single_ode(eq_input)
            st.write(f"**Order:** `{class_res.get('Order')}` | **Autonomous:** `{class_res.get('Is Autonomous')}`")
            
            # Parse IVP
            ivp_dict = {}
            if ivp_input.strip():
                for cond in ivp_input.split(','):
                    k, v = cond.split('=')
                    ivp_dict[k.strip()] = float(v.strip())
                    
            sol_res = solve_symbolic_ode(eq_input, ivp=ivp_dict)
            if sol_res["Status"] == "Success":
                st.success("✅ Analytical Solution Found & Verified")
                st.latex(sp.latex(sol_res["General/Particular Solution"]))
            else:
                st.error(sol_res["Error"])
                
        st.divider()
        st.subheader("Slope/Direction Field")
        sf_eq = st.text_input("dy/dx = f(x,y):", "x - y")
        st.pyplot(plot_slope_field(sf_eq, (-3, 3), (-3, 3)))

    with tabs[1]:
        st.header("Numerical Solvers & Error Analysis")
        n1, n2, n3 = st.columns(3)
        with n1: n_eq = st.text_input("y' = f(t,y):", "-y + sin(t)", key="neq")
        with n2: t_end = st.number_input("End Time (t_end):", value=10.0)
        with n3: h_step = st.number_input("Step Size (h):", value=0.5)
        
        f_num = create_numerical_system([n_eq], "y")
        def f_wrapper(t, y): return f_num(t, y)[0]
        
        y0 = np.array([1.0])
        
        methods = ['Euler', 'Heun', 'Midpoint', 'RK4']
        results = {}
        for m in methods:
            t_vals, y_vals, stat = solve_fixed_step(f_wrapper, 0.0, y0, t_end, h_step, method=m)
            if stat == "SUCCESS": results[m] = y_vals
            
        t_ad, y_ad, stat_ad = solve_adaptive_rk45(f_wrapper, 0.0, y0, t_end)
        if stat_ad == "SUCCESS": results['Adaptive RK45'] = y_ad
        
        st.pyplot(plot_solution_comparison(t_vals, results))
        
        st.info("Notice how the Euler method accumulates severe local truncation error compared to RK4 or Adaptive RK45 at large step sizes.")

    with tabs[2]:
        st.header("Dynamical Systems & Phase Portraits")
        st.markdown("Analyze systems $\\frac{dx}{dt} = f(x,y)$ and $\\frac{dy}{dt} = g(x,y)$.")
        
        s1, s2 = st.columns(2)
        with s1: dx_dt = st.text_input("dx/dt = f(x,y):", "y")
        with s2: dy_dt = st.text_input("dy/dt = g(x,y):", "-sin(x) - 0.5*y") # Damped Pendulum
        
        st.pyplot(plot_phase_portrait([dx_dt, dy_dt], "x, y", (-10, 10), (-5, 5)))
        
        st.divider()
        st.subheader("Higher-Order Conversion")
        ho_eq = st.text_input("Convert y'' = f(x,y,y') into First-Order System:", "-sin(y) - 0.5*y'")
        sys_conv = convert_second_order_to_system(ho_eq)
        st.latex(r"u_1' = " + sp.latex(sys_conv["u1'"]))
        st.latex(r"u_2' = " + sp.latex(sys_conv["u2'"]))

    with tabs[3]:
        st.header("Equilibrium & Stability Analysis")
        st.markdown("Locates critical points where $\\frac{dx}{dt} = \\frac{dy}{dt} = 0$, computes the Jacobian Matrix, and classifies stability via eigenvalues.")
        
        eqs = [dx_dt, dy_dt]
        eq_points = find_equilibria(eqs, "x, y")
        
        if eq_points:
            for pt in eq_points:
                st.subheader(f"Equilibrium Candidate: `{pt}`")
                stab = analyze_stability(eqs, "x, y", pt)
                
                c3, c4 = st.columns(2)
                with c3:
                    st.write(f"- **Classification:** `{stab.get('Classification')}`")
                    st.write(f"- **Eigenvalues ($\lambda$):** `{stab.get('Eigenvalues')}`")
                with c4:
                    if "Jacobian (J)" in stab:
                        st.markdown("**Linearized Jacobian evaluated at point:**")
                        st.latex(sp.latex(sp.Matrix(stab['Evaluated J'])))
        else:
            st.warning("No real equilibrium points found or system too complex for exact symbolic roots.")

    with tabs[4]:
        st.header("Built-in Physics & Mathematical Systems")
        st.markdown("""
        Try inputting these famous dynamical systems into the Phase Space tab:
        
        **1. Lotka-Volterra (Predator-Prey)**
        * $dx/dt = x - xy$
        * $dy/dt = xy - y$
        * *Equilibria:* Saddle at $(0,0)$, Center at $(1,1)$.
        
        **2. Simple Harmonic Oscillator**
        * $dx/dt = y$
        * $dy/dt = -x$
        * *Stability:* Pure imaginary eigenvalues (Center).
        
        **3. Van der Pol Oscillator (Non-linear damping)**
        * $dx/dt = y$
        * $dy/dt = (1 - x^2)y - x$
        * *Feature:* Exhibits a stable limit cycle.
        """)
