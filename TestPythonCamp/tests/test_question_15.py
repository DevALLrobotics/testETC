import pytest

from TestPythonCamp.tests.exam_test_utils import (
    assert_function_result,
    get_required_function,
)


def get_celsius_to_fahrenheit():
    return get_required_function(
        "TestPythonCamp.students.question_15",
        "celsius_to_fahrenheit",
        "students/question_15.py",
    )


@pytest.mark.parametrize(
    ("celsius", "expected"),
    [
        (0, 32.0),
        (100, 212.0),
        (-40, -40.0),
        (25, 77.0),
    ],
)
def test_question_15_celsius_to_fahrenheit(celsius, expected):
    celsius_to_fahrenheit = get_celsius_to_fahrenheit()
    assert_function_result(
        celsius_to_fahrenheit,
        (celsius,),
        expected,
        f"celsius_to_fahrenheit({celsius!r})",
    )
