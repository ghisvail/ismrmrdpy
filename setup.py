#!/usr/bin/python
# coding: utf8

# Copyright (c) 2014-2015, Ghislain Antony Vaillant
# All rights reserved.
#
# This file is distributed under the BSD License, see the LICENSE file or
# checkout the license terms at http://opensource.org/licenses/BSD-2-Clause).

from __future__ import absolute_import, division, print_function

from setuptools import setup, find_packages, Command
from setuptools.command.build_py import build_py as BuildPyCommand
from setuptools.command.test import test as TestCommand
from distutils import log

import os
import sys
import subprocess


class IsmrmrdpyBuildSchemaCommand(Command):
    """Custom build command generating the schema bindings."""
    
    description = 'Run pyxbgen on the ISMRMRD schema'
    user_options = [
        # The format is (long option, short option, description).
        ('schema-location=', 'u', 'Location of an entrypoint schema'),
        ('module=', 'm', 'Module name corresponding to an entrypoint schema'),
        ('binding-root=', None, 'Path where the bindings will be written'),
    ]

    def initialize_options(self):
        """Set default values for options."""
        # Each user option must be listed here with their default value.
        self.schema_location = 'schema/ismrmrd.xsd'
        self.module = 'schema'
        self.binding_root = 'ismrmrdpy/backend'
    
    def finalize_options(self):
        """Post-process options."""
        if self.schema_location is not None:
            assert os.path.exists(self.schema_location), (
                'schema file {} does not exist'.format(self.schema_location))
    
    def run(self):
        """Run command."""
        if sys.version_info[0] < 3:
            command = ['pyxbgen']
        else:
            command = ['pyxbgen-py3']
        command.append('--schema-location={}'.format(self.schema_location))
        command.append('--module={}'.format(self.module))
        command.append('--binding-root={}'.format(self.binding_root))        
        self.announce(
            'Running command: {}'.format(command),
            level=log.INFO,
        )
        subprocess.check_call(command)


class IsmrmrdpyBuildPyCommand(BuildPyCommand):
  """Custom build command."""

  def run(self):
    self.run_command('build_schema')
    BuildPyCommand.run(self)


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
        'enum34',
        'bitarray',
        'h5py >= 2.3',
        'numpy',
        'pyxb >= 1.2.4',
    ],
    setup_requires=['pyxb>=1.2.4'],
    tests_require=['pytest'],
    cmdclass = {
        'build_py': IsmrmrdpyBuildPyCommand,
        'build_schema': IsmrmrdpyBuildSchemaCommand,
        'test': IsmrmrdpyTestCommand,
    },
)
