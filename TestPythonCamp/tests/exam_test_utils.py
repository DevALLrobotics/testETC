import importlib

import pytest


def get_required_function(module_name: str, function_name: str, file_name: str):
    module = importlib.import_module(module_name)
    function = getattr(module, function_name, None)

    if function is None:
        pytest.fail(
            f"Please create function `{function_name}` in `{file_name}` before running this test."
        )

    if not callable(function):
        pytest.fail(
            f"`{function_name}` in `{file_name}` must be a function created with `def {function_name}(...):`."
        )

    return function


def assert_function_result(function, args, expected, call_text):
    try:
        actual = function(*args)
    except Exception as error:
        pytest.fail(
            f"Your code crashed while running {call_text}\n"
            f"Error: {type(error).__name__}: {error}"
        )

    if actual != expected:
        pytest.fail(
            f"Wrong answer for {call_text}\n"
            f"Expected: {expected!r}\n"
            f"Got: {actual!r}"
        )


def assert_raises_value_error(function, args, call_text):
    try:
        function(*args)
    except ValueError:
        return
    except Exception as error:
        pytest.fail(
            f"{call_text} should raise ValueError, but your code raised "
            f"{type(error).__name__}: {error}"
        )

    pytest.fail(f"{call_text} should raise ValueError, but no error was raised.")
