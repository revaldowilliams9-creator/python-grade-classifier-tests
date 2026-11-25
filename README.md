# Python Grade Classifier & Unit Test Suite

A modular Python grading utility paired with an automated `unittest` suite demonstrating input validation, boundary-value analysis, and 100% branch coverage.

## Features
- **Strict Input & Range Validation:** Rejects non-numeric inputs (`TypeError`) and out-of-bounds marks outside `0–100` (`ValueError`).
- **Complete Branch & Boundary Coverage:** Tests `Distinction` (`>= 75`), `Pass` (`50–74.9`), and `Fail` (`< 50`) across exact threshold edges (`0`, `50`, `75`, `100`).

## Project Structure
- `grades.py` — Core `classify_grade()` function with defensive range checking.
- `test_grades.py` — Automated `unittest.TestCase` suite covering valid grades, boundary edges, and error states.

## Running the Tests
```bash
python -m unittest discover -v
```

• 
I built this suite to practice defensive programming and test-driven quality assurance using Python's built-in unittest framework. Rather than assuming valid user inputs, the project focuses on catching type errors, enforcing strict 0–100 boundary rules, and verifying 100% branch coverage automatically.
