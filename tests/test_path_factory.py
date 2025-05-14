"""Tests for path_factory.py."""

from pathlib import Path

import pytest

from pytest_resource_path.path_factory import PathFactory
from tests.testlibraries.function_getter import FunctionGetter


class TestPathFactory:
    """Tests for PathFactory."""

    @staticmethod
    def test_create_path_as_same_as_file_name(testdir_structure: pytest.Testdir) -> None:
        # noinspection LongLine
        # pylint:disable=line-too-long
        """Method should return path to module of argument method.

        @see
        https://github.com/pytest-dev/pytest/blob/3d0f3baa2bb89257dfff25ae6ebabd565287240e/testing/python/fixtures.py#L782
        # noqa
        """
        file_name_pytest = "test_module_something"
        function = FunctionGetter.get(file_name_pytest, testdir_structure)
        # noinspection PyProtectedMember
        path = PathFactory.create_path_as_same_as_file_name(function)
        assert path == Path(str(testdir_structure.tmpdir)) / "tests/test_package" / file_name_pytest
