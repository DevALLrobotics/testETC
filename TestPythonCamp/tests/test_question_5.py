import pytest

from TestPythonCamp.tests.exam_test_utils import (
    assert_function_result,
    assert_raises_value_error,
    get_required_function,
)


def get_find_top_student():
    return get_required_function(
        "TestPythonCamp.students.question_5",
        "find_top_student",
        "students/question_5.py",
    )


def test_question_5_find_top_student():
    find_top_student = get_find_top_student()
    scores = {"Ann": 82, "Boss": 91, "Mew": 88}
    assert_function_result(
        find_top_student,
        (scores,),
        "Boss",
        f"find_top_student({scores!r})",
    )


def test_question_5_find_top_student_empty_dict():
    find_top_student = get_find_top_student()
    assert_raises_value_error(
        find_top_student,
        ({},),
        "find_top_student({})",
    )
