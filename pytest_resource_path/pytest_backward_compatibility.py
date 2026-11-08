"""The backward compatibility for pytest."""

__author__ = "Yukihiko Shinoda"
__copyright__ = "Copyright (c) 2025 Yukihiko Shinoda"
__license__ = "MIT"

from pathlib import Path

import pytest


def get_path(request: pytest.FixtureRequest) -> Path:
    """Get path to resource directory of argument method."""
    try:
        return request.path
    # Reason: Since it requires to use pytest < 7.0.0 to test following code
    except AttributeError:  # pragma: no cover
        # To support pytest < 7.0.0
        return Path(str(request.fspath))  # type: ignore[attr-defined]
