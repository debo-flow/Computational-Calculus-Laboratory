# ... [Keep Milestones 1 to 20 unchanged] ...

elif page == "Milestone 21: Tensor Geometry":
    st.title("Advanced Tensor Calculus & Differential Geometry Laboratory")
    st.markdown("Analyze metric tensors, derive Christoffel symbols, compute Riemannian curvature, and visualize intrinsic surface geometry.")

    from calculus.tensor_geometry.metric import compute_metric_properties, raise_lower_index
    from calculus.tensor_geometry.christoffel import compute_christoffel_symbols
    from calculus.tensor_geometry.curvature import compute_riemann_tensor, compute_ricci_tensor, compute_scalar_curvature
    from calculus.tensor_geometry.geodesics import generate_geodesic_odes
    from calculus.tensor_geometry.differential_geometry import compute_surface_geometry
    from calculus.tensor_geometry.geometry_analysis import compute_exterior_derivative_1form
    from visualization.tensor_geometry_plots import plot_surface_with_curvature

    tabs = st.tabs([
        "Metric & Connections (Christoffel)", 
        "Riemann Curvature (Tensors)", 
        "Differential Geometry (Surfaces)", 
        "Differential Forms"
    ])

    with tabs[0]:
        st.header("Metric Tensors & Christoffel Symbols")
        st.markdown(r"Given a metric $g_{ij}$, calculates the inverse $g^{ij}$ and connection coefficients $\Gamma^k_{ij}$.")
        
        c1, c2 = st.columns(2)
        with c1: vars_in = st.text_input("Coordinates (e.g. r, theta):", "r, theta")
        with c2: metric_in = st.text_input("Metric Matrix g_ij (comma separated rows):", "[1, 0], [0, r^2]")
        
        if st.button("Compute Metric & Connections"):
            try:
                var_syms = sp.symbols(vars_in)
                rows = [sp.sympify(row) for row in metric_in.split('],')]
                g_mat = sp.Matrix(rows)
                
                m_res = compute_metric_properties(g_mat)
                if m_res["Status"] == "Success":
                    st.latex(r"g_{ij} = " + sp.latex(m_res['g_ij']))
                    st.latex(r"g^{ij} = " + sp.latex(m_res['g^ij']))
                    st.write(f"**Metric Determinant ($g$):** `{m_res['Determinant (g)']}`")
                    
                    Gamma = compute_christoffel_symbols(m_res['g_ij'], m_res['g^ij'], var_syms)
                    st.subheader("Non-Zero Christoffel Symbols $\Gamma^k_{ij}$")
                    
                    found_any = False
                    for k in range(len(var_syms)):
                        for i in range(len(var_syms)):
                            for j in range(len(var_syms)):
                                if Gamma[k][i][j] != 0:
                                    st.latex(rf"\Gamma^{var_syms[k]}_{{{var_syms[i]}{var_syms[j]}}} = " + sp.latex(Gamma[k][i][j]))
                                    found_any = True
                    if not found_any:
                        st.info("All Christoffel symbols are zero (Flat space in Cartesian coordinates).")
                        
                    st.subheader("Geodesic Equations")
                    st.markdown(r"$\frac{d^2 x^k}{d\lambda^2} + \Gamma^k_{ij} \frac{dx^i}{d\lambda}\frac{dx^j}{d\lambda} = 0$")
                    geo_odes = generate_geodesic_odes(Gamma, var_syms)
                    for k, ode in enumerate(geo_odes):
                        st.latex(rf"\frac{{d^2 {var_syms[k]}}}{{d\lambda^2}} = " + sp.latex(ode))
                        
            except Exception as e:
                st.error(f"Error parsing metric: {e}")

    with tabs[1]:
        st.header("Riemann, Ricci, and Scalar Curvature")
        st.markdown("Derives intrinsic curvature tensors strictly from the metric and connections.")
        if st.button("Compute Curvature Tensors (requires metric above)"):
            if 'm_res' in locals() and m_res["Status"] == "Success":
                R_tensor = compute_riemann_tensor(Gamma, var_syms)
                Ricci = compute_ricci_tensor(R_tensor, len(var_syms))
                R_scalar = compute_scalar_curvature(Ricci, m_res['g^ij'], len(var_syms))
                
                st.subheader("Ricci Tensor $R_{ij}$")
                st.latex(r"R_{ij} = " + sp.latex(Ricci))
                st.subheader("Scalar Curvature $R$")
                st.latex(r"R = " + sp.latex(R_scalar))
                if R_scalar == 0:
                    st.success("Scalar Curvature is 0 (Space is flat or Ricci-flat).")
            else:
                st.warning("Please compute the metric in the previous tab first.")

    with tabs[2]:
        st.header("Differential Geometry of Surfaces")
        st.markdown(r"Computes First ($E, F, G$) and Second ($e, f, g$) Fundamental Forms, and intrinsic curvatures for parametrized surfaces $\vec{r}(u,v)$.")
        
        s1, s2, s3 = st.columns(3)
        with s1: x_s = st.text_input("x(u,v):", "cos(u)*sin(v)") # Sphere R=1
        with s2: y_s = st.text_input("y(u,v):", "sin(u)*sin(v)")
        with s3: z_s = st.text_input("z(u,v):", "cos(v)")
        
        if st.button("Analyze Surface Geometry"):
            s_res = compute_surface_geometry(x_s, y_s, z_s, "u, v")
            if s_res["Status"] == "Success":
                c3, c4 = st.columns(2)
                with c3:
                    st.write(f"- **First Fundamental Form (E, F, G):** `{s_res['E']}`, `{s_res['F']}`, `{s_res['G']}`")
                    st.write(f"- **Second Fundamental Form (e, f, g):** `{s_res['e']}`, `{s_res['f']}`, `{s_res['g']}`")
                with c4:
                    st.write(f"- **Gaussian Curvature ($K$):** `{s_res['Gaussian Curvature (K)']}`")
                    st.write(f"- **Mean Curvature ($H$):** `{s_res['Mean Curvature (H)']}`")
                    
                st.pyplot(plot_surface_with_curvature(x_s, y_s, z_s, "u, v", (0, 2*np.pi), (0.01, np.pi-0.01), s_res['Gaussian Curvature (K)']))
            else:
                st.error(s_res["Error"])

    with tabs[3]:
        st.header("Differential Forms & Exterior Derivative")
        st.markdown(r"Evaluates the exterior derivative $d\omega$ of a 1-form $\omega = P dx + Q dy + R dz$.")
        w1, w2, w3 = st.columns(3)
        with w1: w_p = st.text_input("P(x,y,z):", "-y", key="wp")
        with w2: w_q = st.text_input("Q(x,y,z):", "x", key="wq")
        with w3: w_r = st.text_input("R(x,y,z):", "z", key="wr")
        
        if st.button("Compute $d\omega$"):
            form_res = compute_exterior_derivative_1form(w_p, w_q, w_r, "x, y, z")
            st.latex(rf"d\omega = ({sp.latex(form_res['dy ∧ dz'])}) dy \wedge dz + ({sp.latex(form_res['dz ∧ dx'])}) dz \wedge dx + ({sp.latex(form_res['dx ∧ dy'])}) dx \wedge dy")
            st.info(form_res["Interpretation"])
