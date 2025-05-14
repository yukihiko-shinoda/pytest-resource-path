"""Tests for absolute_path_factory.py."""

from pathlib import Path

import pytest

from pytest_resource_path.absolute_path_factory import AbsolutePathFactory
from tests.testlibraries.function_getter import FunctionGetter


class TestAbsolutePathFactory:
    """Tests for AbsolutePathFactory."""

    @staticmethod
    def test_create_absolute_path_tests(testdir_structure: pytest.Testdir) -> None:
        """Method create_absolute_path() should return absolute path."""
        file_name_pytest = "test_module_something"
        function = FunctionGetter.get(file_name_pytest, testdir_structure)
        # noinspection PyProtectedMember
        path = AbsolutePathFactory(Path("tests")).create_by_function(function)
        assert path.is_absolute() is True
        assert path.name == "tests"
