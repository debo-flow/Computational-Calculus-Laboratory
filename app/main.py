# ... [Keep Milestones 1 to 19 unchanged] ...

elif page == "Milestone 20: Calculus of Variations":
    st.title("Advanced Calculus of Variations & Functional Optimization")
    st.markdown("Derive Euler-Lagrange equations, compute first variations, and minimize action functionals $J[y]$.")

    from calculus.variations.functional import Functional
    from calculus.variations.euler_lagrange import derive_euler_lagrange
    from calculus.variations.variational_derivatives import compute_first_variation
    from calculus.variations.extremals import solve_extremal
    from calculus.variations.numerical_variations import numerical_functional_optimization
    from calculus.variations.variation_analysis import calculate_el_residual
    from calculus.variations.constraints import setup_isoperimetric_problem
    from visualization.variation_plots import plot_extremal_comparison, plot_el_residual

    tabs = st.tabs([
        "Symbolic Euler-Lagrange", 
        "Numerical Functional Optimization", 
        "Variations & Perturbations", 
        "Isoperimetric & Constraints"
    ])

    with tabs[0]:
        st.header("Euler-Lagrange Extrema Generation")
        st.markdown(r"For $J[y] = \int_a^b F(x, y, y') dx$, a necessary condition for an extremal is $\frac{\partial F}{\partial y} - \frac{d}{dx}\left(\frac{\partial F}{\partial y'}\right) = 0$.")
        
        st.info("Notation: Use `y` for $y(x)$, `yp` for $y'(x)$, and `ypp` for $y''(x)$.")
        f_input = st.text_input("Integrand F(x, y, y'):", value="sqrt(1 + yp^2)", key="f1")
        
        if st.button("Derive Euler-Lagrange Equation"):
            fnc = Functional(f_input)
            el_data = derive_euler_lagrange(fnc)
            
            st.write(f"- **$\partial F / \partial y$:** `{el_data['∂F/∂y']}`")
            st.write(f"- **$\partial F / \partial y'$:** `{el_data['∂F/∂y\'']}`")
            st.write(f"- **$d/dx (\partial F / \partial y')$:** `{el_data['d/dx(∂F/∂y\')']}`")
            st.latex(r"\text{Euler-Lagrange Equation: } " + sp.latex(el_data["EL Equation"]))
            
            ext_res = solve_extremal(fnc)
            if ext_res["Status"] == "Success":
                st.success("✅ Symbolic Candidate Extremal Found:")
                st.latex(sp.latex(ext_res["Candidate Extremal"]))
            else:
                st.warning(f"Symbolic integration failed or ODE is non-elementary. Use the Numerical Optimizer. ({ext_res.get('Error', '')})")

    with tabs[1]:
        st.header("Numerical Discretization & Direct Minimization")
        st.markdown("Approximates the continuous functional $J[y]$ using a finite grid and minimizes the resulting multivariable function via BFGS.")
        
        c1, c2, c3, c4 = st.columns(4)
        with c1: a_val = st.number_input("x_a:", value=0.0)
        with c2: b_val = st.number_input("x_b:", value=1.0)
        with c3: y_a = st.number_input("y(a):", value=0.0)
        with c4: y_b = st.number_input("y(b):", value=1.0)
        
        f_num_in = st.text_input("Integrand F(x,y,y') for minimization:", value="0.5 * yp^2") # Dirichlet Energy -> Straight line
        
        if st.button("Run Numerical Functional Optimization"):
            fnc_num = Functional(f_num_in)
            res_opt = numerical_functional_optimization(fnc_num, a_val, b_val, y_a, y_b, N=40)
            
            if res_opt["Status"] == "Converged":
                st.success(f"✅ Minimization Converged in {res_opt['Iterations']} iterations. Optimal $J[y] \approx {res_opt['J_min']:.6f}$")
                
                # Try to get symbolic reference for plot
                sym_sol = solve_extremal(fnc_num, {"a": a_val, "b": b_val, "A": y_a, "B": y_b})
                ref_expr = sym_sol["Candidate Extremal"].rhs if sym_sol["Status"] == "Success" else None
                
                st.pyplot(plot_extremal_comparison(res_opt["x"], res_opt["y"], ref_expr, a_val, b_val))
                
                st.subheader("Euler-Lagrange Residual Check")
                st.markdown("If the numerical profile is a true extremal, the residual $R(x)$ of the EL equation should locally approach 0.")
                resid = calculate_el_residual(fnc_num, res_opt["x"], res_opt["y"])
                st.pyplot(plot_el_residual(res_opt["x"][1:-1], resid[1:-1])) # Trim noisy edges
            else:
                st.error(res_opt["Message"])

    with tabs[2]:
        st.header("First Variation & Trial Functions")
        st.markdown(r"Evaluates $\delta J = \frac{d}{d\epsilon} J[y + \epsilon \eta] \big\vert{}_{\epsilon=0}$")
        v_input = st.text_input("Integrand F:", "yp^2", key="f2")
        
        if st.button("Compute First Variation"):
            v_fnc = Functional(v_input)
            v_res = compute_first_variation(v_fnc)
            st.latex(r"\delta F = " + sp.latex(v_res["First Variation δF"]))
            st.info(v_res["Interpretation"])
            
        st.divider()
        st.subheader("Trial Function Evaluator")
        trial_str = st.text_input("Trial Function y(x):", "x^2")
        if st.button("Evaluate Functional J[y]"):
            v_fnc = Functional(v_input)
            e_res = v_fnc.evaluate_trial_function(trial_str, 0, 1)
            if "Error" not in e_res:
                st.latex(r"J[y_{trial}] = \int_0^1 \left(" + sp.latex(e_res["Evaluated Integrand"]) + r"\right) dx = " + str(e_res["Exact J"]))
            else:
                st.error(e_res["Error"])

    with tabs[3]:
        st.header("Constrained Variational Problems")
        st.markdown("Constructs the modified Lagrangian $H = F + \lambda G$ for Isoperimetric problems.")
        iso_F = st.text_input("Objective Integrand F (e.g. maximize area):", "y")
        iso_G = st.text_input("Constraint Integrand G (e.g. fixed perimeter):", "sqrt(1 + yp^2)")
        
        if st.button("Generate Modified Problem"):
            iso_res = setup_isoperimetric_problem(iso_F, iso_G)
            st.latex(r"H = F + \lambda G = " + sp.latex(iso_res["Modified Integrand H"]))
            st.info("Applying the Euler-Lagrange generator to $H$ yields the constrained extremal.")
