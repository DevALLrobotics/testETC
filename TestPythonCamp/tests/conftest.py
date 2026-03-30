import _pytest.terminal


def pytest_configure(config):
    _pytest.terminal.TerminalReporter.short_test_summary = lambda self: None
