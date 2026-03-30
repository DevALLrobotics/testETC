import pytest

from TestPythonCamp.tests.exam_test_utils import (
    assert_function_result,
    get_required_function,
)


def get_count_character():
    return get_required_function(
        "TestPythonCamp.students.question_14",
        "count_character",
        "students/question_14.py",
    )


@pytest.mark.parametrize(
    ("text", "target", "expected"),
    [
        ("banana", "a", 3),
        ("Hello", "l", 2),
        ("Python", "z", 0),
    ],
)
def test_question_14_count_character(text, target, expected):
    count_character = get_count_character()
    assert_function_result(
        count_character,
        (text, target),
        expected,
        f"count_character({text!r}, {target!r})",
    )
