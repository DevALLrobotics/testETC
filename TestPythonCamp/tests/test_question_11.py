import pytest

from TestPythonCamp.tests.exam_test_utils import (
    assert_function_result,
    get_required_function,
)


def get_factorial():
    return get_required_function(
        "TestPythonCamp.students.question_11",
        "factorial",
        "students/question_11.py",
    )


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (0, 1),
        (1, 1),
        (5, 120),
        (6, 720),
    ],
)
def test_question_11_factorial(number, expected):
    factorial = get_factorial()
    assert_function_result(
        factorial,
        (number,),
        expected,
        f"factorial({number!r})",
    )
