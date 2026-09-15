# Computational Calculus Laboratory

**Milestone 10 — Advanced Taylor & Maclaurin Series Laboratory**

## Project Description
The Computational Calculus Laboratory is a comprehensive, extensible Python-based interactive mathematics environment. 

Milestone 10 introduces the **Advanced Taylor & Maclaurin Series Laboratory**. This final single-variable calculus component leverages the differentiation engine, symbolic limits, and root-finding utilities to generate $T_n(x)$, compute precise Lagrange Error Bounds, analyze the Radius of Convergence via complex plane singularities, and dynamically select Taylor orders required for requested error tolerances.

## Features Implemented

### Milestone 10: Taylor & Maclaurin Series
* **Polynomial Generation:** Symbolically generates $T_n(x)$ and explicitly maps cached coefficients $c_n = f^{(n)}(a)/n!$.
* **Taylor's Theorem & Lagrange Remainders:** Numerically bounds $M = \max |f^{(n+1)}(t)|$ on $[a, x]$ to explicitly contrast Actual Approximation Error with Theoretical Error Bounds.
* **Symbolic Verification:** Evaluates $T_n^{(k)}(a) == f^{(k)}(a)$ to mathematically prove the foundational conditions of Taylor polynomials.
* **Convergence Radii:** Discovers distances to complex singularities to establish the absolute radius of convergence ($R$) and intervals of valid approximations.
* **Dynamic Order Selection:** Recursively iterates through Taylor orders to locate the minimal $n$ required to satisfy user-defined target tolerances.
* **Error Map Visualization:** Plots the original function overlaid with polynomial approximations, alongside semi-log error maps ($E_n(x) = |f(x) - T_n(x)|$).

### Earlier Milestones (Preserved)
* **M9:** Advanced Sequences & Infinite Series (Ratio/Root/Integral Tests, Convergence).
* **M8:** Advanced Numerical Integration (Quadrature, Gaussian, Adaptive).
* **M7:** Advanced Integral Calculus (Symbolic $+C$, FTC, substitutions).
* **M6:** Advanced Numerical Differentiation.
* **M5:** Applications of Differential Calculus (Extrema, MVT).
* **M4:** Advanced Differential Calculus (Rules, Tangents).
* **M3:** Continuity and Discontinuity Classification.
* **M2:** Limits Laboratory (LHL/RHL).
* **M1:** Core Foundation & Mathematical Function Engine.

## Technology Stack
* Python 3.9+
* Mathematics: SymPy, NumPy
* Visualization: Matplotlib
* UI Framework: Streamlit
* Testing: Pytest

## Installation & Running
```bash
pip install -r requirements.txt
streamlit run app/main.py
