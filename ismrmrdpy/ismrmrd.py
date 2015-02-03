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

from __future__ import absolute_import, division, print_function
from .core import *
import numpy


class AcquisitonHeader(object):
    """
    """
    def __init__(self, version=ismrmrd_libver, **kwargs):
        # TODO: more granular constructor
        self._data = numpy.zeros((), dtype=acquisition_header_dtype)
        self['version'] = version
        for kwarg in kwargs:
            self.__setitem__(kwargs)
        
    def __getitem__(self, key):
        return self._data.__getitem__(key)
        
    def __setitem__(self, key, value):
        # TODO: do not allow direct manip. of channel mask
        # TODO: do not allow direct manip. of flags
        self._data.__setitem__(key, value)
        
    def clear_channels(self, indices=None)
        pass

    def set_channels(self, indices=None):
        pass
    
    def is_channel_active(self, index):
        pass
    
    def clear_flags(self, indices=None):
        pass

    def set_flags(self, indices=None):
        pass

    def is_flag_set(self, index):
        pass

    def toarray(self):
        return self._data
        
    def tobytes(self):
        return self._data.tostring()


class Acquisiton(object):
    """
    """
    def __init__(self, head, data=None, traj=None, *args, **kwargs):
        self._head = head
        self._data = (data if data is not None else
            numpy.zeros(self.dtype['data']))
        self._traj = (data if data is not None else
            numpy.zeros(self.dtype['traj']))            

    @property
    def head(self):
        return self._head

    @property
    def data(self):
        return self._data
        
    @property
    def traj(self):
        return self._traj

    @property
    def dtype(self):
        return make_acquisition_dtype(self.head)

    def toarray(self):
        return numpy.array((self.head, self.traj, self.data),
                           dtype=self.dtype)
        
    def tobytes(self):
        return self.toarray().tostring()


class ImageHeader(object):
    """
    """
    def __init__(self, *args, **kwargs):
        pass

    def __getitem__(self, key):
        pass
        
    def __setitem__(self, key, value):
        pass

    def clear_flags(self, indices=None):
        pass

    def set_flags(self, indices=None):
        pass

    def is_flag_set(self, index):
        pass

    def toarray(self):
        return self._data
        
    def tobytes(self):
        return self._data.tostring()


class Image(object):
    """
    """
    def __init__(self, *args, **kwargs):
        pass

    @property
    def head(self):
        pass

    @property
    def attribute_string(self):
        pass

    @property
    def data(self):
        pass

    @classmethod
    def frombytes(cls, *args, **kwargs):
        pass
        
    def tobytes(self):
        pass