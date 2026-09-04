# Computational Calculus Laboratory

**Milestone 1 — Foundation & Mathematical Function Engine**

## Project Description
The Computational Calculus Laboratory is an extensible Python-based interactive mathematics environment. Its long-term goal is to provide a high-quality suite for limits, differentiation, integration, multivariable calculus, and numerical methods. 

This repository currently represents **Milestone 1**. It does *not* contain the complete calculus laboratory yet. Instead, it lays down a strictly typed, modular, and safe foundation focusing on mathematical string parsing, symbolic representation, fundamental analysis, and robust visualization.

## Features Implemented
* **Safe Mathematical Parsing:** Utilizes SymPy to parse string functions securely, avoiding python `eval()`.
* **Symbolic Representation:** Simplifies, expands, and factorizes algebraic equations.
* **Function Evaluation:** Solves continuous and discontinuous expressions (e.g., $1/x$) seamlessly.
* **Function Tables:** Generates step-based datasets across bounded intervals.
* **Basic Visualization:** 2D graphing engine with smart asymptote handling built on Matplotlib.
* **Numerical Validation:** Foundation for absolute and relative error mathematics.
* **Interactive UI:** A modular Streamlit frontend isolating interface logic from mathematical operations.

## Technology Stack
* **Language:** Python 3.9+
* **Core Mathematics:** SymPy, NumPy
* **Visualization:** Matplotlib
* **UI Framework:** Streamlit
* **Testing:** Pytest

## Project Architecture
```text
app/             - Streamlit frontend routing
calculus/        - Core symbolic manipulation and engine classes
numerical/       - Pure mathematical and error-validation functions
visualization/   - Reusable graphing components
tests/           - Automated quality assurance tests
