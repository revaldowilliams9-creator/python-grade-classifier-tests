def classify_grade(mark):
    """Classify a percentage mark (0-100) into an academic grade."""
    if not isinstance(mark, (int, float)) or isinstance(mark, bool):
        raise TypeError("Mark must be a numeric value.")
    if mark < 0 or mark > 100:
        raise ValueError("Mark must be between 0 and 100 inclusive.")

    if mark >= 75:
        return "Distinction"
    elif mark >= 50:
        return "Pass"
    else:
        return "Fail"
