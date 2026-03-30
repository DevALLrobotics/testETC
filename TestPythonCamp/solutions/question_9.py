"""Reference solution for question 9."""


def get_max_number(numbers):
    if not numbers:
        raise ValueError("numbers cannot be empty")
    return max(numbers)
