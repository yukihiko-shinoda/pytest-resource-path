"""Implements test for pytest-resource-path Fixtures with pytest.ini."""
from pathlib import Path


def test_resource_path_ini(resource_path, request):
    """Fixture resource_path should be following absolute path."""
    assert (
        resource_path
        == Path(str(request.fspath)).parents[1] / "data/test_package/test_module_something/test_resource_path_ini"
    )


def test_resource_path_root_ini(resource_path_root, request):
    """Fixture resource_path_root should be following absolute path."""
    assert resource_path_root == Path(str(request.fspath)).parents[1] / "data"
