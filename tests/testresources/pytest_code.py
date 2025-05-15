"""This module is run in test_dir on pytest for test pytest FixtureRequest."""


def test_function_something() -> None:
    """This test is run in test_dir on pytest for test pytest FixtureRequest."""
    expected = 2
    actual = 1 + 1
    assert actual == expected
