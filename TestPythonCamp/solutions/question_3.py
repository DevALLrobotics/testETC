"""Reference solution for question 3."""


def sum_even_numbers(numbers):
    return sum(number for number in numbers if number % 2 == 0)

# def sum_even_numbers(numbers):
#     total = 0
#     for i in numbers:
#         if i % 2 == 0:
#             total = total + i
#     return total