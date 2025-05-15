"""Test for pytest."""

from pathlib import Path

import pytest

from pytest_resource_path.path_to_resource_factory import PathToResourceFactory
from pytest_resource_path.pytest_backward_compatibility import get_path

__all__ = [
    "INI_KEY_DIRECTORY_NAME_TESTS",
    "INI_KEY_DIRECTORY_NAME_TEST_RESOURCES",
    "create_path_to_resource_factory",
    "pytest_addoption",
    "resource_path",
    "resource_path_root",
]

INI_KEY_DIRECTORY_NAME_TESTS = "resource-path.directory-name-tests"
INI_KEY_DIRECTORY_NAME_TEST_RESOURCES = "resource-path.directory-name-test-resources"


def pytest_addoption(parser: pytest.Parser) -> None:
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
def resource_path(request: pytest.FixtureRequest) -> Path:
    """Fixture to get path to resource."""
    return create_path_to_resource_factory(request).create(request.function)


@pytest.fixture(scope="package")
def resource_path_root(request: pytest.FixtureRequest) -> Path:
    """Fixture to get path to resource root."""
    return create_path_to_resource_factory(request).create_path_to_resource_root(get_path(request)).resolve()


def create_path_to_resource_factory(request: pytest.FixtureRequest) -> PathToResourceFactory:
    """Creates PathToResourceFactory."""
    path_tests = Path(request.config.getini(INI_KEY_DIRECTORY_NAME_TESTS))
    path_test_resources = Path(request.config.getini(INI_KEY_DIRECTORY_NAME_TEST_RESOURCES))
    return PathToResourceFactory(path_tests, path_test_resources)
