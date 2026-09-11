# Computational Calculus Laboratory

**Milestone 6 — Advanced Numerical Differentiation Laboratory**

## Project Description
The Computational Calculus Laboratory is an extensible Python-based interactive mathematics environment. 

Milestone 6 introduces the **Advanced Numerical Differentiation Laboratory**. Moving beyond simple difference quotients, this milestone tackles the computational realities of machine limits: exploring the violent collision between truncation error and floating-point cancellation, establishing reusable $O(h^n)$ stencils, deploying Richardson Extrapolation, and accurately handling discrete/noisy data.

## Features Implemented

### Milestone 6: Advanced Numerical Differentiation
* **Finite-Difference Stencils:** Standardized object-oriented stencils for Forward, Backward, Central, and Higher-Order derivatives (up to 3rd derivative).
* **Truncation vs. Round-off Error Analysis:** Generates dynamic log-log plots proving that infinitely decreasing $h$ destroys accuracy due to floating-point cancellation.
* **Algorithmic Corrections:** 
  * **Richardson Extrapolation:** Combines $O(h^2)$ estimates to achieve $O(h^4)$ precision.
  * **Adaptive Step-Size:** Automatically searches for optimal $h$ by detecting convergence halts.
* **Discrete & Noisy Data Processing:** Differentiates arrays of data, accurately handling non-uniform spacing using weighted interpolations. A noisy-data simulation proves why numerical derivatives act as high-pass filters amplifying noise.
* **Reliability Classifications:** Automatically tags calculations as `RELIABLE`, `CAUTION`, `UNSTABLE`, or `FAILED` based on mathematical limits.

### Earlier Milestones (Preserved)
* **M5:** Applications (Optimization, MVT, Newton's Root-Finding).
* **M4:** Advanced Differentiation (Rules, Implicit, Parametric).
* **M3:** Continuity and Discontinuity Classification.
* **M2:** Limits Laboratory (LHL/RHL, Infinity).
* **M1:** Core Foundation (Parsing, Validation).

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
