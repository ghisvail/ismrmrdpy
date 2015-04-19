# -*- coding: utf-8 -*-
#
# Copyright (c) 2014-2015, Ghislain Antony Vaillant
# All rights reserved.
#
# This file is distributed under the BSD License, see the LICENSE file or
# checkout the license terms at http://opensource.org/licenses/BSD-2-Clause).

from __future__ import absolute_import, division, print_function

from .constants import Constants, AcquisitionFlags, DataTypes
from .constants import acquisition_header_dtype, ismrmrd_to_numpy_dtypes
import numpy


def make_header(version=Constants.version, *args, **kwargs):
    header = numpy.zeros((), dtype=acquisition_header_dtype)
    header['version'] = version
    for key in kwargs:
        if key in acquisition_header_dtype.fields:
            header[key] = kwargs[key]
    return header    

def make_dtype(header):
    data_dtype = ismrmrd_to_numpy_dtypes[DataTypes.cxfloat]
    data_shape = (header['active_channels'],
                  header['number_of_samples'])
    traj_dtype = ismrmrd_to_numpy_dtypes[DataTypes.float]
    traj_shape = (header['number_of_samples'],
                  header['trajectory_dimensions'])
    return numpy.dtype([
        ('head',    acquisition_header_dtype),
        ('traj',    (traj_dtype, traj_shape)),
        ('data',    (data_dtype, data_shape)),
    ])

def make_array(header=None, *args, **kwargs):
    header = header or make_header(**kwargs)
    trajectory = None
    data = None
    dtype = make_dtype(header)
    array = numpy.zeros((), dtype=dtype)
    array['head'] = header
    if trajectory is not None:
        array['traj'] = trajectory
    if data is not None:
        array['data'] = data

def frombytes(bytestring):
    pass

def set_flags(header, flags=None):
    pass

def clear_flags(header, flags=None):
    pass

def is_flag_set(header, flag):
    pass

def _verify_flags(flags):
    pass

def set_channels(header, channels=None):
    pass

def clear_channels(header, channels=None):
    pass

def is_channel_set(header, channel):
    pass

def _verify_channels(flags):
    pass    