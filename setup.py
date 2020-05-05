#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import os
from setuptools import setup, find_packages


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return io.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-resource-path',
    version='0.1.0',
    author='Yukihiko Shinoda',
    author_email='yuk.hik.future@gmail.com',
    maintainer='Yukihiko Shinoda',
    maintainer_email='yuk.hik.future@gmail.com',
    license='MIT',
    url='https://github.com/yukihiko-shinoda/pytest-resource-path',
    description='Provides path for uniform access to test resources in isolated directory',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=("tests*",)),
    package_data={"pytest_resource_path": ["py.typed"]},
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=['pytest>=3.5.0'],
    dependency_links=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Topic :: System :: Filesystems',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Typing :: Typed',
    ],
    entry_points={
        'pytest11': [
            'resource-path = pytest_resource_path',
        ],
    },
)
