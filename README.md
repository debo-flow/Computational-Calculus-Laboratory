# Computational Calculus Laboratory

**Milestone 4 — Advanced Differential Calculus Laboratory**

## Project Description
The Computational Calculus Laboratory is an extensible Python-based interactive mathematics environment. 

Milestone 4 introduces the **Advanced Differential Calculus Laboratory**. This module builds seamlessly on top of limits and continuity, providing robust symbolic differentiation, rule identification, interactive geometric limits (secant-to-tangent), error analysis for numerical methods, and advanced techniques (implicit/parametric).

## Features Implemented

### Milestone 4: Differential Calculus
* **Symbolic Differentiation:** Uses SymPy to exact $n$-th order derivatives.
* **Differentiation Rules:** Detects power, product, quotient, and chain rules.
* **Geometric Limits:** Interactive visualization showing secant lines converging to tangent lines as $h \to 0$.
* **Numerical Differentiation:** Forward, Backward, and Central difference equations.
* **Error Analysis Table:** Dynamically shows floating-point cancellation errors when $h$ becomes too small.
* **Advanced Derivation:** Implicit differentiation, Parametric equations, and Logarithmic differentiation.
* **Differentiability Analysis:** Proves that Continuity does not imply Differentiability (e.g., $f(x) = |x|$ at $x=0$).

### Milestone 1-3 Features (Preserved)
* Foundation mathematical engine.
* Symbolic limit evaluation and tables.
* Continuity evaluation and classification (jump, removable, infinite).

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
