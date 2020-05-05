from pathlib import Path


def test_resource_path_ini(resource_path, request):
    assert resource_path == Path(
        request.fspath).parents[1] / 'data/test_package/test_module_something/test_resource_path_ini'
