# Computational Calculus Laboratory

**Milestone 7 — Advanced Integral Calculus Laboratory**

## Project Description
The Computational Calculus Laboratory is an extensible Python-based interactive mathematics environment. 

Milestone 7 introduces the **Advanced Integral Calculus Laboratory**, completing the foundational core of single-variable calculus. Building on top of limits, continuity, and differential calculus, this milestone introduces symbolic antiderivatives, exact definite integrals, numerical Riemann approximations, FTC verification, techniques of integration, and improper integral classification.

## Features Implemented

### Milestone 7: Integral Calculus
* **Symbolic Antiderivatives:** Computes exact indefinite integrals, explicitly incorporating the constant of integration $+ C$ and verifying results via differentiation ($d/dx[F(x)] = f(x)$).
* **Definite Integration & Area:** Computes signed accumulation $\int_a^b f(x) dx$, total geometric area $\int_a^b |f(x)| dx$, and properly enforces reversed bound identities ($\int_b^a = -\int_a^b$).
* **Area Between Curves:** Computes bounded area between $f(x)$ and $g(x)$, identifying critical intersection points within the interval.
* **Riemann Sum Approximations:** Left, Right, and Midpoint Riemann sums with interactive rectangle visualization and $n \to \infty$ convergence tracking.
* **Fundamental Theorem of Calculus:**
  * **Part I:** Verifies $\frac{d}{dx} \left[\int_a^x f(t) dt\right] = f(x)$.
  * **Part II:** Evaluates $\int_a^b f(x) dx = F(b) - F(a)$.
* **Integration Techniques:** Symbolic support for $u$-substitution, Integration by Parts ($\int u \, dv = uv - \int v \, du$), and Partial Fractions decomposition.
* **Improper Integrals:** Evaluates infinite limits and singular integrands, classifying convergence/divergence behavior.

### Earlier Milestones (Preserved)
* **M6:** Advanced Numerical Differentiation (Stencils, Truncation vs Round-off, Richardson Extrapolation, Noisy Data).
* **M5:** Applications of Differential Calculus (Extrema, Critical Points, MVT, Newton-Raphson).
* **M4:** Advanced Differential Calculus (Symbolic/Numerical derivatives, Tangents/Secants).
* **M3:** Continuity and Discontinuity Classification (Removable, Jump, Infinite, Oscillatory).
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
