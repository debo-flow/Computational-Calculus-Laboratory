# ... [Keep Milestones 1 to 9 unchanged] ...

elif page == "Milestone 10: Taylor & Maclaurin Series":
    st.title("Advanced Taylor & Maclaurin Series Laboratory")
    st.markdown("Generate Taylor polynomials, analyze Lagrange error bounds, and visualize local convergence.")
    
    from calculus.taylor.taylor_engine import TaylorEngine
    from calculus.taylor.taylor_analysis import calculus_on_taylor
    from visualization.taylor_plots import plot_taylor_approximation, plot_taylor_error_map

    c1, c2, c3 = st.columns([2, 1, 1])
    with c1: expr_input = st.text_input("Function f(x):", value="exp(x)")
    with c2: a_input = st.number_input("Expansion Point (a):", value=0.0)
    with c3: order_input = st.number_input("Order (n):", value=3, min_value=0, max_value=30)
    
    try:
        engine = FunctionEngine(expr_input)
        t_engine = TaylorEngine(engine, a=a_input)
        T_n = t_engine.get_polynomial(order_input)
        
        st.latex(f"T_{{{order_input}}}(x) = {sp.latex(T_n)}")
        
        tabs = st.tabs(["Polynomial & Coefficients", "Error & Remainder Bounds", "Convergence & Verification", "Visualization"])
        
        with tabs[0]:
            st.header("Taylor Coefficients & Expansion")
            st.markdown(r"Taylor Series formula: $f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} (x-a)^n$")
            
            coeffs = t_engine.get_coefficients(order_input)
            df_coeffs = pd.DataFrame(coeffs)
            df_coeffs["c_n"] = df_coeffs["c_n"].astype(str)
            df_coeffs["f^(n)(a)"] = df_coeffs["f^(n)(a)"].astype(str)
            st.dataframe(df_coeffs, use_container_width=True)
            
            st.subheader("Calculus on Taylor Polynomials")
            st.markdown("Notice how differentiating $T_n(x)$ approximates $f'(x)$ at order $n-1$.")
            calc_res = calculus_on_taylor(t_engine.poly, order_input)
            st.latex(r"\frac{d}{dx}[T_n(x)] = " + sp.latex(calc_res["d/dx [T_n(x)]"]))
            
        with tabs[1]:
            st.header("Remainder & Error Analysis")
            st.markdown(r"**Taylor's Theorem:** $f(x) = T_n(x) + R_n(x)$")
            st.markdown(r"**Lagrange Bound:** $|R_n(x)| \le \frac{M}{(n+1)!} |x-a|^{n+1}$ where $M = \max |f^{(n+1)}(t)|$")
            
            x_eval = st.number_input("Evaluation Point (x):", value=1.0)
            
            rem_res = t_engine.get_remainder_analysis(x_eval, order_input)
            if rem_res["Status"] == "Success":
                st.write(f"- **Exact $f(x)$:** `{rem_res['Exact f(x)']}`")
                st.write(f"- **Approximation $T_n(x)$:** `{rem_res['Taylor T_n(x)']}`")
                st.write(f"- **Actual Error:** `{rem_res['Actual Error']}`")
                st.write(f"- **Lagrange Error Bound:** `{rem_res['Lagrange Error Bound']}`")
                if isinstance(rem_res['Lagrange Error Bound'], float):
                    st.success("✅ The actual error is strictly within the theoretical Lagrange bound.")
            else:
                st.error(rem_res["Reason"])
                
            st.divider()
            st.subheader("Order Selection via Target Tolerance")
            tol_val = st.number_input("Target Tolerance $\epsilon$:", value=1e-5, format="%.6f")
            if st.button("Find Minimum Required Order"):
                ord_res = t_engine.find_target_order(x_eval, tol_val)
                st.json(ord_res)
                
        with tabs[2]:
            st.header("Convergence & Symbolic Verification")
            
            st.subheader("1. Radius & Interval of Convergence")
            roc = t_engine.get_convergence()
            st.write(f"- **Radius (R):** `{roc['R']}`")
            st.write(f"- **Interval:** `{roc['Interval']}`")
            st.info(f"Methodology: {roc['Note']}")
            
            st.subheader("2. Derivative Condition Verification")
            st.markdown("Verifying that $T_n^{(k)}(a) = f^{(k)}(a)$ for all $k \le n$.")
            ver_res = t_engine.verify_polynomial(order_input)
            if ver_res["All Verified"]:
                st.success("✅ All initial value derivative conditions verified symbolically.")
            else:
                st.warning("Verification failed or was symbolically indeterminate.")
                
        with tabs[3]:
            st.header("Visualizing Convergence & Error")
            v1, v2 = st.columns(2)
            with v1:
                st.pyplot(plot_taylor_approximation(t_engine, order_input))
            with v2:
                # Compare current order, half order, and n=1
                map_orders = list(set([1, max(1, order_input//2), order_input]))
                st.pyplot(plot_taylor_error_map(t_engine, map_orders))
                
    except Exception as e:
        st.error(f"Error parsing function or generating polynomial: {e}")
