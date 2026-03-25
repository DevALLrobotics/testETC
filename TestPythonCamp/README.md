# Python Basic Exam with `pytest`

Thai version: [README_TH.md](README_TH.md)

This folder contains a small Python basic exam with 7 questions.

Files:
- `student.py`: overview file
- `students/`: student templates for each question
- `solution.py`: solution overview file
- `solutions/`: reference solutions
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

Rules:
- Edit only the matching student file for each question
- Do not change files in `tests/`
- For question 5, raise `ValueError` when the dictionary is empty

Usage:
1. Install `pytest`
2. Write your answer in the matching template under `students/`
3. Run the tests

How to run all questions:
```bash
python3 -m pip install pytest
python3 -m pytest TestPythonCamp/tests -q
```

How to run one question at a time:
```bash
python3 -m pytest TestPythonCamp/tests/test_question_1.py -q
python3 -m pytest TestPythonCamp/tests/test_question_2.py -q
python3 -m pytest TestPythonCamp/tests/test_question_3.py -q
python3 -m pytest TestPythonCamp/tests/test_question_4.py -q
python3 -m pytest TestPythonCamp/tests/test_question_5.py -q
python3 -m pytest TestPythonCamp/tests/test_question_6.py -q
python3 -m pytest TestPythonCamp/tests/test_question_7.py -q
```

Question mapping:
- Question 1: create `add_numbers(a, b)` in `students/question_1.py`
- Question 2: create `is_leap_year(year)` in `students/question_2.py`
- Question 3: create `sum_even_numbers(numbers)` in `students/question_3.py`
- Question 4: create `count_vowels(text)` in `students/question_4.py`
- Question 5: create `find_top_student(scores)` in `students/question_5.py`
- Question 6: create `get_grade(score)` in `students/question_6.py`
- Question 7: create `reverse_text(text)` in `students/question_7.py`

Reference solutions:
- Question 1: `solutions/question_1.py`
- Question 2: `solutions/question_2.py`
- Question 3: `solutions/question_3.py`
- Question 4: `solutions/question_4.py`
- Question 5: `solutions/question_5.py`
- Question 6: `solutions/question_6.py`
- Question 7: `solutions/question_7.py`
