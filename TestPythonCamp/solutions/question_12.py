"""Reference solution for question 12."""


def average_numbers(numbers):
    if not numbers:
        raise ValueError("numbers cannot be empty")
    return sum(numbers) / len(numbers)
