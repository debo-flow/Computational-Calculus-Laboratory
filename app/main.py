# ... [Keep Milestones 1 to 8 unchanged] ...

elif page == "Milestone 9: Sequences & Series":
    st.title("Advanced Sequences & Infinite Series Laboratory")
    st.markdown("Analyze discrete sequence convergence, calculate partial sums, and rigorously test infinite series.")
    
    from calculus.sequences.sequence_engine import SequenceEngine
    from calculus.sequences.convergence import analyze_sequence_limit
    from calculus.sequences.sequence_analysis import analyze_monotonicity, analyze_boundedness
    from calculus.series.series_engine import SeriesEngine
    from calculus.series.partial_sums import calculate_partial_sums
    from visualization.sequence_series_plots import plot_sequence_and_series
    
    tabs = st.tabs(["Sequences ($a_n$)", "Infinite Series ($\Sigma a_n$)", "Special Series (Geometric & P)"])
    
    with tabs[0]:
        st.header("Sequence Analysis ($a_n$)")
        seq_input = st.text_input("Enter Sequence $a_n = f(n)$:", value="(2*n) / (n + 1)")
        
        try:
            seq_eng = SequenceEngine(seq_input)
            st.latex(r"a_n = " + sp.latex(seq_eng.expression))
            
            c1, c2 = st.columns(2)
            with c1:
                st.subheader("1. Limit & Convergence")
                lim_res = analyze_sequence_limit(seq_eng)
                st.write(f"- **Limit as $n \\to \\infty$:** `{lim_res['Limit']}`")
                st.write(f"- **Status:** `{lim_res['Classification']}`")
                
                st.subheader("2. Monotonicity & Boundedness")
                st.write(f"- **Monotonicity:** `{analyze_monotonicity(seq_eng)}`")
                st.write(f"- **Boundedness:** `{analyze_boundedness(seq_eng)}`")
                
            with c2:
                st.subheader("Sequence Terms")
                num_terms = st.slider("Number of terms to generate", 5, 50, 10)
                st.dataframe(pd.DataFrame(seq_eng.generate_terms(1, num_terms)), use_container_width=True)
                
        except Exception as e:
            st.error(f"Error parsing sequence: {e}")

    with tabs[1]:
        st.header("Infinite Series Convergence Tests ($\Sigma a_n$)")
        ser_input = st.text_input("Enter Series Term $a_n$:", value="1 / factorial(n)")
        
        try:
            ser_seq_eng = SequenceEngine(ser_input)
            ser_eng = SeriesEngine(ser_seq_eng)
            
            st.latex(r"\sum_{n=1}^{\infty} " + sp.latex(ser_seq_eng.expression))
            
            col_tests, col_viz = st.columns([1, 1])
            with col_tests:
                st.subheader("Convergence Test Report")
                report = ser_eng.run_all_tests()
                
                st.info(f"**Final Conclusion:** {report['Final Conclusion']}")
                
                with st.expander("View Individual Test Results"):
                    for test_name, test_data in report.items():
                        if test_name != "Final Conclusion":
                            st.markdown(f"**{test_name}:**")
                            st.json(test_data)
                            
                exact_sum = ser_eng.evaluate_exact_sum()
                st.success(f"**Exact Analytic Sum:** `{exact_sum}`")
                
            with col_viz:
                st.subheader("Partial Sums Visualization ($S_N$)")
                N_val = st.slider("Calculate up to N =", 5, 100, 20)
                partial_data = calculate_partial_sums(ser_seq_eng, N_val)
                st.pyplot(plot_sequence_and_series(partial_data))
                
        except Exception as e:
            st.error(f"Error analyzing series: {e}")
            
    with tabs[2]:
        st.header("Special Educational Series")
        st.markdown("""
        **1. The Harmonic Series:** $\sum \frac{1}{n}$
        - The limit of the terms approaches 0, proving that $a_n \to 0$ is a *necessary* but not *sufficient* condition for convergence.
        - The series strictly **diverges** to infinity.
        
        **2. P-Series:** $\sum \frac{1}{n^p}$
        - Converges if $p > 1$. Diverges if $p \le 1$.
        
        **3. Geometric Series:** $\sum a r^n$
        - Converges absolutely if $|r| < 1$. Sum $= \frac{a}{1-r}$.
        """)
