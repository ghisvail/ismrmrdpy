#!/usr/bin/python
# coding: utf8

# Copyright (c) 2014-2015, Ghislain Antony Vaillant
# All rights reserved.
#
# This file is distributed under the BSD License, see the LICENSE file or
# checkout the license terms at http://opensource.org/licenses/BSD-2-Clause).

from __future__ import absolute_import, division, print_function

from setuptools import setup, find_packages


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
)