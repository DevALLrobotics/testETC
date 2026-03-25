import importlib

import pytest


def get_required_function(module_name: str, function_name: str, file_name: str):
    module = importlib.import_module(module_name)
    function = getattr(module, function_name, None)

    if function is None:
        pytest.fail(
            f"Please create `{function_name}` in `{file_name}` before running this test."
        )

    if not callable(function):
        pytest.fail(f"`{function_name}` in `{file_name}` must be a function.")

    return function
