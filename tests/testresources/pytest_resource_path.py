from pathlib import Path


def test_resource_path(resource_path, request):
    assert resource_path == Path(request.fspath).parents[1] / Path(
        'testresources/test_package/test_module_something/test_resource_path'
    )
