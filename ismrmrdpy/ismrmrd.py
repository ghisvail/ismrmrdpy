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


class AcquisitonHeader(object):
    """
    """
    def __init__(self, *args, **kwargs):
        pass
    
    def __getitem__(self, key):
        pass
        
    def __setitem__(self, key, value):
        pass
        
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

    @classmethod
    def frombytes(cls, *args, **kwargs):
        pass

    def tobytes(self):
        pass


class Acquisiton(object):
    """
    """
    def __init__(self, *args, **kwargs):
        pass

    @property
    def header(self):
        pass

    @property
    def data(self):
        pass
        
    @property
    def traj(self):
        pass

    @classmethod
    def frombytes(cls, *args, **kwargs):
        pass
        
    def tobytes(self):
        pass


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

    @classmethod
    def frombytes(cls, *args, **kwargs):
        pass
        
    def tobytes(self):
        pass


class Image(object):
    """
    """
    def __init__(self, *args, **kwargs):
        pass

    @property
    def header(self):
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