# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is `pytest-resource-path`, a pytest plugin that provides fixtures for uniform access to test resources in isolated directories. It's a Python package distributed on PyPI.

## Development Commands

### Testing
```bash
# Run all tests
pytest

# Run specific test
pytest tests/test_specific_module.py

# Run with coverage
python -m pytest --cov=pytest_resource_path --cov-report=html
```

### Code Quality and Linting
The project uses `invokelint` for task management. Available commands via `invoke`:
```bash
# Run all linting and style checks
invoke lint.lint

# Run style formatting
invoke style.style

# Clean build artifacts
invoke clean.clean

# Build distribution
invoke dist.dist
```

Individual linting tools configured in pyproject.toml:
- `ruff` - Primary linter with extensive rule set
- `flake8` - Additional linting with custom configuration
- `mypy` - Type checking with strict mode
- `pylint` - Additional code quality checks
- `bandit` - Security analysis

### Build and Distribution
```bash
# Build package
python -m build

# Version management with bump-my-version
bump-my-version bump patch  # or minor, major
```

## Code Architecture

### Core Components

**Main Plugin Module** (`pytest_resource_path/pytest_resource_path.py`):
- Defines pytest fixtures: `resource_path` and `resource_path_root`
- Handles pytest configuration options for customizing directory names
- Factory pattern for creating path resolvers

**Path Resolution System**:
- `PathToResourceFactory` - Main factory for creating resource paths
- `AbsolutePathFactory` - Handles absolute path resolution
- `PathFactory` - Base path manipulation utilities

**Directory Structure Convention**:
- Default test directory: `tests/`
- Default test resources directory: `testresources/`
- Path mapping: `tests/package/module.py` → `testresources/package/module/test_method/`

### Key Design Patterns

1. **Factory Pattern**: Used throughout for path creation and resolution
2. **Plugin Architecture**: Integrates with pytest via entry points
3. **Configuration-driven**: Directory names customizable via `pytest.ini`

### Fixtures Provided

- `resource_path`: Returns absolute Path to test-specific resource directory
- `resource_path_root`: Returns absolute Path to the testresources root directory

## Configuration

Directory names can be customized in `pytest.ini`:
```ini
[pytest]
resource-path.directory-name-tests = integrationtests
resource-path.directory-name-test-resources = data
```

## Code Style

- Line length: 119 characters (Black/Ruff compatible)
- Type hints: Required (mypy strict mode)
- Docstring style: Google convention
- Import style: Force single-line imports (isort)
- Security: Bandit scanning enabled (excludes test assertions)