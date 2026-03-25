import pytest

from TestPythonCamp.tests.exam_test_utils import get_required_function


def get_find_top_student():
    return get_required_function(
        "TestPythonCamp.students.question_5",
        "find_top_student",
        "students/question_5.py",
    )


def test_question_5_find_top_student():
    find_top_student = get_find_top_student()
    scores = {"Ann": 82, "Boss": 91, "Mew": 88}
    assert find_top_student(scores) == "Boss"


def test_question_5_find_top_student_empty_dict():
    find_top_student = get_find_top_student()
    with pytest.raises(ValueError):
        find_top_student({})
