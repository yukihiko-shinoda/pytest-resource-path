

class TestInit:
    """Tests for File."""

    @staticmethod
    def test_fixture(testdir_structure_for_testing_resource_path):
        """Make sure that pytest accepts our fixture."""

        # run pytest
        result = testdir_structure_for_testing_resource_path.runpytest("-v")

        # fnmatch_lines does an assertion internally
        lines = [
            "*::test_resource_path PASSED*",
            "*::test_resource_path_root PASSED*",
        ]
        result.stdout.fnmatch_lines(lines)

        # make sure that that we get a '0' exit code for the testsuite
        assert result.ret == 0

    @staticmethod
    def test_fixture_with_ini(testdir_structure_for_testing_ini):
        testdir_structure_for_testing_ini.makeini(
            """
            [pytest]
            resource-path.directory-name-tests = integrationtests
            resource-path.directory-name-test-resources = data
        """
        )

        # run pytest
        result = testdir_structure_for_testing_ini.runpytest("-v")

        # fnmatch_lines does an assertion internally
        lines = [
            "*::test_resource_path_ini PASSED*",
            "*::test_resource_path_root_ini PASSED*",
        ]
        result.stdout.fnmatch_lines(lines)

        # make sure that that we get a '0' exit code for the testsuite
        assert result.ret == 0
