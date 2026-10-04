"""Main orchestration module for Student Marks Application."""

from calculations import calculate_average, calculate_grade, calculate_total
from display import display_result
from validation import validate_mark


def get_valid_mark(subject_num: int) -> float:
    """Prompt user repeatedly until a valid mark is entered."""
    while True:
        try:
            mark = float(input(f"Enter marks for subject {subject_num}: "))
            if validate_mark(mark):
                return mark
            print("Invalid marks. Enter 0-100.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")


def main() -> None:
    name = input("Enter student name: ")
    marks = []

    for i in range(3):
        mark = get_valid_mark(i + 1)
        marks.append(mark)

    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)

    display_result(name, total, average, grade)


if __name__ == "__main__":
    main()
