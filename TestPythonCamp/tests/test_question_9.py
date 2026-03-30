import pytest

from TestPythonCamp.tests.exam_test_utils import (
    assert_function_result,
    assert_raises_value_error,
    get_required_function,
)


def get_get_max_number():
    return get_required_function(
        "TestPythonCamp.students.question_9",
        "get_max_number",
        "students/question_9.py",
    )


@pytest.mark.parametrize(
    ("numbers", "expected"),
    [
        ([3, 7, 2], 7),
        ([-5, -2, -9], -2),
        ([10], 10),
    ],
)
def test_question_9_get_max_number(numbers, expected):
    get_max_number = get_get_max_number()
    assert_function_result(
        get_max_number,
        (numbers,),
        expected,
        f"get_max_number({numbers!r})",
    )


def test_question_9_get_max_number_empty_list():
    get_max_number = get_get_max_number()
    assert_raises_value_error(
        get_max_number,
        ([],),
        "get_max_number([])",
    )
