# -*- coding: utf-8 -*-
#
# Copyright (c) 2014-2015, Ghislain Antony Vaillant
# All rights reserved.
#
# This file is distributed under the BSD License, see the LICENSE file or
# checkout the license terms at http://opensource.org/licenses/BSD-2-Clause).

from __future__ import absolute_import, division, print_function

# TODO: autogeneration
# In the future, this file should be autogenerated by parsing a 
# system-installed or vendorized ismrmrd header file.

import enum
import numpy

# from ISMRMRD_Constants
class Constants(enum.IntEnum):
    version = 1
    user_ints = 8
    user_floats = 8
    phys_stamps = 3
    channel_masks = 16
    ndarray_maxdim = 7
    position_length = 3
    direction_length = 3

# from ISMRMRD_DataTypes
class DataTypes(enum.IntEnum):
    ushort = 1
    short = 2
    uint = 3
    int = 4
    float = 5
    double = 6
    cxfloat = 7
    cxdouble = 8

# from ISMRMRD_AcquisitionFlags
class AcquisitionFlags(enum.IntEnum):
    acq_first_in_encode_step1 = 1
    acq_last_in_encode_step1 = 2
    acq_first_in_encode_step2 = 3
    acq_last_in_encode_step2 = 4
    acq_first_in_average = 5
    acq_last_in_average = 6
    acq_first_in_slice = 7
    acq_last_in_slice = 8
    acq_first_in_contrast =  9
    acq_last_in_contrast = 10
    acq_first_in_phase = 11
    acq_last_in_phase = 12
    acq_first_in_repetition = 13
    acq_last_in_repetition = 14
    acq_first_in_set = 15
    acq_last_in_set = 16
    acq_first_in_segment = 17
    acq_last_in_segment = 18
    acq_is_noise_measurement = 19
    acq_is_parallel_calibration = 20
    acq_is_parallel_calibration_and_imaging = 21
    acq_is_reverse = 22
    acq_is_navigation_data = 23
    acq_is_phasecorr_data = 24
    acq_last_in_measurement = 25
    acq_is_hpfeedback_data = 26
    acq_is_dummyscan_data = 27
    acq_is_rtfeedback_data = 28
    acq_is_surfacecoilcorrectionscan_data = 29
    acq_user1 = 57
    acq_user2 = 58
    acq_user3 = 59
    acq_user4 = 60
    acq_user5 = 61
    acq_user6 = 62
    acq_user7 = 63
    acq_user8 = 64

# from ISMRMRD_ImageTypes
class ImageTypes(enum.IntEnum):
    imtype_magnitude = 1
    imtype_phase = 2
    imtype_real = 3
    imtype_imag = 4
    imtype_complex = 5

# from ISMRMRD_ImageFlags
class ImageFlags(enum.IntEnum):
    image_is_navigation_data = 1
    image_user1 = 57
    image_user2 = 58
    image_user3 = 59
    image_user4 = 60
    image_user5 = 61
    image_user6 = 62
    image_user7 = 63
    image_user8 = 64

# from ISMRMRD_EncodingCounters
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
    ('user',                        ('<u2', Constants.user_ints)),
])

# from ISMRMRD_AcquisitionHeader
acquisition_header_dtype = numpy.dtype([
    ('version',                     '<u2'),
    ('flags',                       '<u8'),
    ('measurement_uid',             '<u4'),
    ('scan_counter',                '<u4'),
    ('acquisition_time_stamp',      '<u4'),
    ('physiology_time_stamp',       ('<u4', Constants.phys_stamps)),
    ('number_of_samples',           '<u2'),
    ('available_channels',          '<u2'),
    ('active_channels',             '<u2'),
    ('channel_mask',                ('<u8', Constants.channel_masks)),
    ('discard_pre',                 '<u2'),
    ('discard_post',                '<u2'),
    ('center_sample',               '<u2'),
    ('encoding_space_ref',          '<u2'),
    ('trajectory_dimensions',       '<u2'),
    ('sample_time_us',              '<f4'),
    ('position',                    ('<f4', Constants.position_length)),
    ('read_dir',                    ('<f4', Constants.direction_length)),
    ('phase_dir',                   ('<f4', Constants.direction_length)),
    ('slice_dir',                   ('<f4', Constants.direction_length)),
    ('patient_table_position',      ('<f4', Constants.position_length)),
    ('idx',                         encoding_counters_dtype),
    ('user_int',                    ('<u4', Constants.user_ints)),
    ('user_float',                  ('<f4', Constants.user_floats)),
])

# from ISMRMRD_ImageHeader
image_header_dtype = numpy.dtype([
    ('version',                     '<u2'),
    ('data_type',                   '<u2'),
    ('flags',                       '<u8'),
    ('measurement_uid',             '<u4'),
    ('matrix_size',                 ('<u2', 3)),
    ('field_of_view',               ('<f4', 3)),
    ('channels',                    '<u2'),
    ('position',                    ('<f4', Constants.position_length,)),
    ('read_dir',                    ('<f4', Constants.direction_length,)),
    ('phase_dir',                   ('<f4', Constants.direction_length,)),
    ('slice_dir',                   ('<f4', Constants.direction_length,)),
    ('patient_table_position',      ('<f4', Constants.position_length,)),
    ('average',                     '<u2'),
    ('slice',                       '<u2'),
    ('contrast',                    '<u2'),
    ('phase',                       '<u2'),
    ('repetition',                  '<u2'),
    ('set',                         '<u2'),
    ('acquisition_time_stamp',      '<u4'),
    ('physiology_time_stamp',       ('<u4', Constants.phys_stamps,)),
    ('image_type',                  '<u2'),
    ('image_index',                 '<u2'),
    ('image_series_index',          '<u2'),
    ('user_int',                    ('<u4', Constants.user_ints,)),
    ('user_float',                  ('<f4', Constants.user_floats,)),
    ('attribute_string_len',        '<u4'),
])

# Mapping from ismrmrd typenums to their corresponding Numpy dtypes
ismrmrd_to_numpy_dtypes = {
    DataTypes.ushort: numpy.uint16,
    DataTypes.short: numpy.int16,
    DataTypes.uint: numpy.uint32,
    DataTypes.int: numpy.int32,
    DataTypes.float: numpy.float32,
    DataTypes.double: numpy.float64,
    DataTypes.cxfloat: numpy.complex64,
    DataTypes.cxdouble: numpy.complex128,
}