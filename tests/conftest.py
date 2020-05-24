"""Implements config for pytest."""
from pathlib import Path

import pytest  # type: ignore

pytest_plugins = "pytester"  # pylint: disable=invalid-name


@pytest.fixture
def testdir_structure(testdir):
    """
    This fixture prepares basic directory structure on testdir.
    This fixture is for testing pytestresource.
    """
    yield from create_directory_structure(testdir, "pytest_code.py")


@pytest.fixture
def testdir_structure_for_testing_resource_path(testdir):
    """
    This fixture prepares basic directory structure on testdir.
    This fixture is for testing pytestresource.
    """
    yield from create_directory_structure(testdir, "pytest_resource_path.py")


@pytest.fixture
def testdir_structure_for_testing_ini(testdir):
    """
    This fixture prepares basic directory structure on testdir.
    This fixture is for testing pytestresource.
    """
    yield from create_directory_structure(testdir, "pytest_resource_path_ini.py", "integrationtests")


def create_directory_structure(testdir, file_name: str, directory_name_tests: str = "tests"):
    """Creates directory structure."""
    testdir.makepyfile(__init__="")
    directory_tests = testdir.mkpydir(directory_name_tests)
    tmpdir_default = testdir.tmpdir
    testdir.tmpdir = directory_tests
    testdir.mkpydir("test_package")
    testdir.tmpdir = tmpdir_default
    module_name = directory_name_tests + "/test_package/test_module_something"
    testdir.makepyfile(**{module_name: (Path(__file__).parent / "testresources" / file_name).read_text()})
    yield testdir
