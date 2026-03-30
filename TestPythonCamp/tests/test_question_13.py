import pytest

from TestPythonCamp.tests.exam_test_utils import (
    assert_function_result,
    get_required_function,
)


def get_remove_duplicates():
    return get_required_function(
        "TestPythonCamp.students.question_13",
        "remove_duplicates",
        "students/question_13.py",
    )


@pytest.mark.parametrize(
    ("items", "expected"),
    [
        ([1, 2, 2, 3, 1], [1, 2, 3]),
        (["a", "a", "b"], ["a", "b"]),
        ([], []),
    ],
)
def test_question_13_remove_duplicates(items, expected):
    remove_duplicates = get_remove_duplicates()
    assert_function_result(
        remove_duplicates,
        (items,),
        expected,
        f"remove_duplicates({items!r})",
    )
