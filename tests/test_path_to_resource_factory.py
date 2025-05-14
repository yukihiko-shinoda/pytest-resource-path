"""Tests for path_to_resource_factory.py."""

from pathlib import Path

import pytest

from pytest_resource_path import PathToResourceFactory
from tests.testlibraries.function_getter import FunctionGetter
from tests.testlibraries.module_getter import ModuleGetter


class TestPathToResourceFactory:
    """Tests for path_to_resource_factory.py."""

    @staticmethod
    def test_create(testdir_structure: pytest.Testdir) -> None:
        # noinspection LongLine
        # pylint:disable=line-too-long
        """Method should return path to resource directory of argument method.

        @see
        https://github.com/pytest-dev/pytest/blob/3d0f3baa2bb89257dfff25ae6ebabd565287240e/testing/python/fixtures.py#L782
        # noqa
        """
        file_name_pytest = "test_module_something"
        function = FunctionGetter.get(file_name_pytest, testdir_structure)
        path = PathToResourceFactory().create(function)
        assert (
            path
            == Path(str(testdir_structure.tmpdir))
            / "tests/testresources/test_package"
            / file_name_pytest
            / "test_function_something"
        )

    @staticmethod
    def test_create_path_to_resource_root(testdir_structure: pytest.Testdir) -> None:
        # noinspection LongLine
        # pylint:disable=line-too-long
        """Method should return path to resource directory of argument method.

        @see
        https://github.com/pytest-dev/pytest/blob/3d0f3baa2bb89257dfff25ae6ebabd565287240e/testing/python/fixtures.py#L782
        # noqa
        """
        file_name_pytest = "test_module_something"
        module = ModuleGetter.get(file_name_pytest, testdir_structure)
        path = PathToResourceFactory().create_path_to_resource_root(Path(str(module.fspath)).resolve())
        assert path == Path(str(testdir_structure.tmpdir) + "/tests/testresources")

    @staticmethod
    def test_run_test_in_sub_directory(testdir_structure: pytest.Testdir) -> None:
        """Pytest in sub directory in temporary directory should work well."""
        result = testdir_structure.runpytest("-v")

        # fnmatch_lines does an assertion internally
        result.stdout.fnmatch_lines(["*tests/test_package/test_module_something.py::test_function_something PASSED*"])

        # make sure that that we get a '0' exit code for the testsuite
        assert result.ret == 0
