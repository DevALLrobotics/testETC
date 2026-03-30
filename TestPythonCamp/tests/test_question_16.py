import pytest

from TestPythonCamp.tests.exam_test_utils import (
    assert_function_result,
    get_required_function,
)


def get_filter_positive_numbers():
    return get_required_function(
        "TestPythonCamp.students.question_16",
        "filter_positive_numbers",
        "students/question_16.py",
    )


@pytest.mark.parametrize(
    ("numbers", "expected"),
    [
        ([1, -2, 3, 0, 5], [1, 3, 5]),
        ([-1, -2], []),
        ([0, 2], [2]),
    ],
)
def test_question_16_filter_positive_numbers(numbers, expected):
    filter_positive_numbers = get_filter_positive_numbers()
    assert_function_result(
        filter_positive_numbers,
        (numbers,),
        expected,
        f"filter_positive_numbers({numbers!r})",
    )
