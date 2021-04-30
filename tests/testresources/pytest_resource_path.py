"""Implements test for pytest-resource-path Fixtures."""
from pathlib import Path

import pytest


def test_resource_path(resource_path, request):
    """Fixture resource_path should be following absolute path."""
    assert resource_path == Path(str(request.fspath)).parents[1] / Path(
        "testresources/test_package/test_module_something/test_resource_path"
    )


def test_resource_path_root(resource_path_root, request):
    """Fixture resource_path_root should be following absolute path."""
    assert resource_path_root == Path(str(request.fspath)).parents[1] / Path("testresources")


@pytest.fixture(scope="package")
def resource_path_root_scope_package(resource_path_root):
    yield resource_path_root


# Reason: To define fixture in same module. pylint: disable=redefined-outer-name
def test_resource_path_root_scope_package(resource_path_root_scope_package, request):
    assert resource_path_root_scope_package == Path(str(request.fspath)).parents[1] / Path("testresources")
