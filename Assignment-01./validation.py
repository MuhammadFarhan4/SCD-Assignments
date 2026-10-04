"""Module for data validation rules."""


def validate_mark(mark: float) -> bool:
    """Check if a numeric mark is within the valid range of 0 to 100."""
    return 0 <= mark <= 100
