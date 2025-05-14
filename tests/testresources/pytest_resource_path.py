"""Implements test for pytest-resource-path Fixtures."""

from pathlib import Path

import pytest

from tests.testlibraries.pytest_backward_compatibility import get_path


def test_resource_path(resource_path: Path, request: pytest.FixtureRequest) -> None:
    """Fixture resource_path should be following absolute path."""
    assert resource_path == get_path(request).parents[1] / Path(
        "testresources/test_package/test_module_something/test_resource_path",
    )


def test_resource_path_root(resource_path_root: Path, request: pytest.FixtureRequest) -> None:
    """Fixture resource_path_root should be following absolute path."""
    assert resource_path_root == get_path(request).parents[1] / Path("testresources")


@pytest.fixture(scope="package")
def resource_path_root_scope_package(resource_path_root: Path) -> Path:
    return resource_path_root


# Reason: To define fixture in same module. pylint: disable=redefined-outer-name
def test_resource_path_root_scope_package(
    resource_path_root_scope_package: Path,
    request: pytest.FixtureRequest,
) -> None:
    assert resource_path_root_scope_package == get_path(request).parents[1] / Path("testresources")
