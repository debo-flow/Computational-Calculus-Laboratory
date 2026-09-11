# Computational Calculus Laboratory

**Milestone 5 — Applications of Differential Calculus Laboratory**

## Project Description
The Computational Calculus Laboratory is an extensible Python-based interactive mathematics environment. 

Milestone 5 introduces the **Applications of Differential Calculus**. Building on the strict mathematical foundation of M1-M4, this milestone turns abstract derivatives into powerful applied tools: finding optimal solutions, proving theorems, approximating values, and executing algorithmic root-finding.

## Features Implemented

### Milestone 5: Applications
* **Critical Point & Extrema Detection:** Employs the First and Second Derivative tests to automatically classify local minima and maxima.
* **Closed Interval Optimization:** Strictly determines Absolute Max/Min on bounded intervals $[a, b]$.
* **Theorem Verification:** Computes the mathematical guarantees of the **Mean Value Theorem** and **Rolle's Theorem**, solving for candidates $c$.
* **Concavity & Inflection:** Analyzes $f''(x)$ to determine concavity boundaries.
* **Newton-Raphson Engine:** Algorithmic root-finding with built-in iteration limiters, derivative failure detection, and history tracking.
* **Approximations:** Computes Linear (Tangent) Approximations and Absolute Error tables dynamically.

### Earlier Milestones (Preserved)
* **M4:** Advanced Differentiation (Rules, Symbolic, Numerical limits).
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
