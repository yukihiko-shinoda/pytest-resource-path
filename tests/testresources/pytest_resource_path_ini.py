"""Implements test for pytest-resource-path Fixtures with pytest.ini."""

from pathlib import Path

import pytest

from tests.testlibraries.pytest_backward_compatibility import get_path


def test_resource_path_ini(resource_path: Path, request: pytest.FixtureRequest) -> None:
    """Fixture resource_path should be following absolute path."""
    assert resource_path == get_path(request).parents[1] / Path(
        "data/test_package/test_module_something/test_resource_path_ini",
    )


def test_resource_path_root_ini(resource_path_root: Path, request: pytest.FixtureRequest) -> None:
    """Fixture resource_path_root should be following absolute path."""
    assert resource_path_root == get_path(request).parents[1] / Path("data")


@pytest.fixture(scope="package")
def resource_path_root_scope_package_ini(resource_path_root: Path) -> Path:
    return resource_path_root


# Reason: To define fixture in same module. pylint: disable=redefined-outer-name
def test_resource_path_root_scope_package_ini(
    resource_path_root_scope_package_ini: Path,
    request: pytest.FixtureRequest,
) -> None:
    assert resource_path_root_scope_package_ini == get_path(request).parents[1] / Path("data")
