"""Implements getting process for function object in pytest by pytest file name and testdir object."""

from __future__ import annotations

from typing import TYPE_CHECKING
from typing import cast

from _pytest.python import Function

from tests.testlibraries.module_getter import ModuleGetter

if TYPE_CHECKING:
    from types import FunctionType
    from types import MethodType

    import pytest


class FunctionGetter:
    """Implements getting process for function object in pytest by pytest file name and testdir object."""

    @staticmethod
    def get(file_name_pytest: str, testdir_structure: pytest.Testdir) -> MethodType | FunctionType:
        """Gets function object."""
        modulecol = ModuleGetter.get(file_name_pytest, testdir_structure)
        (item,) = testdir_structure.genitems([modulecol])
        if isinstance(item, Function):
            return cast("FunctionType", item.obj)
        msg = "Currently, only the type: Function is supported."
        raise ValueError(msg)
