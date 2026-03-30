import pytest

from TestPythonCamp.tests.exam_test_utils import (
    assert_function_result,
    get_required_function,
)


def get_sum_digits():
    return get_required_function(
        "TestPythonCamp.students.question_18",
        "sum_digits",
        "students/question_18.py",
    )


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (123, 6),
        (9001, 10),
        (0, 0),
        (-42, 6),
    ],
)
def test_question_18_sum_digits(number, expected):
    sum_digits = get_sum_digits()
    assert_function_result(
        sum_digits,
        (number,),
        expected,
        f"sum_digits({number!r})",
    )
