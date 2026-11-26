# 🧪 Python Grade Classifier & Unit Test Suite

A modular **Python** grading utility paired with an automated `unittest` suite demonstrating input validation, boundary-value analysis, and 100% branch coverage.

## 💡 Why I Built This
I built this suite to practice defensive programming and test-driven quality assurance using Python's built-in `unittest` framework. Rather than assuming valid user inputs, the project focuses on catching type errors, enforcing strict `0–100` boundary rules, and verifying 100% branch coverage automatically.

## ✨ Key Features
* 🛡️ **Strict Input & Range Validation:** Rejects non-numeric inputs and booleans (`TypeError`) as well as out-of-bounds marks outside `0–100` (`ValueError`).
* 🎯 **Complete Branch & Boundary Coverage:** Verifies `Distinction` (`>= 75`), `Pass` (`50–74.9`), and `Fail` (`< 50`) across exact threshold edges (`0`, `50`, `75`, `100`).

## 📂 Project Structure
* 📄 `grades.py` — Core `classify_grade()` function with defensive type and range checking.
* ✅ `test_grades.py` — Automated `unittest.TestCase` suite covering valid grades, boundary edges, and error states.

## 🚀 Running the Tests

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd python-grade-classifier-tests
   ```

2. **Execute the verbose test suite:**
   ```bash
   python -m unittest discover -v
   ```

## 📊 Sample Test Output
```text
test_distinction (test_grades.TestGradeClassifier) ... ok
test_fail (test_grades.TestGradeClassifier) ... ok
test_invalid_type_raises_type_error (test_grades.TestGradeClassifier) ... ok
test_out_of_range_raises_value_error (test_grades.TestGradeClassifier) ... ok
test_pass (test_grades.TestGradeClassifier) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```
