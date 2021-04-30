"""Implements getting process for module object in pytest by pytest file name and testdir object."""
import sys

if sys.version_info.major == 3 and sys.version_info.minor <= 5:  # pragma: nocover
    import pathlib2  # type: ignore # pylint: disable=import-error
else:  # pragma: nocover
    import pathlib


class ModuleGetter:
    """Implements getting process for nodule object in pytest by pytest file name and testdir object."""

    @staticmethod
    def get(file_name_pytest: str, testdir_structure):
        """Gets module object."""
        path_to_python_file_string = "tests/test_package/" + file_name_pytest + ".py"
        if sys.version_info.major == 3 and sys.version_info.minor <= 5:  # pragma: nocover
            path = pathlib2.Path(path_to_python_file_string)
        else:  # pragma: nocover
            path = pathlib.Path(path_to_python_file_string)
        return testdir_structure.getmodulecol(path)
