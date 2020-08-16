"""Implements creating process for absolute path to argument of constructor."""
from pathlib import Path
from types import FunctionType, MethodType
from typing import Union

from pytest_resource_path.exceptions import LogicError
from pytest_resource_path.path_factory import PathFactory

__all__ = ["AbsolutePathFactory"]


class AbsolutePathFactory:
    """Implements creating process for absolute path to argument of constructor."""

    def __init__(self, path_target: Path):
        self.path_target = path_target

    def create(self, item: Union[MethodType, FunctionType]) -> Path:
        """Creates absolute path to parh_target."""
        path = PathFactory.create_absolute_path(item)
        index = None
        index_tests = None
        string_path_tests = str(self.path_target)
        for index, part in enumerate(path.parts):
            if part == string_path_tests:
                index_tests = index
        if index is None or index_tests is None:
            raise LogicError(  # pragma: no cover
                "Unexpected path.\n"
                "path = " + str(path) + ",\n"
                "string_path_tests = " + string_path_tests + ",\n"
                "index_tests, " + str(index_tests) + ",\n"
                "index = " + str(index)
            )
        return path.parents[index - index_tests - 1]
