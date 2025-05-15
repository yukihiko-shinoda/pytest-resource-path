"""Tests for __init__.py."""

import pytest


class TestInit:
    """Tests for __init__.py."""

    @staticmethod
    def test_fixture(testdir_structure_for_testing_resource_path: pytest.Testdir) -> None:
        """Fixture should be expected path."""

        # run pytest
        result = testdir_structure_for_testing_resource_path.runpytest("-v")

        # fnmatch_lines does an assertion internally
        lines = [
            "*::test_resource_path PASSED*",
            "*::test_resource_path_root PASSED*",
            "*::test_resource_path_root_scope_package PASSED*",
        ]
        result.stdout.fnmatch_lines(lines)

        # make sure that that we get a '0' exit code for the testsuite
        assert result.ret == 0

    @staticmethod
    def test_fixture_with_ini(testdir_structure_for_testing_ini: pytest.Testdir) -> None:
        """Fixture should be expected path with pytest.ini."""
        testdir_structure_for_testing_ini.makeini(
            """
            [pytest]
            resource-path.directory-name-tests = integrationtests
            resource-path.directory-name-test-resources = data
        """,
        )

        # run pytest
        result = testdir_structure_for_testing_ini.runpytest("-v")

        # fnmatch_lines does an assertion internally
        lines = [
            "*::test_resource_path_ini PASSED*",
            "*::test_resource_path_root_ini PASSED*",
            "*::test_resource_path_root_scope_package_ini PASSED*",
        ]
        result.stdout.fnmatch_lines(lines)

        # make sure that that we get a '0' exit code for the testsuite
        assert result.ret == 0
