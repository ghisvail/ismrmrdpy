# -*- coding: utf-8 -*-
#
# Copyright (c) 2014-2015, Ghislain Antony Vaillant
# All rights reserved.
#
# This file is distributed under the BSD License, see the LICENSE file or
# checkout the license terms at http://opensource.org/licenses/BSD-2-Clause).

from __future__ import absolute_import, division, print_function

import bitarray
import numpy


class BitmaskWrapper(object):
    
    def __init__(self, array, *args, **kwargs):
        self._array = array
        self._bitmask = bitarray.bitarray(endian='little')
        self._bitmask.frombytes(array.tostring())
        
    def clear(self, indices=None):
        if indices is not None:
            for indice in indices:
                self._bitmask[indice] = 0
        else:
            self._bitmask.setall(0)
        self._update()
    
    def set(self, indices=None):
        if indices is not None:
            for indice in indices:
                self._bitmask[indice] = 1
        else:
            self._bitmask.setall(1)
        self._update()
    
    def is_set(self, indice):
        return self._bitmask[indice]
    
    def count(self):
        return self._bitmask.count(True)
        
    def _update(self):
        self._array.ravel()[:] = numpy.fromstring(self._bitmask.tobytes(),
            dtype=self._array.dtype)