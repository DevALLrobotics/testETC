import pytest

from TestPythonCamp.tests.exam_test_utils import (
    assert_function_result,
    assert_raises_value_error,
    get_required_function,
)


def get_get_last_element():
    return get_required_function(
        "TestPythonCamp.students.question_17",
        "get_last_element",
        "students/question_17.py",
    )


@pytest.mark.parametrize(
    ("items", "expected"),
    [
        ([1, 2, 3], 3),
        (["a", "b"], "b"),
    ],
)
def test_question_17_get_last_element(items, expected):
    get_last_element = get_get_last_element()
    assert_function_result(
        get_last_element,
        (items,),
        expected,
        f"get_last_element({items!r})",
    )


def test_question_17_get_last_element_empty_list():
    get_last_element = get_get_last_element()
    assert_raises_value_error(
        get_last_element,
        ([],),
        "get_last_element([])",
    )
