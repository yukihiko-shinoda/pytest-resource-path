"""Test for pytest."""
from pathlib import Path

import pytest  # type: ignore

from pytest_resource_path.path_to_resource_factory import PathToResourceFactory

__all__ = [
    "INI_KEY_DIRECTORY_NAME_TESTS",
    "INI_KEY_DIRECTORY_NAME_TEST_RESOURCES",
    "pytest_addoption",
    "resource_path",
    "resource_path_root",
    "create_path_to_resource_factory",
]

INI_KEY_DIRECTORY_NAME_TESTS = "resource-path.directory-name-tests"
INI_KEY_DIRECTORY_NAME_TEST_RESOURCES = "resource-path.directory-name-test-resources"


def pytest_addoption(parser):
    """Adds options for pytest-resource-path."""
    parser.addini(
        INI_KEY_DIRECTORY_NAME_TESTS,
        "Directory name for tests",
        default=PathToResourceFactory.DIRECTORY_NAME_TESTS_DEAFAULT,
    )
    parser.addini(
        INI_KEY_DIRECTORY_NAME_TEST_RESOURCES,
        "Directory name for test resources",
        default=PathToResourceFactory.DIRECTORY_NAME_TEST_RESOURCES_DEFAULT,
    )


@pytest.fixture
def resource_path(request):
    """Fixture to get path to resource."""
    yield create_path_to_resource_factory(request).create(request.function)


@pytest.fixture
def resource_path_root(request):
    """Fixture to get path to resource root."""
    yield create_path_to_resource_factory(request).create_path_to_resource_root(request.function)


def create_path_to_resource_factory(request):
    """Creates PathToResourceFactory."""
    path_tests = Path(request.config.getini(INI_KEY_DIRECTORY_NAME_TESTS))
    path_test_resources = Path(request.config.getini(INI_KEY_DIRECTORY_NAME_TEST_RESOURCES))
    return PathToResourceFactory(path_tests, path_test_resources)
