from __future__ import annotations

import importlib
import sys
from dataclasses import dataclass
from pathlib import Path


if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


VALUE_ERROR = "VALUE_ERROR"


@dataclass(frozen=True)
class QuestionSpec:
    number: int
    function_name: str
    module_name: str
    file_name: str
    title: str
    cases: list[tuple[tuple, object]]


QUESTIONS = [
    QuestionSpec(
        number=1,
        function_name="add_numbers",
        module_name="TestPythonCamp.students.question_1",
        file_name="students/question_1.py",
        title="Add two numbers",
        cases=[
            ((2, 3), 5),
            ((-4, 10), 6),
            ((1.5, 2.5), 4.0),
        ],
    ),
    QuestionSpec(
        number=2,
        function_name="is_leap_year",
        module_name="TestPythonCamp.students.question_2",
        file_name="students/question_2.py",
        title="Check leap year",
        cases=[
            ((2024,), True),
            ((2023,), False),
            ((1900,), False),
            ((2000,), True),
        ],
    ),
    QuestionSpec(
        number=3,
        function_name="sum_even_numbers",
        module_name="TestPythonCamp.students.question_3",
        file_name="students/question_3.py",
        title="Sum even numbers",
        cases=[
            (([1, 2, 3, 4, 5, 6],), 12),
            (([7, 9, 11],), 0),
            (((-2, -1, 0, 1, 2),), 0),
        ],
    ),
    QuestionSpec(
        number=4,
        function_name="count_vowels",
        module_name="TestPythonCamp.students.question_4",
        file_name="students/question_4.py",
        title="Count vowels",
        cases=[
            (("Hello World",), 3),
            (("PYTHON",), 1),
            (("bcdfg",), 0),
            (("AeIoU",), 5),
            (("",), 0),
        ],
    ),
    QuestionSpec(
        number=5,
        function_name="find_top_student",
        module_name="TestPythonCamp.students.question_5",
        file_name="students/question_5.py",
        title="Find top student",
        cases=[
            (({"Ann": 82, "Boss": 91, "Mew": 88},), "Boss"),
            (({},), VALUE_ERROR),
        ],
    ),
    QuestionSpec(
        number=6,
        function_name="get_grade",
        module_name="TestPythonCamp.students.question_6",
        file_name="students/question_6.py",
        title="Convert score to grade",
        cases=[
            ((85,), "A"),
            ((72,), "B"),
            ((60,), "C"),
            ((50,), "D"),
            ((49,), "F"),
        ],
    ),
    QuestionSpec(
        number=7,
        function_name="reverse_text",
        module_name="TestPythonCamp.students.question_7",
        file_name="students/question_7.py",
        title="Reverse text",
        cases=[
            (("cat",), "tac"),
            (("Python",), "nohtyP"),
            (("12345",), "54321"),
            (("",), ""),
        ],
    ),
    QuestionSpec(
        number=8,
        function_name="count_words",
        module_name="TestPythonCamp.students.question_8",
        file_name="students/question_8.py",
        title="Count words",
        cases=[
            (("hello world",), 2),
            (("  one   two three  ",), 3),
            (("",), 0),
        ],
    ),
    QuestionSpec(
        number=9,
        function_name="get_max_number",
        module_name="TestPythonCamp.students.question_9",
        file_name="students/question_9.py",
        title="Find max number",
        cases=[
            (([3, 7, 2],), 7),
            (([-5, -2, -9],), -2),
            (([10],), 10),
            (([],), VALUE_ERROR),
        ],
    ),
    QuestionSpec(
        number=10,
        function_name="is_palindrome",
        module_name="TestPythonCamp.students.question_10",
        file_name="students/question_10.py",
        title="Check palindrome",
        cases=[
            (("level",), True),
            (("python",), False),
            (("madam",), True),
            (("",), True),
        ],
    ),
    QuestionSpec(
        number=11,
        function_name="factorial",
        module_name="TestPythonCamp.students.question_11",
        file_name="students/question_11.py",
        title="Calculate factorial",
        cases=[
            ((0,), 1),
            ((1,), 1),
            ((5,), 120),
            ((6,), 720),
        ],
    ),
    QuestionSpec(
        number=12,
        function_name="average_numbers",
        module_name="TestPythonCamp.students.question_12",
        file_name="students/question_12.py",
        title="Average numbers",
        cases=[
            (([10, 20, 30],), 20.0),
            (([5],), 5.0),
            (([1, 2],), 1.5),
            (([],), VALUE_ERROR),
        ],
    ),
    QuestionSpec(
        number=13,
        function_name="remove_duplicates",
        module_name="TestPythonCamp.students.question_13",
        file_name="students/question_13.py",
        title="Remove duplicates",
        cases=[
            (([1, 2, 2, 3, 1],), [1, 2, 3]),
            ((["a", "a", "b"],), ["a", "b"]),
            (([],), []),
        ],
    ),
    QuestionSpec(
        number=14,
        function_name="count_character",
        module_name="TestPythonCamp.students.question_14",
        file_name="students/question_14.py",
        title="Count character",
        cases=[
            (("banana", "a"), 3),
            (("Hello", "l"), 2),
            (("Python", "z"), 0),
        ],
    ),
    QuestionSpec(
        number=15,
        function_name="celsius_to_fahrenheit",
        module_name="TestPythonCamp.students.question_15",
        file_name="students/question_15.py",
        title="Convert Celsius to Fahrenheit",
        cases=[
            ((0,), 32.0),
            ((100,), 212.0),
            ((-40,), -40.0),
            ((25,), 77.0),
        ],
    ),
    QuestionSpec(
        number=16,
        function_name="filter_positive_numbers",
        module_name="TestPythonCamp.students.question_16",
        file_name="students/question_16.py",
        title="Filter positive numbers",
        cases=[
            (([1, -2, 3, 0, 5],), [1, 3, 5]),
            (([-1, -2],), []),
            (([0, 2],), [2]),
        ],
    ),
    QuestionSpec(
        number=17,
        function_name="get_last_element",
        module_name="TestPythonCamp.students.question_17",
        file_name="students/question_17.py",
        title="Get last element",
        cases=[
            (([1, 2, 3],), 3),
            ((["a", "b"],), "b"),
            (([],), VALUE_ERROR),
        ],
    ),
    QuestionSpec(
        number=18,
        function_name="sum_digits",
        module_name="TestPythonCamp.students.question_18",
        file_name="students/question_18.py",
        title="Sum digits",
        cases=[
            ((123,), 6),
            ((9001,), 10),
            ((0,), 0),
            ((-42,), 6),
        ],
    ),
    QuestionSpec(
        number=19,
        function_name="sort_numbers",
        module_name="TestPythonCamp.students.question_19",
        file_name="students/question_19.py",
        title="Sort numbers",
        cases=[
            (([3, 1, 2],), [1, 2, 3]),
            (([-1, 5, 0],), [-1, 0, 5]),
            (([],), []),
        ],
    ),
    QuestionSpec(
        number=20,
        function_name="get_initials",
        module_name="TestPythonCamp.students.question_20",
        file_name="students/question_20.py",
        title="Get initials",
        cases=[
            (("John Doe",), "JD"),
            (("alice bob carol",), "ABC"),
            (("Single",), "S"),
            (("  mary   jane  ",), "MJ"),
        ],
    ),
]


