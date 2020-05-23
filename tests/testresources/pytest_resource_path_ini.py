from pathlib import Path


def test_resource_path_ini(resource_path, request):
    assert (
        resource_path
        == Path(str(request.fspath)).parents[1] / "data/test_package/test_module_something/test_resource_path_ini"
    )


def test_resource_path_root_ini(resource_path_root, request):
    assert resource_path_root == Path(str(request.fspath)).parents[1] / "data"
