"""Implements fixtures to get path to resource."""
from pytest_resource_path.absolute_path_factory import *  # noqa
from pytest_resource_path.exceptions import *  # noqa
from pytest_resource_path.path_factory import *  # noqa
from pytest_resource_path.path_to_resource_factory import *  # noqa
from pytest_resource_path.pytest_resource_path import *  # noqa

__version__ = "1.2.1"

__all__ = []
# pylint: disable=undefined-variable
__all__ += absolute_path_factory.__all__  # type: ignore # noqa
__all__ += exceptions.__all__  # type: ignore # noqa
__all__ += path_factory.__all__  # type: ignore # noqa
__all__ += path_to_resource_factory.__all__  # type: ignore # noqa
__all__ += pytest_resource_path.__all__  # type: ignore # noqa
