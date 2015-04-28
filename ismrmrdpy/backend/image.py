# -*- coding: utf-8 -*-
#
# Copyright (c) 2014-2015, Ghislain Antony Vaillant
# All rights reserved.
#
# This file is distributed under the BSD License, see the LICENSE file or
# checkout the license terms at http://opensource.org/licenses/BSD-2-Clause).

from __future__ import absolute_import, division, print_function


from .constants import Constants, ImageFlags
from .constants import image_header_dtype, ismrmrd_to_numpy_dtypes
from .bitmask import BitmaskWrapper
import numpy


header_dtype = image_header_dtype

def make_header(version=Constants.version, *args, **kwargs):
    header = numpy.zeros((), dtype=header_dtype)
    header['version'] = version
    for key in kwargs:
        if key in header_dtype.fields:
            header[key] = kwargs[key]
    return header 

def deserialize_header(bytestring):
    return numpy.fromstring(bytestring, dtype=header_dtype)[0]

def make_dtype(header):
    data_dtype = numpy.dtype(
        (ismrmrd_to_numpy_dtypes[header['data_type']],
        (header['channels'],) + list(header['matrix_size'][::-1]))
    )
    attrib_dtype = numpy.dtype(
        (numpy.str, header['attribute_string_len'])
    )
    return numpy.dtype([
        ('head', header_dtype),
        ('attribute_string', attrib_dtype),
        ('data', data_dtype),
    ])

def make_object(head=None, attribute_string=None, data=None, *args, **kwargs):
    head = head or make_header(*args, **kwargs)
    dtype = make_dtype(head)
    if attribute_string is not None:
        attribute_string = numpy.asarray(attribute_string,
                                         dtype=dtype['attribute_string'])
    if data is not None:
        data = numpy.asarray(data, dtype=dtype['data'].base).reshape(dtype['data'].shape)
    return numpy.array([head, attribute_string, data], dtype=dtype)

def deserialize_object(bytestring):
    header = deserialize_header(bytestring[:header_dtype.itemsize])
    return numpy.fromstring(bytestring, dtype=make_dtype(header))[0]

def set_flags(header, flags=None):
    bitmask = BitmaskWrapper(header['flags'])
    if flags is not None:
        _verify_flags(flags)
        bitmask.set([flag-1 for flag in flags])
    else:
        bitmask.set()

def clear_flags(header, flags=None):
    bitmask = BitmaskWrapper(header['flags'])    
    if flags is not None:
        _verify_flags(flags)
        bitmask.clear([flag-1 for flag in flags])
    else:
        bitmask.clear()

def is_flag_set(header, flag):
    bitmask = BitmaskWrapper(header['flags'])
    _verify_flags([flag,])
    return bitmask.is_set(flag-1)

def _verify_flags(flags):
    for flag in flags:
        if flag not in ImageFlags:
            raise ValueError("Invalid flag provided: {}.".format(flag))