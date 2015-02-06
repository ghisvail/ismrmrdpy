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

# TODO: this file could be generated from a vendorized or system-installed ismrmrd.h header file.

# Constants
ISMRMRD_VERSION             = 1
ISMRMRD_USER_INTS           = 8
ISMRMRD_USER_FLOATS         = 8
ISMRMRD_PHYS_STAMPS         = 3
ISMRMRD_CHANNEL_MASKS       = 16
ISMRMRD_NDARRAY_MAXDIM      = 7
ISMRMRD_POSITION_LENGTH     = 3
ISMRMRD_DIRECTION_LENGTH    = 3

# Data Types
ISMRMRD_USHORT   = 1
ISMRMRD_SHORT    = 2
ISMRMRD_UINT     = 3
ISMRMRD_INT      = 4
ISMRMRD_FLOAT    = 5
ISMRMRD_DOUBLE   = 6
ISMRMRD_CXFLOAT  = 7
ISMRMRD_CXDOUBLE = 8

# Acquisition Flags
ISMRMRD_ACQ_FIRST_IN_ENCODE_STEP1               =  1
ISMRMRD_ACQ_LAST_IN_ENCODE_STEP1                =  2
ISMRMRD_ACQ_FIRST_IN_ENCODE_STEP2               =  3
ISMRMRD_ACQ_LAST_IN_ENCODE_STEP2                =  4
ISMRMRD_ACQ_FIRST_IN_AVERAGE                    =  5
ISMRMRD_ACQ_LAST_IN_AVERAGE                     =  6
ISMRMRD_ACQ_FIRST_IN_SLICE                      =  7
ISMRMRD_ACQ_LAST_IN_SLICE                       =  8
ISMRMRD_ACQ_FIRST_IN_CONTRAST                   =  9
ISMRMRD_ACQ_LAST_IN_CONTRAST                    = 10
ISMRMRD_ACQ_FIRST_IN_PHASE                      = 11
ISMRMRD_ACQ_LAST_IN_PHASE                       = 12
ISMRMRD_ACQ_FIRST_IN_REPETITION                 = 13
ISMRMRD_ACQ_LAST_IN_REPETITION                  = 14
ISMRMRD_ACQ_FIRST_IN_SET                        = 15
ISMRMRD_ACQ_LAST_IN_SET                         = 16
ISMRMRD_ACQ_FIRST_IN_SEGMENT                    = 17
ISMRMRD_ACQ_LAST_IN_SEGMENT                     = 18
ISMRMRD_ACQ_IS_NOISE_MEASUREMENT                = 19
ISMRMRD_ACQ_IS_PARALLEL_CALIBRATION             = 20
ISMRMRD_ACQ_IS_PARALLEL_CALIBRATION_AND_IMAGING = 21
ISMRMRD_ACQ_IS_REVERSE                          = 22
ISMRMRD_ACQ_IS_NAVIGATION_DATA                  = 23
ISMRMRD_ACQ_IS_PHASECORR_DATA                   = 24
ISMRMRD_ACQ_LAST_IN_MEASUREMENT                 = 25
ISMRMRD_ACQ_IS_HPFEEDBACK_DATA                  = 26
ISMRMRD_ACQ_IS_DUMMYSCAN_DATA                   = 27
ISMRMRD_ACQ_IS_RTFEEDBACK_DATA                  = 28
ISMRMRD_ACQ_IS_SURFACECOILCORRECTIONSCAN_DATA   = 29
ISMRMRD_ACQ_USER1                               = 57
ISMRMRD_ACQ_USER2                               = 58
ISMRMRD_ACQ_USER3                               = 59
ISMRMRD_ACQ_USER4                               = 60
ISMRMRD_ACQ_USER5                               = 61
ISMRMRD_ACQ_USER6                               = 62
ISMRMRD_ACQ_USER7                               = 63
ISMRMRD_ACQ_USER8                               = 64

# Image Types
ISMRMRD_IMTYPE_MAGNITUDE = 1
ISMRMRD_IMTYPE_PHASE     = 2
ISMRMRD_IMTYPE_REAL      = 3
ISMRMRD_IMTYPE_IMAG      = 4
ISMRMRD_IMTYPE_COMPLEX   = 5

# Image Flags
ISMRMRD_IMAGE_IS_NAVIGATION_DATA =  1
ISMRMRD_IMAGE_USER1              = 57
ISMRMRD_IMAGE_USER2              = 58
ISMRMRD_IMAGE_USER3              = 59
ISMRMRD_IMAGE_USER4              = 60
ISMRMRD_IMAGE_USER5              = 61
ISMRMRD_IMAGE_USER6              = 62
ISMRMRD_IMAGE_USER7              = 63
ISMRMRD_IMAGE_USER8              = 64

# ISMRMRD Encoding Counters
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

# ISMRMRD Acquisition Header
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

# ISMRMRD Image Header
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