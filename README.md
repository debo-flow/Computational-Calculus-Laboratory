# Computational Calculus Laboratory

**Milestone 9 — Advanced Sequences & Infinite Series Laboratory**

## Project Description
The Computational Calculus Laboratory is an extensible Python-based interactive mathematics environment. 

Milestone 9 introduces the **Advanced Sequences & Infinite Series Laboratory**. It transitions the platform from continuous functions to discrete domains ($n \in \mathbb{N}$). It features robust analytical testing (Ratio, Root, N-th Term, Alternating) to prove infinite series convergence, partial sum generation, and strict distinction between term limits and summation limits.

## Features Implemented

### Milestone 9: Sequences & Infinite Series
* **Sequence Analysis:** Computes $\lim_{n \to \infty} a_n$, evaluates symbolic monotonicity via derivative mapping, and deduces global boundedness.
* **Convergence Test Coordinator:** Automatically subjects $\Sigma a_n$ to the N-th Term Test, Ratio Test ($|a_{n+1}/a_n|$), Root Test ($\sqrt[n]{|a_n|}$), and Alternating Series Test.
* **Strict Mathematical Logic:** Enforces the rule that $a_n \to 0$ is a *necessary* but NOT *sufficient* condition for convergence (e.g., the Harmonic series).
* **Exact vs Partial Sums:** Evaluates $S_N = \sum_{1}^N a_n$ iteratively while using SymPy to hunt for the exact infinite analytic limit. 
* **Discrete Visualization:** Matplotlib scatter plots for discrete sequence terms overlaid with step-plots indicating partial sum accumulation.

### Earlier Milestones (Preserved)
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
