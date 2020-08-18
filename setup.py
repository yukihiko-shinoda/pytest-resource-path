#!/usr/bin/env python
"""Implements setup configuration."""
import io
import os

from setuptools import find_packages, setup  # type: ignore


def read(fname):
    """Reads file content."""
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return io.open(file_path, encoding="utf-8").read()


setup(
    author="Yukihiko Shinoda",
    author_email="yuk.hik.future@gmail.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Testing",
        "Topic :: System :: Filesystems",
        "Typing :: Typed",
    ],
    dependency_links=[],
    description="Provides path for uniform access to test resources in isolated directory",
    entry_points={"pytest11": ["resource-path = pytest_resource_path"]},
    exclude_package_data={"": ["__pycache__", "*.py[co]", ".pytest_cache"]},
    include_package_data=True,
    install_requires=["colorama", "pytest>=3.5.0"],
    keywords="pytest test fixture resource path pathlib",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    maintainer="Yukihiko Shinoda",
    maintainer_email="yuk.hik.future@gmail.com",
    name="pytest-resource-path",
    packages=find_packages(include=["pytest_resource_path", "pytest_resource_path.*", "tests", "tests.*"]),
    package_data={"pytest_resource_path": ["py.typed"], "tests": ["*"]},
    python_requires=">=3.5",
    test_suite="tests",
    tests_require=["pytest>=3"],
    url="https://github.com/yukihiko-shinoda/pytest-resource-path",
    version="1.2.1",
    zip_safe=False,
)
