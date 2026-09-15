# ... [Keep Milestones 1 to 10 unchanged] ...

elif page == "Milestone 11: Multivariable Calculus":
    st.title("Advanced Multivariable Calculus Laboratory")
    st.markdown("Analyze partial derivatives, gradients, critical points, and multiple integrals.")
    
    from calculus.multivariable.multivariable_engine import MultivariableEngine
    from calculus.multivariable.partial_derivatives import compute_partial, compare_mixed_partials
    from calculus.multivariable.gradient import compute_gradient, evaluate_gradient
    from calculus.multivariable.directional_derivatives import directional_derivative
    from calculus.multivariable.tangent_plane import compute_tangent_plane
    from calculus.multivariable.jacobian import compute_jacobian
    from calculus.multivariable.critical_points import find_multivariable_critical_points
    from calculus.multivariable.optimization import lagrange_multipliers
    from calculus.multivariable.multivariable_analysis import path_limit_exploration
    from calculus.multivariable.multiple_integrals import double_integral_rectangular
    from visualization.multivariable_plots import plot_3d_surface, plot_contours_and_gradients
    
    tabs = st.tabs(["Surfaces & Gradients", "Derivatives & Tangents", "Critical Points & Hessian", "Lagrange Optimization", "Multiple Integrals", "Jacobian"])

    c1, c2 = st.columns(2)
    with c1: expr_input = st.text_input("Scalar Field $f(x,y)$:", value="x^2 - y^2")
    with c2: point_input = st.text_input("Evaluation Point (a, b):", value="1.0, 1.0")
    
    try:
        m_eng = MultivariableEngine(expr_input)
        pt = [float(p.strip()) for p in point_input.split(',')]
        x, y = m_eng.vars
    except Exception as e:
        st.error(f"Initialization Error: {e}")
        st.stop()

    with tabs[0]:
        st.header("3D Surface & Contour Mapping")
        v1, v2 = st.columns(2)
        with v1:
            st.pyplot(plot_3d_surface(m_eng, (-3, 3), (-3, 3)))
        with v2:
            st.pyplot(plot_contours_and_gradients(m_eng, (-3, 3), (-3, 3)))
            
        st.divider()
        st.subheader("Multivariable Path Limits")
        st.markdown(r"Evaluating $\lim_{(x,y) \to (a,b)}$ along standard paths.")
        st.json(path_limit_exploration(m_eng, pt))

    with tabs[1]:
        st.header("Partial Derivatives, Gradients & Tangent Planes")
        st.latex(r"\nabla f = \left\langle \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right\rangle = " + sp.latex(compute_gradient(m_eng)["Gradient"]))
        
        st.subheader("Directional Derivative")
        u_str = st.text_input("Direction Vector (v_x, v_y):", "1, 1")
        u_vec = [float(u.strip()) for u in u_str.split(',')]
        d_res = directional_derivative(m_eng, u_vec, pt)
        st.write(f"- **Unit Direction:** `{d_res['Unit Vector']}`")
        st.write(f"- **Directional Derivative $D_u f(a,b)$:** `{d_res['Evaluated D_u']}`")
        st.write(f"- **Maximum Rate of Change ($|\\nabla f|$):** `{d_res['Max Rate of Change']}`")
        
        st.divider()
        st.subheader("Tangent Plane & Linear Approximation")
        tp_res = compute_tangent_plane(m_eng, pt)
        st.latex("z = f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b)")
        st.latex(f"L(x,y) = {sp.latex(tp_res.get('Tangent Plane Equation', 'Error'))}")
        st.info(f"**Differential:** $df = {sp.latex(tp_res.get('Differential df', 'Error'))}$")

    with tabs[2]:
        st.header("Critical Points & Second Derivative Test")
        st.markdown(r"Finds where $\nabla f = \vec{0}$ and evaluates the Hessian Discriminant $D = f_{xx}f_{yy} - (f_{xy})^2$.")
        
        crits = find_multivariable_critical_points(m_eng)
        if crits:
            for c in crits:
                st.markdown(f"**Point:** `{c['Point']}`")
                st.json(c["Classification"])
        else:
            st.warning("No critical points found or system too complex for symbolic solver.")

    with tabs[3]:
        st.header("Constrained Optimization: Lagrange Multipliers")
        st.markdown(r"Solves $\nabla f = \lambda \nabla g$ subject to $g(x,y) = 0$.")
        g_input = st.text_input("Constraint Equation $g(x,y) = 0$ (e.g. x^2 + y^2 - 1):", value="x^2 + y^2 - 1")
        if st.button("Solve System"):
            l_res = lagrange_multipliers(m_eng, g_input)
            st.json(l_res)

    with tabs[4]:
        st.header("Double Integrals over Rectangular Domains")
        st.markdown(r"$\iint_D f(x,y) \, dA$ represents the signed volume under the surface.")
        i1, i2 = st.columns(2)
        with i1: x_bnds = st.text_input("x bounds (c, d):", "0, 1")
        with i2: y_bnds = st.text_input("y bounds (a, b):", "0, 1")
        
        if st.button("Compute Double Integral"):
            xb = tuple(x_bnds.split(','))
            yb = tuple(y_bnds.split(','))
            int_res = double_integral_rectangular(m_eng, xb, yb)
            st.write(f"**Exact Integral:** `{int_res['Final Exact Integral']}`")
            st.write(f"**Numerical Value:** `{int_res['Numerical Value']}`")
            st.info(int_res["Interpretation"])

    with tabs[5]:
        st.header("Jacobian Matrix & Transformations")
        st.markdown(r"For transformations $F(u, v) = (x(u,v), y(u,v))$:")
        j1, j2 = st.columns(2)
        with j1: eq1 = st.text_input("Function 1 (e.g., r*cos(theta)):", "r*cos(theta)")
        with j2: eq2 = st.text_input("Function 2 (e.g., r*sin(theta)):", "r*sin(theta)")
        v_str = st.text_input("Variables:", "r, theta")
        
        j_res = compute_jacobian([eq1, eq2], v_str)
        st.latex("J = " + sp.latex(j_res["Jacobian Matrix"]))
        st.markdown(f"**Jacobian Determinant $|J|$:**")
        st.latex(sp.latex(j_res["Determinant"]))