def format_call(function_name: str, args: tuple) -> str:
    rendered_args = ", ".join(repr(arg) for arg in args)
    return f"{function_name}({rendered_args})"


def load_function(spec: QuestionSpec):
    try:
        module = importlib.import_module(spec.module_name)
    except Exception as error:
        print(f"[ERROR] Could not load {spec.file_name}")
        print(f"        {type(error).__name__}: {error}")
        return None

    function = getattr(module, spec.function_name, None)
    if function is None:
        print(
            f"[ERROR] Missing function `{spec.function_name}` in {spec.file_name}"
        )
        return None

    if not callable(function):
        print(
            f"[ERROR] `{spec.function_name}` in {spec.file_name} is not a function"
        )
        return None

    return function


def run_case(function, function_name: str, args: tuple, expected: object) -> bool:
    call_text = format_call(function_name, args)

    try:
        actual = function(*args)
    except Exception as error:
        if expected == VALUE_ERROR and isinstance(error, ValueError):
            print(f"[PASS] {call_text}")
            return True

        print(f"[FAIL] {call_text}")
        print(f"       Code crashed: {type(error).__name__}: {error}")
        return False

    if expected == VALUE_ERROR:
        print(f"[FAIL] {call_text}")
        print("       Expected: ValueError")
        print(f"       Got: {actual!r}")
        return False

    if actual == expected:
        print(f"[PASS] {call_text}")
        return True

    print(f"[FAIL] {call_text}")
    print(f"       Expected: {expected!r}")
    print(f"       Got: {actual!r}")
    return False


def run_question(spec: QuestionSpec) -> tuple[int, int]:
    print(f"Question {spec.number}: {spec.function_name}")
    print(f"Topic: {spec.title}")

    function = load_function(spec)
    if function is None:
        print("Result: 0 passed")
        print()
        return 0, len(spec.cases)

    passed = 0
    total = len(spec.cases)

    for args, expected in spec.cases:
        if run_case(function, spec.function_name, args, expected):
            passed += 1

    print(f"Result: {passed}/{total} passed")
    print()
    return passed, total


def parse_question_numbers(argv: list[str]) -> list[int]:
    if not argv:
        return [spec.number for spec in QUESTIONS]

    numbers = []
    for value in argv:
        try:
            number = int(value)
        except ValueError:
            raise SystemExit(
                "Usage: python3 TestPythonCamp/check.py [question_number ...]"
            ) from None

        numbers.append(number)

    valid_numbers = {spec.number for spec in QUESTIONS}
    invalid_numbers = [number for number in numbers if number not in valid_numbers]
    if invalid_numbers:
        invalid_text = ", ".join(str(number) for number in invalid_numbers)
        raise SystemExit(f"Unknown question number: {invalid_text}")

    return numbers


def main(argv: list[str]) -> int:
    selected_numbers = parse_question_numbers(argv)
    selected_specs = [
        spec for spec in QUESTIONS if spec.number in selected_numbers
    ]

    total_passed = 0
    total_cases = 0

    for spec in selected_specs:
        passed, total = run_question(spec)
        total_passed += passed
        total_cases += total

    print("Summary")
    print(f"Passed: {total_passed}/{total_cases}")

    if total_passed != total_cases:
        print("Status: FAIL")
        return 1

    print("Status: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
