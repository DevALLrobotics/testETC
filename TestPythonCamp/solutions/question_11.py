"""Reference solution for question 11."""


def factorial(n):
    result = 1
    for number in range(1, n + 1):
        result *= number
    return result
