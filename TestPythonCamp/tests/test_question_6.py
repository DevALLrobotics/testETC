import pytest

from TestPythonCamp.tests.exam_test_utils import (
    assert_function_result,
    get_required_function,
)


def get_get_grade():
    return get_required_function(
        "TestPythonCamp.students.question_6",
        "get_grade",
        "students/question_6.py",
    )


@pytest.mark.parametrize(
    ("score", "expected"),
    [
        (85, "A"),
        (72, "B"),
        (60, "C"),
        (50, "D"),
        (49, "F"),
    ],
)
def test_question_6_get_grade(score, expected):
    get_grade = get_get_grade()
    assert_function_result(
        get_grade,
        (score,),
        expected,
        f"get_grade({score!r})",
    )
