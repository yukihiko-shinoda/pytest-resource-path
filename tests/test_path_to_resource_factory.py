"""Tests for path_to_resource_factory.py"""
import sys
if sys.version_info.major == 3 and sys.version_info.minor <= 5:  # pragma: nocover
    import pathlib2
else:  # pragma: nocover
    import pathlib
from pathlib import Path

from pytest_resource_path import PathToResourceFactory


class TestPathToResourceFactory:
    def test_create(self, testdir_structure):
        # noinspection LongLine
        # pylint:disable=line-too-long
        """
        Method should return path to resource directory of argument method.
        @see https://github.com/pytest-dev/pytest/blob/3d0f3baa2bb89257dfff25ae6ebabd565287240e/testing/python/fixtures.py#L782 # noqa
        """
        file_name_pytest = 'test_module_something'
        function = self.get_function(file_name_pytest, testdir_structure)
        path = PathToResourceFactory().create(function)
        assert path == Path(
            str(testdir_structure.tmpdir)
        ) / 'tests/testresources/test_package' / file_name_pytest / 'test_function_something'

    def test_create_path_to_resource_root(self, testdir_structure):
        # noinspection LongLine
        # pylint:disable=line-too-long
        """
        Method should return path to resource directory of argument method.
        @see https://github.com/pytest-dev/pytest/blob/3d0f3baa2bb89257dfff25ae6ebabd565287240e/testing/python/fixtures.py#L782 # noqa
        """
        file_name_pytest = 'test_module_something'
        function = self.get_function(file_name_pytest, testdir_structure)
        path = PathToResourceFactory().create_path_to_resource_root(function)
        assert path == Path(str(testdir_structure.tmpdir) + '/tests/testresources')

    def test_create_absolute_path_tests(self, testdir_structure):
        file_name_pytest = 'test_module_something'
        function = self.get_function(file_name_pytest, testdir_structure)
        # noinspection PyProtectedMember
        path = PathToResourceFactory()._create_absolute_path_tests(function)
        assert path.is_absolute() is True
        assert path.name == 'tests'

    def test_create_path_as_same_as_file_name(self, testdir_structure):
        # noinspection LongLine
        # pylint:disable=line-too-long
        """
        Method should return path to module of argument method.
        @see https://github.com/pytest-dev/pytest/blob/3d0f3baa2bb89257dfff25ae6ebabd565287240e/testing/python/fixtures.py#L782 # noqa
        """
        file_name_pytest = 'test_module_something'
        function = self.get_function(file_name_pytest, testdir_structure)
        # noinspection PyProtectedMember
        path = PathToResourceFactory()._create_path_as_same_as_file_name(function)
        assert path == Path(str(testdir_structure.tmpdir)) / 'tests/test_package' / file_name_pytest

    def test_run_test_in_sub_directory(self, testdir_structure):
        result = testdir_structure.runpytest('-v')

        # fnmatch_lines does an assertion internally
        result.stdout.fnmatch_lines([
            '*tests/test_package/test_module_something.py::test_function_something PASSED*',
        ])

        # make sure that that we get a '0' exit code for the testsuite
        assert result.ret == 0

    @staticmethod
    def get_function(file_name_pytest: str, testdir_structure):
        if sys.version_info.major == 3 and sys.version_info.minor <= 5:  # pragma: nocover
            path = pathlib2.Path('tests/test_package/' + file_name_pytest + '.py')
        else:  # pragma: nocover
            path = pathlib.Path('tests/test_package/' + file_name_pytest + '.py')
        modulecol = testdir_structure.getmodulecol(path)
        (item,) = testdir_structure.genitems([modulecol])
        return item.obj
