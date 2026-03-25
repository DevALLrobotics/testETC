import pytest

from TestPythonCamp.tests.exam_test_utils import get_required_function


def get_sum_even_numbers():
    return get_required_function(
        "TestPythonCamp.students.question_3",
        "sum_even_numbers",
        "students/question_3.py",
    )


@pytest.mark.parametrize(
    ("numbers", "expected"),
    [
        ([1, 2, 3, 4, 5, 6], 12),
        ([7, 9, 11], 0),
        ([-2, -1, 0, 1, 2], 0),
    ],
)
def test_question_3_sum_even_numbers(numbers, expected):
    sum_even_numbers = get_sum_even_numbers()
    assert sum_even_numbers(numbers) == expected
