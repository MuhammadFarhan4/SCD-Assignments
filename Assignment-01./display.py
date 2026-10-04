"""Module for presenting formatted output to the user."""


def display_result(name: str, total: float, average: float, grade: str) -> None:
    """Format and display the student result summary."""
    print("\nStudent Result")
    print("----------------")
    print("Name:", name)
    print("Total:", total)
    print("Average:", f"{average:.2f}")
    print("Grade:", grade)
