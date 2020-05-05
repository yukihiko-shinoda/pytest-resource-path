import sys
from os.path import splitext
from pathlib import Path
from types import MethodType, FunctionType
from typing import Optional, Union

from pytest_resource_path.exceptions import LogicError


class PathToResourceFactory:
    DIRECTORY_NAME_TESTS_DEAFAULT = 'tests'
    DIRECTORY_NAME_TEST_RESOURCES_DEFAULT = 'testresources'
    """This class implements uniform access to test resources."""
    def __init__(self, path_tests: Path = None, path_test_resources: Optional[Path] = None):
        self.path_tests = self._init_path(path_tests, self.DIRECTORY_NAME_TESTS_DEAFAULT)
        self.path_test_resources = self._init_path(
            path_test_resources, self.DIRECTORY_NAME_TEST_RESOURCES_DEFAULT)

    @staticmethod
    def _init_path(path_test_resources: Optional[Path], default) -> Path:
        return Path(default) if path_test_resources is None else path_test_resources

    def create(self, item: Union[MethodType, FunctionType]) -> Path:
        """This method creates path to test resource directory."""
        absolute_path_tests = self._create_absolute_path_tests(item)
        path_to_resource_root = self._create_path_to_resource_root(absolute_path_tests)
        path_as_same_as_file_name = self._create_path_as_same_as_file_name(item)
        return path_to_resource_root / path_as_same_as_file_name.relative_to(
            self._create_absolute_path_tests(item)) / item.__name__

    def create_path_to_resource_root(self, item: Union[MethodType, FunctionType]) -> Path:
        return self._create_path_to_resource_root(self._create_absolute_path_tests(item))

    def _create_path_to_resource_root(self, absolute_path_tests: Path) -> Path:
        return absolute_path_tests / self.path_test_resources

    def _create_absolute_path_tests(self, item: Union[MethodType, FunctionType]) -> Path:
        """This method creates and returns path as same as file name."""
        path = Path(self._create_string_absolute_path(item)).resolve(True)
        index: Optional[int] = None
        index_tests: Optional[int] = None
        string_path_tests = str(self.path_tests)
        for index, part in enumerate(path.parts):
            if part == string_path_tests:
                index_tests = index
        if index is None or index_tests is None:
            raise LogicError(  # pragma: no cover
                f'Unexpected path.\n'
                f'path = {path},\n'
                f'string_path_tests = {string_path_tests},\n'
                f'index_tests, {index_tests},\n'
                f'index = {index}'
            )
        return path.parents[index - index_tests - 1]

    @classmethod
    def _create_path_as_same_as_file_name(cls, item: Union[MethodType, FunctionType]) -> Path:
        """This method creates and returns path as same as file name."""
        return Path(splitext(cls._create_string_absolute_path(item))[0])

    @classmethod
    def _create_string_absolute_path(cls, item: Union[MethodType, FunctionType]) -> str:
        return sys.modules[item.__module__].__file__
