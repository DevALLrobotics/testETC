import pytest

from TestPythonCamp.tests.exam_test_utils import (
    assert_function_result,
    get_required_function,
)


def get_count_words():
    return get_required_function(
        "TestPythonCamp.students.question_8",
        "count_words",
        "students/question_8.py",
    )


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("hello world", 2),
        ("  one   two three  ", 3),
        ("", 0),
    ],
)
def test_question_8_count_words(text, expected):
    count_words = get_count_words()
    assert_function_result(
        count_words,
        (text,),
        expected,
        f"count_words({text!r})",
    )
