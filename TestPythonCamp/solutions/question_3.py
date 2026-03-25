"""Reference solution for question 3."""


def sum_even_numbers(numbers):
    return sum(number for number in numbers if number % 2 == 0)
