import pytest

from TestPythonCamp.tests.exam_test_utils import (
    assert_function_result,
    get_required_function,
)


def get_get_initials():
    return get_required_function(
        "TestPythonCamp.students.question_20",
        "get_initials",
        "students/question_20.py",
    )


@pytest.mark.parametrize(
    ("full_name", "expected"),
    [
        ("John Doe", "JD"),
        ("alice bob carol", "ABC"),
        ("Single", "S"),
        ("  mary   jane  ", "MJ"),
    ],
)
def test_question_20_get_initials(full_name, expected):
    get_initials = get_get_initials()
    assert_function_result(
        get_initials,
        (full_name,),
        expected,
        f"get_initials({full_name!r})",
    )
