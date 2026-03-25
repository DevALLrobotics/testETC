import pytest

from TestPythonCamp.tests.exam_test_utils import get_required_function


def get_is_leap_year():
    return get_required_function(
        "TestPythonCamp.students.question_2",
        "is_leap_year",
        "students/question_2.py",
    )


@pytest.mark.parametrize(
    ("year", "expected"),
    [
        (2024, True),
        (2023, False),
        (1900, False),
        (2000, True),
    ],
)
def test_question_2_is_leap_year(year, expected):
    is_leap_year = get_is_leap_year()
    assert is_leap_year(year) is expected
