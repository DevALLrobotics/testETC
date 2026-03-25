import pytest

from TestPythonCamp.tests.exam_test_utils import get_required_function


def get_count_vowels():
    return get_required_function(
        "TestPythonCamp.students.question_4",
        "count_vowels",
        "students/question_4.py",
    )


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello World", 3),
        ("PYTHON", 1),
        ("bcdfg", 0),
        ("AeIoU", 5),
        ("", 0),
    ],
)
def test_question_4_count_vowels(text, expected):
    count_vowels = get_count_vowels()
    assert count_vowels(text) == expected
