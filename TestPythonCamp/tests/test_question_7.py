import pytest

from TestPythonCamp.tests.exam_test_utils import (
    assert_function_result,
    get_required_function,
)


def get_reverse_text():
    return get_required_function(
        "TestPythonCamp.students.question_7",
        "reverse_text",
        "students/question_7.py",
    )


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("cat", "tac"),
        ("Python", "nohtyP"),
        ("12345", "54321"),
        ("", ""),
    ],
)
def test_question_7_reverse_text(text, expected):
    reverse_text = get_reverse_text()
    assert_function_result(
        reverse_text,
        (text,),
        expected,
        f"reverse_text({text!r})",
    )
