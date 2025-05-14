"""The backward compatibility for pytest."""

from pathlib import Path

import pytest


def get_path(request: pytest.FixtureRequest) -> Path:
    """Get path to resource directory of argument method."""
    try:
        return request.path
    except AttributeError:
        # To support pytest < 7.0.0
        return Path(str(request.fspath))  # type: ignore[attr-defined]
