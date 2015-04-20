# -*- coding: utf-8 -*-
#
# Copyright (c) 2014-2015, Ghislain Antony Vaillant
# All rights reserved.
#
# This file is distributed under the BSD License, see the LICENSE file or
# checkout the license terms at http://opensource.org/licenses/BSD-2-Clause).

from __future__ import absolute_import, division, print_function

from .constants import acquisition_header_dtype
import h5py
import numpy


hdf5_acquisition_dtype = numpy.dtype([
    ('head', acquisition_header_dtype),
    ('traj', h5py.special_dtype(vlen=numpy.dtype('float32'))),
    ('data', h5py.special_dtype(vlen=numpy.dtype('float32')))
])


def as_hdf5_acquisition(array):
    h5array = numpy.empty((1,), dtype=hdf5_acquisition_dtype)
    h5array[0]['head'] = array['head']
    h5array[0]['data'] = array['data'].view(numpy.float32).ravel()
    h5array[0]['traj'] = array['traj'].view(numpy.float32).ravel()
    return h5array[0]