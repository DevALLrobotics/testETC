# Python Basic Exam with `pytest`

Thai version: [README_TH.md](README_TH.md)

This folder contains a small Python basic exam with 20 questions.

Files:
- `student.py`: overview file
- `students/`: student templates for each question
- `solution.py`: solution overview file
- `solutions/`: reference solutions
- `check.py`: beginner-friendly checker with readable output
- `test.py`: quick index file
- `tests/`: pytest test cases and test utilities

Questions:
1. `add_numbers(a, b)` returns the sum of two numbers
2. `is_leap_year(year)` checks leap year rules
3. `sum_even_numbers(numbers)` sums only even numbers in a list
4. `count_vowels(text)` counts vowels in a string
5. `find_top_student(scores)` returns the name with the highest score
6. `get_grade(score)` returns the grade from a score
7. `reverse_text(text)` returns the reversed text
8. `count_words(text)` returns the number of words
9. `get_max_number(numbers)` returns the largest number in a list
10. `is_palindrome(text)` checks whether a text is a palindrome
11. `factorial(n)` returns the factorial of a number
12. `average_numbers(numbers)` returns the average of a list
13. `remove_duplicates(items)` removes duplicates while keeping order
14. `count_character(text, target)` counts a specific character
15. `celsius_to_fahrenheit(celsius)` converts Celsius to Fahrenheit
16. `filter_positive_numbers(numbers)` keeps only positive numbers
17. `get_last_element(items)` returns the last item in a list
18. `sum_digits(number)` returns the sum of all digits
19. `sort_numbers(numbers)` returns numbers in ascending order
20. `get_initials(full_name)` returns the initials of a name

Rules:
- Edit only the matching student file for each question
- Do not change files in `tests/`
- For question 5, raise `ValueError` when the dictionary is empty

Usage:
1. Install `pytest`
2. Write your answer in the matching template under `students/`
3. Run `check.py` for readable feedback or run `pytest`

Beginner-friendly check:
```bash
python3 TestPythonCamp/check.py
python3 TestPythonCamp/check.py 1
python3 TestPythonCamp/check.py 1 2
```

How to run all questions:
```bash
python3 -m pip install pytest
python3 -m pytest TestPythonCamp/tests -q
```

How to run one question at a time:
```bash
python3 -m pytest TestPythonCamp/tests/test_question_1.py -q
```

Replace `1` with any question number from `1` to `20`.

Question mapping:
- Question 1: create `add_numbers(a, b)` in `students/question_1.py`
- Question 2: create `is_leap_year(year)` in `students/question_2.py`
- Question 3: create `sum_even_numbers(numbers)` in `students/question_3.py`
- Question 4: create `count_vowels(text)` in `students/question_4.py`
- Question 5: create `find_top_student(scores)` in `students/question_5.py`
- Question 6: create `get_grade(score)` in `students/question_6.py`
- Question 7: create `reverse_text(text)` in `students/question_7.py`
- Question 8: create `count_words(text)` in `students/question_8.py`
- Question 9: create `get_max_number(numbers)` in `students/question_9.py`
- Question 10: create `is_palindrome(text)` in `students/question_10.py`
- Question 11: create `factorial(n)` in `students/question_11.py`
- Question 12: create `average_numbers(numbers)` in `students/question_12.py`
- Question 13: create `remove_duplicates(items)` in `students/question_13.py`
- Question 14: create `count_character(text, target)` in `students/question_14.py`
- Question 15: create `celsius_to_fahrenheit(celsius)` in `students/question_15.py`
- Question 16: create `filter_positive_numbers(numbers)` in `students/question_16.py`
- Question 17: create `get_last_element(items)` in `students/question_17.py`
- Question 18: create `sum_digits(number)` in `students/question_18.py`
- Question 19: create `sort_numbers(numbers)` in `students/question_19.py`
- Question 20: create `get_initials(full_name)` in `students/question_20.py`

Reference solutions follow the same pattern in `solutions/question_<number>.py`.
