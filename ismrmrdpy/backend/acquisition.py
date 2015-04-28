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
from .bitmask import BitmaskWrapper
import numpy


header_dtype = acquisition_header_dtype

def make_header(version=Constants.version, *args, **kwargs):
    """Generates an array of type ISMRMRD acquisition header.
    
    Generates a Numpy array whose dtype satisfies the ISMRMRD acquisition 
    header data structure specifications.
    
    Parameters
    ----------
    version : int, optional
        Version of the ISMRMRD acquisition header specifications. Should be 
        left to its default value, which is defined in the `constants` module.
    **kwargs
        Optional initialization values for ISMRMRD acquisition header 
        metadata.
        
    Returns
    -------
    ndarray
        ISMRMRD acquisition header.
    
    Examples
    --------
    By default, all items in the resulting array defaults to 0, besides 
    version.
    
    >>> hdr = make_header()
    >>> print(hdr['number_of_samples'])
    0
    
    Alternative default values may be provided using the corresponding keyword 
    argument.
    
    >>> hdr = make_header(number_of_samples=256, active_channels=8)
    >>> print(hdr['number_of_samples'])
    256
    >>> print(hdr['active_channels'])
    8
    
    """
    header = numpy.zeros((), dtype=header_dtype)
    header['version'] = version
    for key in kwargs:
        if key in header_dtype.fields:
            header[key] = kwargs[key]
    return header    

def deserialize_header(bytestring):
    """Deserialize an ISMRMRD acquisition header from an arbitrary string of 
    bytes.
    """
    return numpy.fromstring(bytestring, dtype=header_dtype)[0]

def make_dtype(header):
    """Dynamically generate the ISMRMRD acquisition dtype.
    
    Helper function for generating the ISMRMRD acquisition dtype described by 
    its header.
    
    Parameters
    ----------
    header : dict-like
        Object containing the required metadata information to construct the 
        ISMRMRD acquisition dtype, i.e. number_of_samples, active_channels and 
        trajectory_dimensions.
        
    Returns
    -------
    numpy.dtype
        ISMRMRD acquisition dtype.
    
    """
    data_dtype = ismrmrd_to_numpy_dtypes[DataTypes.cxfloat]
    data_shape = (header['active_channels'],
                  header['number_of_samples'])
    traj_dtype = ismrmrd_to_numpy_dtypes[DataTypes.float]
    traj_shape = (header['number_of_samples'],
                  header['trajectory_dimensions'])
    return numpy.dtype([
        ('head',    header_dtype),
        ('traj',    (traj_dtype, traj_shape)),
        ('data',    (data_dtype, data_shape)),
    ])

def make_object(head=None, traj=None, data=None, *args, **kwargs):
    """Generates an array of type ISMRMRD acquisition.
    
    Generates a Numpy array whose dtype satisfies the ISMRMRD acquisition 
    data structure specifications.   
    
    Parameters
    ----------
    head : ndarray, optional
        Array containing the ISMRMRD acquisition header metadata, generated 
        using the `make_head` function. If not specified, a header is 
        generated from the optional keyword arguments.
    *args
        Optional trajectory [0] and data arrays [1] to initialize the 
        acquisition with. Both should be provided in order to override the 
        default value, which is to initialize both arrays with 0.
    **kwargs
        Optional keyword arguments, used internally for generating a header 
        if the latter is missing from the argument list.
    
    Returns
    -------
    ndarray
        ISMRMRD acquisition object.
    
    """
    head = head or make_header(**kwargs)
    dtype = make_dtype(head)
    array = numpy.zeros((), dtype=dtype)
    array['head'] = head
    if traj is not None:
        array['traj'] = traj.view(dtype['traj'].base).reshape(dtype['traj'].shape)
    if data is not None:
        array['data'] = data.view(dtype['data'].base).reshape(dtype['data'].shape)
    return array

def deserialize_object(bytestring):
    """Deserialize an ISMRMRD acquisition object from an arbitrary string of 
    bytes.
    """
    header = deserialize_header(bytestring[:header_dtype.itemsize])
    return numpy.fromstring(bytestring, dtype=make_dtype(header))[0]

def set_flags(header, flags=None):
    """Utility function for management of flag related metadata."""
    bitmask = BitmaskWrapper(header['flags'])
    if flags is not None:
        _verify_flags(flags)
        bitmask.set([flag-1 for flag in flags])
    else:
        bitmask.set()
    
def clear_flags(header, flags=None):
    """Utility function for management of flag related metadata."""
    bitmask = BitmaskWrapper(header['flags'])
    if flags is not None:
        _verify_flags(flags)
        bitmask.clear([flag-1 for flag in flags])
    else:
        bitmask.clear()

def is_flag_set(header, flag):
    """Utility function for management of flag related metadata."""
    bitmask = BitmaskWrapper(header['flags'])
    _verify_flags([flag,])
    return bitmask.is_set(flag-1)    

def _verify_flags(flags):
    """Utility function for management of flag related metadata."""
    for flag in flags:
        if flag not in AcquisitionFlags:
            raise ValueError("Invalid flag provided: {}.".format(flag))

def set_channels(header, channels=None):
    """Utility function for management of channel related metadata."""
    bitmask = BitmaskWrapper(header['channel_mask'])
    if channels is not None:
        _verify_channels(channels)
        bitmask.set([channel-1 for channel in channels])
    else:
        bitmask.set()
    header['active_channels'] = bitmask.count()

def clear_channels(header, channels=None):
    """Utility function for management of channel related metadata."""
    bitmask = BitmaskWrapper(header['channel_mask'])
    if channels is not None:
        _verify_channels(channels)
        bitmask.clear([channel-1 for channel in channels])
    else:
        bitmask.clear()
    header['active_channels'] = bitmask.count()

def is_channel_set(header, channel):
    """Utility function for management of channel related metadata."""
    bitmask = BitmaskWrapper(header['channel_mask'])
    _verify_channels([channel,])
    return bitmask.is_set(channel-1) 

def _verify_channels(channels):
    """Utility function for management of channel related metadata."""
    for channel in channels:
        if channel < 1:
            raise ValueError("Invalid channel provided: {}.".format(channel))