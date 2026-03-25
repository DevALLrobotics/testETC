import pytest

from TestPythonCamp.tests.exam_test_utils import (
    assert_function_result,
    get_required_function,
)


def get_add_numbers():
    return get_required_function(
        "TestPythonCamp.students.question_1",
        "add_numbers",
        "students/question_1.py",
    )


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (2, 3, 5),
        (-4, 10, 6),
        (1.5, 2.5, 4.0),
    ],
)
def test_question_1_add_numbers(a, b, expected):
    add_numbers = get_add_numbers()
    assert_function_result(
        add_numbers,
        (a, b),
        expected,
        f"add_numbers({a!r}, {b!r})",
    )
