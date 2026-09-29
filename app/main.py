# ... [Keep Milestones 1 to 22 unchanged] ...

elif page == "Milestone 23: Symbolic CAS":
    st.title("Advanced Symbolic Mathematics & Computer Algebra System")
    st.markdown("A unified interface for safe expression parsing, exact algebra, assumptions, and symbolic routing.")

    from calculus.symbolic.symbolic_engine import CASRouter
    from calculus.symbolic.expression_analysis import analyze_complexity, find_domain_restrictions
    from calculus.symbolic.assumptions import apply_assumptions_to_expr

    tabs = st.tabs([
        "Parser & Algebra", 
        "Equations & Inequalities", 
        "Calculus Router & Laplacian",
        "Expression Tree & Domain",
        "CAS Notebook (Stateful)"
    ])

    with tabs[0]:
        st.header("Safe Parsing & Algebraic Manipulation")
        c1, c2 = st.columns([3, 1])
        with c1: expr_input = st.text_input("Expression (e.g. `(x+1)^2 / (x^2 - 1)`):", "(x+1)^2 / (x^2 - 1)")
        with c2: operation = st.selectbox("Operation:", ["simplify", "expand", "factor", "cancel", "apart"])
        
        if st.button("Execute Algebra"):
            try:
                if operation == "simplify":
                    res = CASRouter.simplify(expr_input)
                else:
                    res = CASRouter.algebra(expr_input, operation)
                st.latex(sp.latex(res))
            except Exception as e:
                st.error(f"Error: {e}")
                
        st.divider()
        st.subheader("Assumptions Engine")
        st.markdown("Restricts mathematical domains (e.g., forcing $x$ to be real and positive) to unlock transformations.")
        assump_expr = st.text_input("Expression to evaluate:", "sqrt(x^2)")
        if st.button("Evaluate with Assumptions (x is real, positive)"):
            assumptions = {"real": True, "positive": True}
            res_assump = apply_assumptions_to_expr(assump_expr, ["x"], assumptions)
            st.latex(sp.latex(res_assump))
            st.info("Notice that without positive Real assumptions, $\sqrt{x^2}$ remains unevaluated or simplifies to $\vert{}x\vert{}$.")

    with tabs[1]:
        st.header("Equations & Inequalities")
        eq_input = st.text_input("Equation $f(x) = 0$:", "x^3 - 8")
        if st.button("Solve Exact Equation"):
            sol_res = CASRouter.solve(eq_input, "x")
            st.write(f"- **Status:** `{sol_res['Status']}`")
            st.write(f"- **Solution Set:**")
            st.latex(sp.latex(sol_res['Solutions']))
            
        st.divider()
        ineq_input = st.text_input("Inequality (e.g. `x^2 - 4 < 0`):", "x^2 - 4 < 0")
        if st.button("Solve Inequality"):
            ineq_res = CASRouter.inequalities(ineq_input)
            st.write(f"- **Valid Interval:**")
            st.latex(sp.latex(ineq_res['Interval']))

    with tabs[2]:
        st.header("Unified Calculus Router")
        st.markdown("Routes arbitrary symbolic operations to their respective internal engines without numerical fallback.")
        
        rout_op = st.selectbox("Select Core Operator:", ["derivative", "integral_indefinite", "limit", "series", "laplacian"])
        r1, r2 = st.columns(2)
        with r1: rout_expr = st.text_input("Expression:", "sin(x*y)")
        with r2: rout_var = st.text_input("Variable(s):", "x, y" if rout_op == "laplacian" else "x")
        
        if st.button("Execute Symbolic Operation"):
            rout_res = CASRouter.calculus_route(rout_op, rout_expr, rout_var)
            st.latex(sp.latex(rout_res))
            
        st.divider()
        st.subheader("Symbolic vs. Numerical Verification")
        v1, v2 = st.columns(2)
        with v1: exp_a = st.text_input("Expression A:", "sin(x)^2 + cos(x)^2")
        with v2: exp_b = st.text_input("Expression B:", "1")
        if st.button("Verify Equivalence"):
            ver_res = CASRouter.verify(exp_a, exp_b, "x")
            st.json(ver_res)

    with tabs[3]:
        st.header("Expression Analytics & Trees")
        anal_expr = st.text_input("Analyze Expression:", "exp(sqrt(x-2)) / (x-5)")
        
        if st.button("Generate Analytics"):
            import sympy as sp
            # Safe local parse
            from calculus.symbolic.expression_parser import safe_parse
            p_expr = safe_parse(anal_expr)
            
            c3, c4 = st.columns(2)
            with c3:
                st.subheader("Complexity Metrics")
                st.json(analyze_complexity(p_expr))
            with c4:
                st.subheader("Domain Restrictions ($\mathbb{R}$)")
                st.write(find_domain_restrictions(p_expr, sp.Symbol('x')))
            
            st.subheader("Expression Tree AST")
            st.json(CASRouter.tree(anal_expr))

    with tabs[4]:
        st.header("Interactive CAS Notebook")
        st.markdown("Maintain a stateless or session-stored execution list of operations.")
        
        if "cas_history" not in st.session_state:
            st.session_state.cas_history = []
            
        cmd_in = st.text_input("Notebook Input (Use syntax: `operation: expression`. E.g., `simplify: x*x/x`):")
        
        if st.button("Execute Cell"):
            try:
                op, exp = cmd_in.split(":", 1)
                op, exp = op.strip().lower(), exp.strip()
                if op == "simplify": out = CASRouter.simplify(exp)
                elif op in ["expand", "factor", "cancel", "apart"]: out = CASRouter.algebra(exp, op)
                else: out = "Unsupported Command. Try: simplify, expand, factor, cancel, apart."
                
                st.session_state.cas_history.insert(0, {"In": cmd_in, "Out": out})
            except Exception as e:
                st.error(f"Notebook syntax error: {e}")
                
        if st.button("Clear History"):
            st.session_state.cas_history = []
            
        for idx, cell in enumerate(st.session_state.cas_history):
            st.markdown(f"**In [{len(st.session_state.cas_history) - idx}]:** `{cell['In']}`")
            st.latex(sp.latex(cell["Out"]) if isinstance(cell["Out"], sp.Expr) else cell["Out"])
            st.divider()
