import pytest

from TestPythonCamp.tests.exam_test_utils import (
    assert_function_result,
    assert_raises_value_error,
    get_required_function,
)


def get_average_numbers():
    return get_required_function(
        "TestPythonCamp.students.question_12",
        "average_numbers",
        "students/question_12.py",
    )


@pytest.mark.parametrize(
    ("numbers", "expected"),
    [
        ([10, 20, 30], 20.0),
        ([5], 5.0),
        ([1, 2], 1.5),
    ],
)
def test_question_12_average_numbers(numbers, expected):
    average_numbers = get_average_numbers()
    assert_function_result(
        average_numbers,
        (numbers,),
        expected,
        f"average_numbers({numbers!r})",
    )


def test_question_12_average_numbers_empty_list():
    average_numbers = get_average_numbers()
    assert_raises_value_error(
        average_numbers,
        ([],),
        "average_numbers([])",
    )
