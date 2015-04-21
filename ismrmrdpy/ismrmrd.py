# -*- coding: utf-8 -*-
#
# Copyright (c) 2014-2015, Ghislain Antony Vaillant
# All rights reserved.
#
# This file is distributed under the BSD License, see the LICENSE file or
# checkout the license terms at http://opensource.org/licenses/BSD-2-Clause).

from __future__ import absolute_import, division, print_function


from ismrmrdpy.backend import acquisition
from ismrmrdpy.backend import image
import numpy


class AcquisitionFlagsProperty(object):
    
    def __init__(self, header):
        self._header = header
    
    def set(self, flags=None):
        acquisition.set_flags(self._header, flags)
    
    def clear(self, flags=None):
        acquisition.clear_flags(self._header, flags)


class AcquisitionChannelsProperty(object):
    
    def __init__(self, header):
        self._header = header
    
    def set(self, channels=None):
        acquisition.set_channels(self._header, channels)
    
    def clear(self, channels=None):
        acquisition.clear_channels(self._header, channels)


class AcquisitionHeader(object):
    
    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            self._header = numpy.asarray(args[0], dtype=acquisition.header_dtype)
        else:
            self._header = acquisition.make_header(*args, **kwargs)
        self.flags = AcquisitionFlagsProperty(self._header)
        self.channels = AcquisitionChannelsProperty(self._header)
    
    def __getitem__(self, key):
        return self._header[key]
    
    def __setitem__(self, key, value):
        if key in ('flags',):
            raise KeyError("Use the flags attribute to manipulate flag related metadata.")
        if key in ('channel_mask', 'active_channels'):
            raise KeyError("Use the channels attribute to manipulate channel related metadata.")
        self._header[key] = value


class Acquisition(object):
    
    def __init__(self, header=None, trajectory=None, data=None, *args,
                 **kwargs):
        self._head = header or AcquisitionHeader(*args, **kwargs)
        self._traj = None
        self._data = None
        if trajectory is not None:
            self.trajectory = trajectory      
        if data is not None:
            self.data = data

    def __getitem__(self, key):
        if key in ('head',):
            return self.header
        elif key in ('traj',):
            return self.trajectory
        elif key in ('data',):
            return self.data
        else:
            return self.header[key]
    
    @property
    def header(self):
        return self._head
    
    @property
    def trajectory(self):
        if self._traj is None:
            dtype = acquisition.make_dtype(self.header)
            self._traj = numpy.zeros(dtype=dtype['traj'])
        else:
            return self._traj
    
    @trajectory.setter
    def trajectory(self, value):
        dtype = acquisition.make_dtype(self.header)
        self._traj[:, :] = numpy.asarray(value, dtype=dtype['traj'].base).reshape([dtype['traj'].shape])

    @property
    def data(self):
        if self._data is None:
            dtype = acquisition.make_dtype(self.header)
            self._data = numpy.zeros(dtype=dtype['data'])
        else:
            return self._data
    
    @data.setter
    def data(self, value):
        dtype = acquisition.make_dtype(self.header)
        self._data[:, :] = numpy.asarray(value, dtype=dtype['data'].base).reshape([dtype['data'].shape])


class ImageHeader(object):
    pass

class Image(object):
    pass