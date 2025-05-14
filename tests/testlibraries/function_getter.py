"""Implements getting process for function object in pytest by pytest file name and testdir object."""

from types import FunctionType, MethodType
from typing import cast, Union

from _pytest.python import Function
import pytest

from tests.testlibraries.module_getter import ModuleGetter


class FunctionGetter:
    """Implements getting process for function object in pytest by pytest file name and testdir object."""

    @staticmethod
    def get(file_name_pytest: str, testdir_structure: pytest.Testdir) -> Union[MethodType, FunctionType]:
        """Gets function object."""
        modulecol = ModuleGetter.get(file_name_pytest, testdir_structure)
        (item,) = testdir_structure.genitems([modulecol])
        if isinstance(item, Function):
            return cast(FunctionType, item.obj)
        msg = "Currently, only the type: Function is supported."
        raise ValueError(msg)
