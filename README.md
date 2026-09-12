# Computational Calculus Laboratory

**Milestone 8 — Advanced Numerical Integration Laboratory**

## Project Description
The Computational Calculus Laboratory is an extensible Python-based interactive mathematics environment. 

Milestone 8 introduces the **Advanced Numerical Integration Laboratory**. Bridging analytical integration and computational limitations, this update brings a complete quadrature suite allowing rigorous benchmarking of classical methods, theoretical bounding, and dynamic adaptive refinement for oscillatory or highly-peaked functions. 

## Features Implemented

### Milestone 8: Advanced Numerical Integration
* **Quadrature Engine:** Implements composite Trapezoidal, Simpson 1/3, and Simpson 3/8 rules, strictly enforcing mathematical node requirements.
* **Gaussian Quadrature:** Integrates Gauss-Legendre node-weight transformations from the standard domain $[-1, 1]$ to $[a, b]$ for extreme polynomial accuracy.
* **Adaptive Integration:** A recursive Adaptive Simpson implementation that estimates local error ($|S(a,b) - (S_L+S_R)| / 15$) and refines the mesh exclusively where the function exhibits rapid change. Includes subdivision plotting.
* **Error Bounding & Convergence:** Compares theoretical absolute error bounds (using symbolic derivatives $\max|f''(x)|$) to observed $O(h^p)$ convergence via n-stepping log ratios.
* **Data & Cumulative Integration:** Safely integrates non-uniform discrete data arrays, and computationally constructs cumulative area vectors $F(x) = \int f(t) dt$ to demonstrate FTC computationally.

### Earlier Milestones (Preserved)
* **M7:** Advanced Integral Calculus (Symbolic $+C$, FTC, Area between curves, substitution).
* **M6:** Advanced Numerical Differentiation (Stencils, Truncation vs Round-off, Richardson Extrapolation).
* **M5:** Applications of Differential Calculus (Extrema, Critical Points, MVT, Newton-Raphson).
* **M4:** Advanced Differential Calculus (Symbolic/Numerical derivatives, Tangents/Secants).
* **M3:** Continuity and Discontinuity Classification.
* **M2:** Limits Laboratory (LHL, RHL, Infinite Limits).
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
