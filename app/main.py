# ... [Keep Milestones 1 to 11 unchanged] ...

elif page == "Milestone 12: Multiple Integrals":
    st.title("Advanced Multiple Integrals & Multivariable Analysis")
    st.markdown("Evaluate iterated integrals, calculate Jacobians, analyze physical laminas, and benchmark Monte Carlo stochastic integration.")
    
    from calculus.multivariable.multivariable_engine import MultivariableEngine
    from calculus.multiple_integrals.double_integrals import compute_double_integral, change_integration_order
    from calculus.multiple_integrals.triple_integrals import compute_triple_integral
    from calculus.multiple_integrals.coordinate_transformations import get_polar_transformation, get_cylindrical_transformation, get_spherical_transformation
    from calculus.multiple_integrals.jacobian_integration import apply_coordinate_transformation
    from calculus.multiple_integrals.applications import compute_lamina_properties
    from calculus.multiple_integrals.multiple_integral_analysis import monte_carlo_double_integral, monte_carlo_convergence_study
    from visualization.multiple_integral_plots import plot_double_integral_region, plot_monte_carlo_samples
    
    tabs = st.tabs(["Iterated Integrals & Area", "Coordinate Transformations", "Physical Applications", "Monte Carlo & Numerical"])

    with tabs[0]:
        st.header("Double & Triple Integrals")
        
        st.subheader("1. Double Integral over Rectangular Region $D$")
        c1, c2, c3 = st.columns([2, 1, 1])
        with c1: d_expr = st.text_input("Integrand $f(x,y)$:", value="x^2 + y^2")
        with c2: xb = st.text_input("x bounds (a, b):", "0, 2")
        with c3: yb = st.text_input("y bounds (c, d):", "0, 3")
        
        try:
            m_eng = MultivariableEngine(d_expr, "x, y")
            x_bnds = tuple(float(v.strip()) for v in xb.split(','))
            y_bnds = tuple(float(v.strip()) for v in yb.split(','))
            
            d_res = compute_double_integral(m_eng, x_bnds, y_bnds, "yx")
            
            st.latex(r"\iint_D " + sp.latex(m_eng.expression) + r" \, dA = " + sp.latex(d_res.get("Exact Result", "Error")))
            st.write(f"- **Numerical Value:** `{d_res.get('Numerical Result')}`")
            st.write(f"- **Region Type:** `{d_res.get('Region Type')}`")
            
            st.info("**Fubini's Theorem Check:** Reversing integration order...")
            fubini = change_integration_order(m_eng, x_bnds, y_bnds)
            st.write(f"- dx dy Result: `{fubini['dx dy Result']}`")
            st.write(f"- dy dx Result: `{fubini['dy dx Result']}`")
            if fubini["Fubini Theorem Holds"]:
                st.success("✅ Fubini's Theorem verified: Both orders yield identical results over the constant domain.")
                
            st.pyplot(plot_double_integral_region(x_bnds, y_bnds))
                
        except Exception as e:
            st.error(f"Error computing double integral: {e}")
            
        st.divider()
        st.subheader("2. Triple Integral (Iterated)")
        t_expr = st.text_input("Integrand $f(x,y,z)$:", value="x * y * z")
        zb = st.text_input("z bounds (e, f):", "0, 1")
        if st.button("Compute Triple Integral"):
            t_eng = MultivariableEngine(t_expr, "x, y, z")
            z_bnds = tuple(float(v.strip()) for v in zb.split(','))
            t_res = compute_triple_integral(t_eng, x_bnds, y_bnds, z_bnds)
            st.latex(r"\iiint_V " + sp.latex(t_eng.expression) + r" \, dV = " + sp.latex(t_res.get("Exact Result", "Error")))

    with tabs[1]:
        st.header("Coordinate Transformations & Jacobians")
        st.markdown(r"Transforms $f(x,y,z)$ into new coordinates, calculates Jacobian $|J|$, and returns $f(u,v,w)|J|$.")
        
        system = st.selectbox("Select Target Coordinate System:", ["Polar (2D)", "Cylindrical (3D)", "Spherical (3D)"])
        jac_expr = st.text_input("Cartesian Integrand:", value="x^2 + y^2")
        
        if st.button("Apply Transformation"):
            j_eng = MultivariableEngine(jac_expr, "x, y, z" if "3D" in system else "x, y")
            if system == "Polar (2D)": trans = get_polar_transformation()
            elif system == "Cylindrical (3D)": trans = get_cylindrical_transformation()
            else: trans = get_spherical_transformation()
            
            j_res = apply_coordinate_transformation(j_eng.expression, trans)
            
            st.write(f"- **Substitution Map:** `{j_res['Substitutions']}`")
            st.write(f"- **Transformed $f(u,v)$:** `{j_res['f(u,v)']}`")
            st.latex(r"\text{Jacobian Determinant } J = " + sp.latex(j_res['Jacobian Determinant (J)']))
            st.latex(r"\text{Absolute Jacobian Factor } |J| = " + sp.latex(j_res['Absolute Jacobian Factor |J|']))
            st.latex(r"\text{Final Integrand } f \cdot |J| = " + sp.latex(j_res['Final Integrand f(u,v)|J|']))

    with tabs[2]:
        st.header("Physical Applications: Laminas")
        st.markdown("Calculates Mass, Centroid, and Moments of Inertia for a 2D plate with variable density $\\rho(x,y)$.")
        
        rho_input = st.text_input("Density $\\rho(x,y)$:", value="x + y")
        if st.button("Compute Lamina Properties"):
            lam_res = compute_lamina_properties(rho_input, x_bnds, y_bnds)
            if lam_res["Status"] == "Success":
                st.write(f"- **Mass (M):** `{lam_res['Mass (M)']}`")
                st.write(f"- **Centroid $(\\bar{x}, \\bar{y})$:** `{lam_res['Centroid (x_bar, y_bar)']}`")
                st.write(f"- **Moments ($M_x, M_y$):** `{lam_res['Moment M_x']}, {lam_res['Moment M_y']}`")
                st.write(f"- **Moments of Inertia ($I_x, I_y, I_0$):** `{lam_res['Inertia I_x']}, {lam_res['Inertia I_y']}, {lam_res['Polar Inertia I_0']}`")
            else:
                st.error(lam_res["Error"])

    with tabs[3]:
        st.header("Monte Carlo Integration & Convergence")
        st.markdown(r"Estimates $\iint_D f(x,y) dA$ via random uniform sampling. Expected to converge at rate $O(1/\sqrt{N})$.")
        
        mc_n = st.selectbox("Sample Count ($N$):", [1000, 10000, 100000, 1000000], index=1)
        
        if st.button("Run Monte Carlo Estimate"):
            mc_res = monte_carlo_double_integral(m_eng, x_bnds, y_bnds, N=mc_n)
            exact_val = compute_double_integral(m_eng, x_bnds, y_bnds)["Numerical Result"]
            
            st.metric("Monte Carlo Estimate", f"{mc_res['Estimate']:.5f}", delta=f"Error: {abs(mc_res['Estimate'] - exact_val):.5f}")
            st.write(f"- **Statistical Uncertainty ($\pm 1\sigma$):** `{mc_res['Statistical Uncertainty']}`")
            
            st.pyplot(plot_monte_carlo_samples(m_eng, x_bnds, y_bnds, mc_res))
            
            st.divider()
            st.subheader("Law of Large Numbers: Convergence Study")
            study = monte_carlo_convergence_study(m_eng, x_bnds, y_bnds, exact_val)
            st.dataframe(pd.DataFrame(study), use_container_width=True)
            st.info("Notice how absolute error decreases slowly as N increases by powers of 10.")
