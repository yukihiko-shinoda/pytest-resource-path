"""Implements creating process for several pathlib object."""
import sys
from os.path import splitext
from pathlib import Path
from types import FunctionType, MethodType
from typing import Union

__all__ = ["PathFactory"]


class PathFactory:
    """Implements creating process for several pathlib object."""

    @classmethod
    def create_path_as_same_as_file_name(cls, item: Union[MethodType, FunctionType]) -> Path:
        """Creates and returns path as same as file name."""
        return Path(splitext(cls._create_string_absolute_path(item))[0])

    @classmethod
    def create_absolute_path(cls, item: Union[MethodType, FunctionType]) -> Path:
        """Creates absolute path."""
        return Path(cls._create_string_absolute_path(item)).resolve()

    @classmethod
    def _create_string_absolute_path(cls, item: Union[MethodType, FunctionType]) -> str:
        return sys.modules[item.__module__].__file__
