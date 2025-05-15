"""Implements factory for path to resource."""

from pathlib import Path
from types import FunctionType, MethodType
from typing import Optional, Union

from pytest_resource_path.absolute_path_factory import AbsolutePathFactory
from pytest_resource_path.path_factory import PathFactory

__all__ = ["PathToResourceFactory"]


class PathToResourceFactory:
    """Implements factory fot path to resource."""

    DIRECTORY_NAME_TESTS_DEAFAULT = "tests"
    DIRECTORY_NAME_TEST_RESOURCES_DEFAULT = "testresources"
    """This class implements uniform access to test resources."""

    def __init__(self, path_tests: Optional[Path] = None, path_test_resources: Optional[Path] = None) -> None:
        initialized_path_tests = self._init_path(path_tests, self.DIRECTORY_NAME_TESTS_DEAFAULT)
        self.absolute_path_factory = AbsolutePathFactory(initialized_path_tests)
        self.path_test_resources = self._init_path(path_test_resources, self.DIRECTORY_NAME_TEST_RESOURCES_DEFAULT)

    @staticmethod
    def _init_path(path_test_resources: Optional[Path], default: str) -> Path:
        return Path(default) if path_test_resources is None else path_test_resources

    def create(self, item: Union[MethodType, FunctionType]) -> Path:
        """This method creates path to test resource directory."""
        absolute_path_tests = self.absolute_path_factory.create_by_function(item)
        path_to_resource_root = self._create_path_to_resource_root(absolute_path_tests)
        path_as_same_as_file_name = PathFactory.create_path_as_same_as_file_name(item)
        return path_to_resource_root / path_as_same_as_file_name.relative_to(absolute_path_tests) / item.__name__

    def create_path_to_resource_root(self, path: Path) -> Path:
        """Creates path to resource root."""
        return self._create_path_to_resource_root(self.absolute_path_factory.create_by_path(path))

    def _create_path_to_resource_root(self, absolute_path_tests: Path) -> Path:
        return absolute_path_tests / self.path_test_resources
