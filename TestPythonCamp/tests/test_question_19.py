import pytest

from TestPythonCamp.tests.exam_test_utils import (
    assert_function_result,
    get_required_function,
)


def get_sort_numbers():
    return get_required_function(
        "TestPythonCamp.students.question_19",
        "sort_numbers",
        "students/question_19.py",
    )


@pytest.mark.parametrize(
    ("numbers", "expected"),
    [
        ([3, 1, 2], [1, 2, 3]),
        ([-1, 5, 0], [-1, 0, 5]),
        ([], []),
    ],
)
def test_question_19_sort_numbers(numbers, expected):
    sort_numbers = get_sort_numbers()
    assert_function_result(
        sort_numbers,
        (numbers,),
        expected,
        f"sort_numbers({numbers!r})",
    )
