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

from .constants import *
import numpy

__all__ = ('ismrmrd_libver', 'encoding_counters_dtype', 
           'acquisition_header_dtype', 'image_header_dtype',
           'make_acquisition_dtype', 'make_image_dtype')


ismrmrd_libver = ISMRMRD_VERSION

encoding_counters_dtype = numpy.dtype([
    ('kspace_encode_step_1',        '<u2'),
    ('kspace_encode_step_2',        '<u2'),
    ('average',                     '<u2'),
    ('slice',                       '<u2'),
    ('contrast',                    '<u2'),
    ('phase',                       '<u2'),
    ('repetition',                  '<u2'),
    ('set',                         '<u2'),
    ('segment',                     '<u2'),
    ('user',                        ('<u2', (ISMRMRD_USER_INTS,))),
])

acquisition_header_dtype = numpy.dtype([
    ('version',                     '<u2'),
    ('flags',                       '<u8'),
    ('measurement_uid',             '<u4'),
    ('scan_counter',                '<u4'),
    ('acquisition_time_stamp',      '<u4'),
    ('physiology_time_stamp',       ('<u4', (ISMRMRD_PHYS_STAMPS))),
    ('number_of_samples',           '<u2'),
    ('available_channels',          '<u2'),
    ('active_channels',             '<u2'),
    ('channel_mask',                ('<u8', (ISMRMRD_CHANNEL_MASKS,))),
    ('discard_pre',                 '<u2'),
    ('discard_post',                '<u2'),
    ('center_sample',               '<u2'),
    ('encoding_space_ref',          '<u2'),
    ('trajectory_dimensions',       '<u2'),
    ('sample_time_us',              '<f4'),
    ('position',                    ('<f4', (ISMRMRD_POSITION_LENGTH,))),
    ('read_dir',                    ('<f4', (ISMRMRD_DIRECTION_LENGTH,))),
    ('phase_dir',                   ('<f4', (ISMRMRD_DIRECTION_LENGTH,))),
    ('slice_dir',                   ('<f4', (ISMRMRD_DIRECTION_LENGTH,))),
    ('patient_table_position',      ('<f4', (ISMRMRD_POSITION_LENGTH,))),
    ('idx',                         encoding_counters_dtype),
    ('user_int',                    ('<u4', (ISMRMRD_USER_INTS,))),
    ('user_float',                  ('<f4', (ISMRMRD_USER_FLOATS,))),
])

image_header_dtype = numpy.dtype([
    ('version',                     '<u2'),
    ('data_type',                   '<u2'),
    ('flags',                       '<u8'),
    ('measurement_uid',             '<u4'),
    ('matrix_size',                 ('<u2', (3,))),
    ('field_of_view',               ('<f4', (3,))),
    ('channels',                    '<u2'),
    ('position',                    ('<f4', (ISMRMRD_POSITION_LENGTH,))),
    ('read_dir',                    ('<f4', (ISMRMRD_DIRECTION_LENGTH,))),
    ('phase_dir',                   ('<f4', (ISMRMRD_DIRECTION_LENGTH,))),
    ('slice_dir',                   ('<f4', (ISMRMRD_DIRECTION_LENGTH,))),
    ('patient_table_position',      ('<f4', (ISMRMRD_POSITION_LENGTH,))),
    ('average',                     '<u2'),
    ('slice',                       '<u2'),
    ('contrast',                    '<u2'),
    ('phase',                       '<u2'),
    ('repetition',                  '<u2'),
    ('set',                         '<u2'),
    ('acquisition_time_stamp',      '<u4'),
    ('physiology_time_stamp',       ('<u4', (ISMRMRD_PHYS_STAMPS))),
    ('image_type',                  '<u2'),
    ('image_index',                 '<u2'),
    ('image_series_index',          '<u2'),
    ('user_int',                    ('<u4', (ISMRMRD_USER_INTS,))),
    ('user_float',                  ('<f4', (ISMRMRD_USER_FLOATS,))),
    ('attribute_string_len',        '<u4'),
])

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