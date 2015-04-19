# -*- coding: utf-8 -*-
#
# Copyright (c) 2014-2015, Ghislain Antony Vaillant
# All rights reserved.
#
# This file is distributed under the BSD License, see the LICENSE file or
# checkout the license terms at http://opensource.org/licenses/BSD-2-Clause).

from __future__ import absolute_import, division, print_function

import bitstring
import numpy


class BitMaskWrapper(object):
    
    def __init__(self, array, *args, **kwargs):
        self._array = array
        self._bitmask = bitstring.BitArray(bytes=self._array.tostring())
        
    def clear(self, indices=None):
        if indices is not None:
            self._bitmask.set(False, indices)
        else:
            self._bitmask[:] = False
    
    def set(self, indices=None):
        if indices is not None:
            self._bitmask.set(True, indices)
        else:
            self._bitmask[:] = True
    
    def is_set(self, indice):
        return self._bitmask[indice]
    
    def count(self):
        return self._bitmask.count(True)
        
    def _update(self):
        self._array.ravel()[:] = numpy.fromstring(self._bitmask.tobytes(),
            dtype=self._array.dtype)