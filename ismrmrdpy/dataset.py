# -*- coding: utf-8 -*-
#
# Copyright (c) 2014-2015, Ghislain Antony Vaillant
# All rights reserved.
#
# This file is distributed under the BSD License, see the LICENSE file or
# checkout the license terms at http://opensource.org/licenses/BSD-2-Clause).

from __future__ import absolute_import, division, print_function

from ismrmrdpy.backend.constants import (acquisition_header_dtype,
                                         image_header_dtype)
from ismrmrdpy.backend import acquisition
from ismrmrdpy.backend.hdf5 import as_hdf5_acquisition
import h5py


class AcquisitionListProxy(object):
    
    def __init__(self, dset):
        self._dset = dset

    def __getitem__(self, index):
        return acquisition.make_object(
            head=self._dset[index]['head'],
            traj=self._dset[index]['traj'],
            data=self._dset[index]['data'])
        
    def __setitem__(self, index, value):
        if index > len(self):
            raise ValueError("Invalid index.")
        if value['head'].dtype != acquisition_header_dtype:
            raise TypeError("Invalid value type.")
        self._dset[index] = as_hdf5_acquisition(value)

    def __len__(self):
        return self._dset.shape[0]

    def append(self, value): 
        index = len(self)
        self._dset.resize(1+len(self), axis=0)
        self.__setitem__(index, value)


class Dataset(object):
    
    def __init__(self, header=None, acquisitions=[], images={}, arrays={},
                 *args, **kwargs):
        self.header = header
        self.acquisitions = acquisitions
        self.images = images
        self.arrays = arrays
    
    @classmethod
    def load(cls, filename, *args, **kwargs):
        fobj = h5py.File(filename, 'a')
        dset = fobj['dataset']
        header = dset['xml'][0]
        acquisitions = AcquisitionListProxy(dset['data'])
        images = {}
        arrays = {}
        for key, val in dset.items():
            if key not in ('xml', 'data'):
                if 'head' in val.dtype.fields:
                    if val.dtype['head'] == image_header_dtype:
                        images[key] = val
                else:
                    arrays[key] = val
        this = cls(header=header, acquisitions=acquisitions, images=images,
                   arrays=arrays)
        this._file = fobj  # keeps the HDF5 dataset alive
        return this
        
    def save(filename, *args, **kwargs):
        pass