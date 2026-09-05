# Computational Calculus Laboratory

**Milestone 3 — Advanced Continuity Laboratory**

## Project Description
The Computational Calculus Laboratory is an extensible Python-based interactive mathematics environment. 

Milestone 3 introduces the **Advanced Continuity Laboratory**. It builds upon the function engine (Milestone 1) and limits engine (Milestone 2) to provide rigorous mathematical analysis of continuous and discontinuous functions, supporting point-wise checking, piecewise functions, and interval mapping.

## Features Implemented

### Milestone 3: Advanced Continuity
* **Point Continuity Analysis:** Verifies $f(a)$, $\lim_{x \to a^-} f(x)$, and $\lim_{x \to a^+} f(x)$ to prove continuity.
* **Discontinuity Classification:** Automatically detects Removable (holes), Jump, Infinite (asymptotes), and Oscillatory discontinuities.
* **Piecewise Support:** Analyzes continuity boundaries natively through SymPy's Piecewise expressions.
* **Visual States:** Matplotlib engine upgraded to render open holes (removable), solid points (continuous), and asymptotes.
* **Interval Mapping:** Scans intervals $[a, b]$ for potential theoretical singularities/discontinuities.
* **Numerical Verification:** Reuses limit tables to prove proximity to defined function points.

### Milestone 2: Advanced Limits
* Symbolic one-sided and two-sided limits.
* Numerical convergence tables.
* Infinite limits and error analysis.

### Milestone 1: Foundation
* Safe mathematical parsing.
* Core evaluation, domain rules, and simplification logic.

## Technology Stack
* Python 3.9+
* Core Mathematics: SymPy, NumPy
* Visualization: Matplotlib
* UI Framework: Streamlit
* Testing: Pytest

## Running the Laboratory
```bash
pip install -r requirements.txt
streamlit run app/main.py
