# ... [Keep Milestones 1 to 14 unchanged] ...

elif page == "Milestone 15: Differential Equations":
    st.title("Advanced Differential Equations & Dynamical Systems Laboratory")
    st.markdown("Solve BVPs, Exact/Linear ODEs, Classify Dynamical Phase Spaces, and run Adaptive Integrators.")

    # M14 Imports
    from calculus.differential_equations.ode_analysis import classify_single_ode
    from calculus.differential_equations.symbolic_solutions import solve_symbolic_ode
    from calculus.differential_equations.systems import create_numerical_system, convert_second_order_to_system
    from calculus.differential_equations.equilibrium import find_equilibria
    from calculus.differential_equations.stability import analyze_stability
    from numerical.ode.rk4 import solve_fixed_step
    from numerical.ode.adaptive import solve_adaptive_rk45
    from visualization.ode_plots import plot_slope_field, plot_phase_portrait, plot_solution_comparison
    
    # M15 Imports
    from calculus.differential_equations.first_order import solve_exact_equation, solve_linear_first_order
    from numerical.ode.bvp_solvers import shooting_method, finite_difference_bvp_linear
    from visualization.differential_equation_plots import plot_isoclines, plot_bvp_solution

    tabs = st.tabs([
        "First-Order Analytical",
        "Symbolic General & IVP", 
        "Boundary Value Problems (BVP)",
        "Numerical Error Control", 
        "Dynamical Systems & Equilibria"
    ])

    with tabs[0]:
        st.header("First-Order Analytical Techniques")
        st.markdown("### Exact Equations: $M(x,y)dx + N(x,y)dy = 0$")
        c1, c2 = st.columns(2)
        with c1: m_str = st.text_input("M(x,y):", "2*x*y")
        with c2: n_str = st.text_input("N(x,y):", "x^2 - 1")
        if st.button("Check Exactness & Solve"):
            ex_res = solve_exact_equation(m_str, n_str)
            st.write(f"- **$\\frac{{\partial M}}{{\partial y}}$:** `{ex_res['dM/dy']}`")
            st.write(f"- **$\\frac{{\partial N}}{{\partial x}}$:** `{ex_res['dN/dx']}`")
            if ex_res["Exact"]:
                st.success("✅ Equation is Exact")
                st.latex(r"F(x,y) = " + sp.latex(ex_res["Potential F(x,y)"]) + r" = C")
            else:
                st.warning("❌ Not Exact")
                
        st.divider()
        st.markdown("### Linear Integrating Factor: $y' + P(x)y = Q(x)$")
        l1, l2 = st.columns(2)
        with l1: p_str = st.text_input("P(x):", "2/x")
        with l2: q_str = st.text_input("Q(x):", "x")
        if st.button("Solve Linear Equation"):
            lin_res = solve_linear_first_order(p_str, q_str)
            st.latex(r"\mu(x) = e^{\int P(x) dx} = " + sp.latex(lin_res["Integrating Factor mu(x)"]))
            st.latex(r"y(x) = " + sp.latex(lin_res["General Solution"]))

    with tabs[1]:
        st.header("Symbolic General Solutions & IVPs")
        eq_input = st.text_input("Differential Equation:", "y'' + 4*y = 0")
        ivp_input = st.text_input("Initial Conditions (Optional, e.g., y(0)=1, y'(0)=0):", "")
        
        class_res = classify_single_ode(eq_input)
        st.write(f"**Order:** `{class_res.get('Order')}` | **Autonomous:** `{class_res.get('Is Autonomous')}`")
        
        ivp_dict = {}
        if ivp_input.strip():
            for cond in ivp_input.split(','):
                k, v = cond.split('=')
                ivp_dict[k.strip()] = float(v.strip())
                
        sol_res = solve_symbolic_ode(eq_input, ivp=ivp_dict)
        if sol_res["Status"] == "Success":
            st.success("✅ Analytical Solution Found & Verified via Residual Elimination")
            st.latex(sp.latex(sol_res["General/Particular Solution"]))
        else:
            st.error(sol_res["Error"])

    with tabs[2]:
        st.header("Boundary Value Problems (BVP)")
        st.markdown("Solves $y'' + p(x)y' + q(x)y = r(x)$ subjected to $y(a) = \alpha$, $y(b) = \beta$.")
        b1, b2, b3 = st.columns(3)
        with b1: a_val = st.number_input("Left Bound (a):", value=0.0)
        with b1: alpha_val = st.number_input("y(a) = alpha:", value=0.0)
        with b2: b_val = st.number_input("Right Bound (b):", value=3.14159)
        with b2: beta_val = st.number_input("y(b) = beta:", value=0.0)
        with b3: method = st.selectbox("BVP Method:", ["Finite Difference", "Shooting Method"])
        
        if method == "Finite Difference":
            st.info("Using Central Finite Difference Matrix Discretization.")
            # Default to simple harmonic oscillator y'' + y = 0
            res_bvp = finite_difference_bvp_linear(lambda x: 0, lambda x: 1, lambda x: 0, a_val, b_val, alpha_val, beta_val, n=50)
            if res_bvp["Status"] == "Success":
                st.pyplot(plot_bvp_solution(res_bvp["x"], res_bvp["y"], "Finite Difference BVP Solution"))
            else:
                st.error(res_bvp["Status"])
        else:
            st.info("Using Shooting Method via Newton-Secant Root Finding & RK4.")
            # u1' = u2, u2' = -u1
            f_sys = lambda x, Y: np.array([Y[1], -Y[0]])
            shoot_res = shooting_method(f_sys, a_val, b_val, alpha_val, beta_val, v_guess1=-1.0, v_guess2=1.0, h=0.05)
            if shoot_res["Status"] == "Converged":
                st.success(f"Converged in {shoot_res['Iterations']} iterations. Optimal $y'(a)$ = {shoot_res['Initial Slope y'(a)']}")
                st.pyplot(plot_bvp_solution(shoot_res["x"], shoot_res["y"], "Shooting Method BVP Solution"))
            else:
                st.error(shoot_res["Status"])

    with tabs[3]:
        st.header("Numerical Error Control & Isoclines")
        iso_eq = st.text_input("dy/dx = f(x,y):", "x - y")
        st.pyplot(plot_isoclines(iso_eq, (-3, 3), (-3, 3), c_values=[-2, -1, 0, 1, 2]))
        st.markdown("Isoclines trace paths where the slope field is strictly constant $f(x,y) = C$.")

    with tabs[4]:
        st.header("Phase Space, Equilibria & Stability")
        dx_dt = st.text_input("dx/dt = f(x,y):", "x - x*y") # Lotka Volterra
        dy_dt = st.text_input("dy/dt = g(x,y):", "x*y - y")
        
        st.pyplot(plot_phase_portrait([dx_dt, dy_dt], "x, y", (-1, 3), (-1, 3)))
        
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
