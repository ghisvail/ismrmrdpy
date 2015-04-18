# -*- coding: utf-8 -*-
#
# Copyright (c) 2014-2015, Ghislain Antony Vaillant
# All rights reserved.
#
# This file is distributed under the BSD License, see the LICENSE file or
# checkout the license terms at http://opensource.org/licenses/BSD-2-Clause).

from __future__ import absolute_import, division, print_function

from .constants import Constants, AcquisitionFlags, acquisition_header_dtype


def make_header(*args, **kwargs):
    pass

def make_dtype(header):
    pass

def make_array(header=None, *args, **kwargs):
    pass

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