import pytest

from TestPythonCamp.tests.exam_test_utils import (
    assert_function_result,
    get_required_function,
)


def get_is_palindrome():
    return get_required_function(
        "TestPythonCamp.students.question_10",
        "is_palindrome",
        "students/question_10.py",
    )


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("level", True),
        ("python", False),
        ("madam", True),
        ("", True),
    ],
)
def test_question_10_is_palindrome(text, expected):
    is_palindrome = get_is_palindrome()
    assert_function_result(
        is_palindrome,
        (text,),
        expected,
        f"is_palindrome({text!r})",
    )
