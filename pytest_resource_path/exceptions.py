"""This module implements exceptions for this package."""

__author__ = "Yukihiko Shinoda"
__copyright__ = "Copyright (c) 2020 Yukihiko Shinoda"
__license__ = "MIT"

__all__ = ["Error", "LogicError"]


class Error(Exception):
    """Base class for exceptions in this module.

    @see https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions
    """


class LogicError(Error):
    """This Error indicates programing miss."""
