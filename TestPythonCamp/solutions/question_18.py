"""Reference solution for question 18."""


def sum_digits(number):
    return sum(int(digit) for digit in str(abs(number)))
