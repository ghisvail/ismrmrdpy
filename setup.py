#!/usr/bin/python
# coding: utf8

# Copyright (c) 2014-2015, Ghislain Antony Vaillant
# All rights reserved.
#
# This file is distributed under the BSD License, see the LICENSE file or
# checkout the license terms at http://opensource.org/licenses/BSD-2-Clause).

from __future__ import absolute_import, division, print_function

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys


class IsmrmrdpyTestCommand(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name="ismrmrdpy",
    version="0.1",
    description="Pure Python implementation of ISMRMRD",
    license="BSD",
    url="https://github.com/ghisvail/ismrmrdpy",
    author="Ghislain Antony Vaillant",
    author_email="ghisvail@gmail.com",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        ],
    packages=find_packages(exclude=['tests',]),
    install_requires=[
        'numpy',
        'h5py>=2.3',
        'bitarray'
    ],
    tests_require=['pytest'],
    cmdclass = {'test': IsmrmrdpyTestCommand},
)
