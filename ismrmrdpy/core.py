# Copyright (c) 2014-2015 Ghislain Antony Vaillant.
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

from .declarations import *
import numpy

__all__ = ('ismrmrd_libver', 'acquisition_header_dtype',
           'make_acquisition_dtype', 'image_header_dtype',
           'make_image_dtype')

ismrmrd_libver = ISMRMRD_VERSION

_ismrmrd_typenums_to_numpy_dtypes = {
    ISMRMRD_USHORT   : numpy.uint16,
    ISMRMRD_SHORT    : numpy.int16,
    ISMRMRD_UINT     : numpy.uint32,
    ISMRMRD_INT      : numpy.int32,
    ISMRMRD_FLOAT    : numpy.float32,
    ISMRMRD_DOUBLE   : numpy.float64,
    ISMRMRD_CXFLOAT  : numpy.complex64,
    ISMRMRD_CXDOUBLE : numpy.complex128,
    }

def make_acquisition_dtype(header):
    data_dtype = _ismrmrd_typenums_to_numpy_dtypes[ISMRMRD_CXFLOAT]
    data_shape = (header['active_channels'],
                  header['number_of_samples'])
    traj_dtype = _ismrmrd_typenums_to_numpy_dtypes[ISMRMRD_FLOAT]
    traj_shape = (header['number_of_samples'],
                  header['trajectory_dimensions'])
    return numpy.dtype([
        ('head',    acquisition_header_dtype),
        ('traj',    (traj_dtype, traj_shape)),
        ('data',    (data_dtype, data_shape)),
    ])

def make_image_dtype(header):
    data_dtype = _ismrmrd_typenums_to_numpy_dtypes[header['data_type']]
    data_shape = (list(header['matrix_size']) + [header['channels']])[::-1]
    attr_dtype = numpy.dtype((numpy.str, header['attribute_string_len']))
    return numpy.dtype([
        ('head',                image_header_dtype),
        ('attribute_string',    attr_dtype),
        ('data',                (data_dtype, data_shape))
    ])