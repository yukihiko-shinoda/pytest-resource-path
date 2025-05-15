"""Implements getting process for module object in pytest by pytest file name and testdir object."""

import pathlib
from typing import cast

import pytest


class ModuleGetter:
    """Implements getting process for nodule object in pytest by pytest file name and testdir object."""

    @staticmethod
    def get(file_name_pytest: str, testdir_structure: pytest.Testdir) -> pytest.Module:
        """Gets module object."""
        path_to_python_file_string = "tests/test_package/" + file_name_pytest + ".py"
        path = pathlib.Path(path_to_python_file_string)
        # Reason: Pytest's issue
        return cast(pytest.Module, testdir_structure.getmodulecol(path))  # type: ignore[no-untyped-call]
