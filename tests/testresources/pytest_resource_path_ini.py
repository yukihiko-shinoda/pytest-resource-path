"""Implements test for pytest-resource-path Fixtures with pytest.ini."""
from pathlib import Path

import pytest


def test_resource_path_ini(resource_path, request):
    """Fixture resource_path should be following absolute path."""
    assert resource_path == Path(str(request.fspath)).parents[1] / Path(
        "data/test_package/test_module_something/test_resource_path_ini"
    )


def test_resource_path_root_ini(resource_path_root, request):
    """Fixture resource_path_root should be following absolute path."""
    assert resource_path_root == Path(str(request.fspath)).parents[1] / Path("data")


@pytest.fixture(scope="package")
def resource_path_root_scope_package_ini(resource_path_root):
    yield resource_path_root


# Reason: To define fixture in same module. pylint: disable=redefined-outer-name
def test_resource_path_root_scope_package_ini(resource_path_root_scope_package_ini, request):
    assert resource_path_root_scope_package_ini == Path(str(request.fspath)).parents[1] / Path("data")
