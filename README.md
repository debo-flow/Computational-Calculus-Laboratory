# Computational Calculus Laboratory

**Milestone 2 — Advanced Limits Laboratory**

## Project Description
The Computational Calculus Laboratory is an extensible Python-based interactive mathematics environment. Milestone 2 introduces the **Advanced Limits Laboratory**, building safely upon the mathematical engine laid out in Milestone 1 without breaking existing architectural flow.

## Features Implemented
### Milestone 2: Advanced Limits
* **Symbolic Limit Computation:** Accurately calculates left-hand, right-hand, two-sided, and infinite limits using SymPy.
* **Special Case Handling:** Detects removable discontinuities, jump behaviors, and infinite asymptotes.
* **Numerical Convergence Tables:** Proves limit concepts experimentally by generating structured numerical approaches (e.g., distances of `0.1`, `0.01`, `0.001`).
* **Visual Limits Engine:** An upgraded Matplotlib graph that plots vertical guides at the limit point, allowing users to physically see convergence.
* **Automated Mathematical Interpretation:** Translates complex symbolic states into readable explanations (e.g., explaining *why* a limit doesn't exist based on LHL/RHL inequalities).
* **Error Analysis:** Automatically tracks absolute error and relative error between exact symbolic bounds and iterative approximations.

### Milestone 1: Foundation (Still Available)
* Safe mathematical expression parsing.
* Extensible UI via Streamlit.
* Base numerical validations and basic functions plotting.

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
