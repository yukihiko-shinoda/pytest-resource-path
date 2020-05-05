# pytest-resource-path

[![See Build Status on Travis CI](https://travis-ci.org/yukihiko-shinoda/pytest-resource-path.svg?branch=master)](https://travis-ci.org/yukihiko-shinoda/pytest-resource-path)
[![See Build Status on AppVeyor](https://ci.appveyor.com/api/projects/status/github/yukihiko-shinoda/pytest-resource-path?branch=master)](https://ci.appveyor.com/project/yukihiko-shinoda/pytest-resource-path/branch/master)
[![codecov](https://codecov.io/gh/yukihiko-shinoda/pytest-resource-path/branch/master/graph/badge.svg)](https://codecov.io/gh/yukihiko-shinoda/pytest-resource-path)
[![Python versions](https://img.shields.io/pypi/pyversions/pytest-resource-path.svg)](https://pypi.org/project/pytest-resource-path)
[![Twitter URL](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2Fyukihiko-shinoda%2Fpytest-resource-path)](http://twitter.com/share?text=pytest-resource-path&url=https://pypi.org/project/pytest-resource-path/&hashtags=python)

Provides path for uniform access to test resources in isolated directory

This [pytest] plugin was generated with [Cookiecutter] along with [@hackebrot]'s [cookiecutter-pytest-plugin] template.

## Features

Let's isolate test resources from test code.

The test which use test resource is not so many.
If we place test resource with test code, these resources will fill the display area of explorer. Wouldn't it be more productive if the files or directories which is not related with almost tests wasn't usually displayed?

**pytest-resource-path** provides path for uniform access to test resources in isolated directory.

This pytest plugin assumes that test resource is placed under `testresources` directory directly under `tests`. (Don't worry, you can customize these directory names by `pytest.ini`)

```bash
tests/
+-- some_test_package/
|   +-- some_test_module.py
+-- testresources/
    +-- some_test_package/
        +-- some_test_module/
```

## Installation

You can install "pytest-resource-path" via [pip] from [PyPI]:

```console
pip install pytest-resource-path
```

## Usage

### Basic

You can use fixture `resource_path` which is pathlib.Path instance (**absolte path**).

```python
def test_method(resource_path):
    text_test_resource = (resource_path / 'test_resource.txt').get_text()
```

When assume that above `test_method` is in `tests/some_tests_package_some_test_module.py`, you have to place `test_resource.txt` following directory:

```bash
tests/
+-- some_test_package/
|   +-- some_test_module.py
+-- testresources/
    +-- some_test_package/
        +-- some_test_module/
            +-- test_method/
                +-- test_resource.txt
```

If you want to omit directory per method, you can do:

```python
def test_method(resource_path):
    text_test_resource = Path(f'{resource_path}.txt').get_text()
```

Note that the class name is not used in the path since It felt redundant in design.

### How to customize directory names

To traverse directory structure, this plugin requires to fix directory names.
By default, 
root directory of test requires to be named `tests`,
root directory of test resources requires to be named `testresources`.
You can customize these directory names by `pytest.ini`

Ex:

```ini
[pytest]
resource-path.directory-name-tests = integrationtests
resource-path.directory-name-test-resources = data
```

Above customize fits following directory strucure:

```bash
integrationtests/
+-- some_test_package/
|   +-- some_test_module.py
+-- data/
    +-- some_test_package/
        +-- some_test_module/
```

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [MIT] license, "pytest-resource-path" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@hackebrot]: https://github.com/hackebrot
[MIT]: http://opensource.org/licenses/MIT
[cookiecutter-pytest-plugin]: https://github.com/pytest-dev/cookiecutter-pytest-plugin
[file an issue]: https://github.com/yukihiko-shinoda/pytest-resource-path/issues
[pytest]: https://github.com/pytest-dev/pytest
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/project
