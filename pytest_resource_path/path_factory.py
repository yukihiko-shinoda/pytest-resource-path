"""Implements creating process for several pathlib object."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types import FunctionType
    from types import MethodType

__all__ = ["PathFactory"]


class PathFactory:
    """Implements creating process for several pathlib object."""

    @classmethod
    def create_path_as_same_as_file_name(cls, item: MethodType | FunctionType) -> Path:
        """Creates and returns path as same as file name."""
        path = Path(cls._create_string_absolute_path(item))
        return path.parent / path.stem

    @classmethod
    def create_absolute_path_by_function(cls, item: MethodType | FunctionType) -> Path:
        """Creates absolute path."""
        return Path(cls._create_string_absolute_path(item)).resolve()

    @classmethod
    def _create_string_absolute_path(cls, item: MethodType | FunctionType) -> str:
        file = sys.modules[item.__module__].__file__
        # Reason: Only for unexpected case.
        if not file:  # pragma: no cover
            msg = "File not found."
            raise ValueError(msg)
        return file
