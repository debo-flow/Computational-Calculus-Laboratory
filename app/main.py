# ... [Keep Milestones 1 to 12 unchanged] ...

elif page == "Milestone 13: Vector Calculus":
    st.title("Advanced Vector Calculus Laboratory")
    st.markdown("Analyze parametric curves, vector fields, operators, and fundamental theorems.")

    from calculus.vector_calculus.vector_engine import VectorFunctionEngine
    from calculus.vector_calculus.vector_fields import VectorFieldEngine
    from calculus.vector_calculus.vector_functions import compute_kinematics, compute_arc_length
    from calculus.vector_calculus.curvature import compute_curvature_and_tangent
    from calculus.vector_calculus.divergence import compute_divergence
    from calculus.vector_calculus.curl import compute_curl
    from calculus.vector_calculus.laplacian import compute_scalar_laplacian
    from calculus.vector_calculus.line_integrals import vector_line_integral
    from calculus.vector_calculus.flux import compute_flux
    from calculus.vector_calculus.theorems import verify_greens_theorem, verify_divergence_theorem
    from visualization.vector_calculus_plots import plot_2d_vector_field, plot_parametric_curve_3d

    tabs = st.tabs([
        "Parametric Curves & Kinematics", 
        "Vector Fields (Div, Curl, Laplacian)", 
        "Line Integrals & Work", 
        "Surface Integrals & Flux", 
        "Vector Theorems"
    ])

    with tabs[0]:
        st.header("Parametric Curves $r(t) = \\langle x(t), y(t), z(t) \\rangle$")
        c1, c2, c3 = st.columns(3)
        with c1: x_t = st.text_input("x(t):", "cos(t)")
        with c2: y_t = st.text_input("y(t):", "sin(t)")
        with c3: z_t = st.text_input("z(t):", "t")

        try:
            r_eng = VectorFunctionEngine([x_t, y_t, z_t])
            kin = compute_kinematics(r_eng)
            curv = compute_curvature_and_tangent(r_eng)
            
            st.latex(r"r(t) = \langle " + sp.latex(r_eng.components[0]) + ", " + sp.latex(r_eng.components[1]) + ", " + sp.latex(r_eng.components[2]) + r"\rangle")
            st.write(f"- **Velocity $v(t)$:** `{kin['Velocity (v)']}`")
            st.write(f"- **Acceleration $a(t)$:** `{kin['Acceleration (a)']}`")
            st.write(f"- **Speed $\vert{}v(t)\vert{}$:** `{kin['Speed (|v|)']}`")
            st.write(f"- **Unit Tangent $T(t)$:** `{curv['Unit Tangent (T)']}`")
            st.write(f"- **Curvature $\kappa(t)$:** `{curv['Curvature (kappa)']}`")
            
            st.subheader("Arc Length $L = \int \vert{}r'(t)\vert{} dt$")
            l1, l2 = st.columns(2)
            with l1: t_start = st.number_input("t start:", value=0.0)
            with l2: t_end = st.number_input("t end:", value=6.28318)
            l_res = compute_arc_length(r_eng, t_start, t_end)
            st.write(f"**Arc Length Exact:** `{l_res.get('Integral')}` | **Numerical:** `{l_res.get('Numerical')}`")
            
            st.pyplot(plot_parametric_curve_3d(x_t, y_t, z_t, (t_start, t_end)))
        except Exception as e:
            st.error(str(e))

    with tabs[1]:
        st.header("Vector Fields $F(x,y,z) = \\langle P, Q, R \\rangle$")
        v1, v2, v3 = st.columns(3)
        with v1: P_x = st.text_input("P(x,y,z):", "-y")
        with v2: Q_x = st.text_input("Q(x,y,z):", "x")
        with v3: R_x = st.text_input("R(x,y,z):", "0")
        
        try:
            f_eng = VectorFieldEngine([P_x, Q_x, R_x])
            div = compute_divergence(f_eng)
            curl = compute_curl(f_eng)
            
            st.write(f"- **Divergence $\\nabla \cdot F$:** `{div}`")
            st.write(f"- **Curl $\\nabla \\times F$:** `{curl}`")
            
            if div == 0: st.info("Field is Incompressible (Divergence = 0)")
            if curl == [0, 0, 0]: st.info("Field is Irrotational/Conservative (Curl = 0). Note: Depends on simply connected domain.")
            
            st.subheader("Scalar Laplacian $\\nabla^2 f$")
            scalar_f = st.text_input("Scalar f(x,y,z):", "x^2 + y^2 + z^2")
            st.write(f"**Laplacian:** `{compute_scalar_laplacian(scalar_f)}`")
            
            st.pyplot(plot_2d_vector_field(P_x, Q_x, (-3, 3), (-3, 3)))
        except Exception as e:
            st.error(str(e))

    with tabs[2]:
        st.header("Vector Line Integrals & Work")
        st.markdown(r"$W = \int_C F \cdot dr$")
        if st.button("Compute Work using Curve $r(t)$ and Field $F$"):
            w_res = vector_line_integral(f_eng, r_eng, t_start, t_end)
            st.write(f"- **Integrand $F \cdot dr$:** `{w_res.get('Integrand (F·dr)')}`")
            st.write(f"- **Work Exact:** `{w_res.get('Exact')}`")
            st.write(f"- **Work Numerical:** `{w_res.get('Numerical')}`")

    with tabs[3]:
        st.header("Surface Integrals & Flux")
        st.markdown(r"$\Phi = \iint_S F \cdot n \, dS$")
        s1, s2, s3 = st.columns(3)
        with s1: ru = st.text_input("x(u,v):", "u")
        with s2: rv = st.text_input("y(u,v):", "v")
        with s3: rw = st.text_input("z(u,v):", "u^2 + v^2")
        
        b1, b2 = st.columns(2)
        with b1: u_bounds = st.text_input("u bounds (start, end):", "0, 1")
        with b2: v_bounds = st.text_input("v bounds (start, end):", "0, 1")
        
        if st.button("Compute Flux"):
            ub = tuple(float(x) for x in u_bounds.split(','))
            vb = tuple(float(x) for x in v_bounds.split(','))
            flux_res = compute_flux(f_eng, [ru, rv, rw], "u, v", ub, vb)
            st.write(f"- **Normal Vector $n$:** `{flux_res.get('Normal (n)')}`")
            st.write(f"- **Exact Flux:** `{flux_res.get('Exact Flux')}`")
            st.write(f"- **Numerical Flux:** `{flux_res.get('Numerical')}`")

    with tabs[4]:
        st.header("Fundamental Theorems of Vector Calculus")
        st.markdown("Computationally verify major theorems over basic standard domains (e.g., box domains).")
        
        t_col1, t_col2 = st.columns(2)
        with t_col1:
            st.subheader("Green's Theorem")
            st.markdown(r"$\oint_C P dx + Q dy = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dA$")
            g_res = verify_greens_theorem(f_eng, (0, 1), (0, 1))
            st.write(f"- **Curl / Integrand:** `{g_res['Curl (Q_x - P_y)']}`")
            st.write(f"- **RHS Area Evaluation:** `{g_res['RHS (Area Integral)']}`")
            
        with t_col2:
            st.subheader("Divergence Theorem")
            st.markdown(r"$\oiint_S F \cdot n \, dS = \iiint_V \nabla \cdot F \, dV$")
            d_res = verify_divergence_theorem(f_eng, (0, 1), (0, 1), (0, 1))
            st.write(f"- **Divergence:** `{d_res['Divergence (∇·F)']}`")
            st.write(f"- **RHS Volume Evaluation:** `{d_res['RHS (Volume Integral)']}`")
