"""Implements getting process for function object in pytest by pytest file name and testdir object."""
from tests.testlibraries.module_getter import ModuleGetter


class FunctionGetter:
    """Implements getting process for function object in pytest by pytest file name and testdir object."""

    @staticmethod
    def get(file_name_pytest: str, testdir_structure):
        """Gets function object."""
        modulecol = ModuleGetter.get(file_name_pytest, testdir_structure)
        (item,) = testdir_structure.genitems([modulecol])
        return item.obj
