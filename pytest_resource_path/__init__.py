# -*- coding: utf-8 -*-
from pathlib import Path

import pytest

from pytest_resource_path.path_to_resource_factory import PathToResourceFactory

INI_KEY_DIRECTORY_NAME_TESTS = 'resource-path.directory-name-tests'
INI_KEY_DIRECTORY_NAME_TEST_RESOURCES = 'resource-path.directory-name-test-resources'


def pytest_addoption(parser):
    parser.addini(
        INI_KEY_DIRECTORY_NAME_TESTS,
        'Directory name for tests',
        default=PathToResourceFactory.DIRECTORY_NAME_TESTS_DEAFAULT
    )
    parser.addini(
        INI_KEY_DIRECTORY_NAME_TEST_RESOURCES,
        'Directory name for test resources',
        default=PathToResourceFactory.DIRECTORY_NAME_TEST_RESOURCES_DEFAULT
    )


@pytest.fixture
def resource_path(request):
    path_tests = Path(request.config.getini(INI_KEY_DIRECTORY_NAME_TESTS))
    path_test_resources = Path(request.config.getini(INI_KEY_DIRECTORY_NAME_TEST_RESOURCES))
    yield PathToResourceFactory(path_tests, path_test_resources).create(request.function)


@pytest.fixture
def resource_path_root(request):
    path_tests = Path(request.config.getini(INI_KEY_DIRECTORY_NAME_TESTS))
    path_test_resources = Path(request.config.getini(INI_KEY_DIRECTORY_NAME_TEST_RESOURCES))
    yield PathToResourceFactory(path_tests, path_test_resources).create_path_to_resource_root(request.function)
