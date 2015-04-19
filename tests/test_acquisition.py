# -*- coding: utf-8 -*-
#
# Copyright (c) 2014-2015, Ghislain Antony Vaillant
# All rights reserved.
#
# This file is distributed under the BSD License, see the LICENSE file or
# checkout the license terms at http://opensource.org/licenses/BSD-2-Clause).

from ismrmrdpy.backend import constants
from ismrmrdpy.backend import acquisition
import pytest
import numpy


def test_encoding_counter_bytesize():
    assert(constants.acquisition_header_dtype['idx'].itemsize == 34)


def test_header_bytesize():
    assert(constants.acquisition_header_dtype.itemsize == 340)


@pytest.mark.parametrize("parameters", [
    None,  # default version, rest of metadata is 0 
    {'version': 99},  # override default version
    {'number_of_samples': 256, 'active_channels': 8},  # override metadata
])
def test_header_creation(parameters):
    if parameters is not None:
        header = acquisition.make_header(**parameters)
        for key, val in parameters.items():
            assert(header[key] == val)
    else:
        header = acquisition.make_header()
        assert(header['version'] == constants.Constants.version)
        assert(header['number_of_samples'] == 0)
        assert(header['active_channels'] == 0)


def test_dtype_creation():
    header = acquisition.make_header(number_of_samples=256,
                                     active_channels=8,
                                     trajectory_dimensions=2)
    dtype = acquisition.make_dtype(header)
    assert(dtype['head'] == header.dtype)
    assert(dtype['traj'].shape == (header['number_of_samples'],
                                   header['trajectory_dimensions']))
    assert(dtype['traj'].base == numpy.float32)
    assert(dtype['data'].shape == (header['active_channels'],
                                   header['number_of_samples']))
    assert(dtype['data'].base == numpy.complex64)


def test_object_creation():
    header = acquisition.make_header(number_of_samples=256,
                                     active_channels=8,
                                     trajectory_dimensions=2)
    array = acquisition.make_object(header)
    assert(array['head'] == header)
    assert(not numpy.any(array['traj']))  # trajectory should only contain zeros
    assert(not numpy.any(array['data']))  # data should only contain zeros