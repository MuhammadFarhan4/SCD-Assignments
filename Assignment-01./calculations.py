"""Module for student marks calculation and grading logic."""


def calculate_total(marks: list[float]) -> float:
    """Calculate the total sum of marks."""
    return sum(marks)


def calculate_average(marks: list[float]) -> float:
    """Calculate the arithmetic average of marks."""
    if not marks:
        return 0.0
    return calculate_total(marks) / len(marks)


def calculate_grade(average: float) -> str:
    """Determine letter grade based on the average mark."""
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"
