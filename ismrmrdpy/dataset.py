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
from ismrmrdpy.backend import image
from ismrmrdpy.backend.hdf5 import as_hdf5_acquisition
import h5py


#class AcquisitionListProxy(object):
#    
#    def __init__(self, dset):
#        self._dset = dset
#
#    def __getitem__(self, index):
#        return acquisition.make_object(
#            head=self._dset[index]['head'],
#            traj=self._dset[index]['traj'],
#            data=self._dset[index]['data'])
#        
#    def __setitem__(self, index, value):
#        if value['head'].dtype != acquisition_header_dtype:
#            raise TypeError("Invalid value type.")
#        self._dset[index] = as_hdf5_acquisition(value)
#
#    def __len__(self):
#        return self._dset.shape[0]
#
#    def append(self, value): 
#        index = len(self)
#        self._dset.resize(1+len(self), axis=0)
#        self.__setitem__(index, value)          
#
#
#class AcquisitionProxy(object):
#    
#    def __init__(self, dset):
#        self._dset = dset
#    
#    def __get__(self):
#        if 'data' not in self._dset:
#            raise RuntimeError("Dataset does not contain any acquisitions.")
#        return AcquisitionListProxy(self._dset['data'])
#
#
#class ImageListProxy(object):
#    
#    def __init__(self, dset):
#        self._dset = dset
#    
#    def __getitem__(self, index):
#        self.check_index()
#        return image.make_object(
#            head=self._dset['header'][index],
#            attribute_string=self._dset['attributes'][index],
#            data=self._dset['data'][index],)
#    
#    def __setitem__(self, index, value):
#        self.check_index() 
#        self._dset['header'][index] = value['head']
#        self._dset['attributes'][index] = value['attribute_string'] 
#        self._dset['data'][index] = value['data']
#    
#    def __len__(self):
#        if 'header' not in self._dset:
#            return 0
#        else:
#            return self._dset['header'].shape[0]      
#  
#    def append(self, value):
#        index = len(self)
#        if 'header' not in self._dset:
#            dtype = image.make_dtype(value['head'])
#            self._dset.create_dataset('header', maxshape=(1,),
#                                      dtype=dtype['head'])
#            self._dset.create_dataset('attributes', maxshape=(1,),
#                                      dtype=h5py.special_dtype(vlen=str))
#            self._dset.create_dataset('data', maxshape=(1,),
#                                      dtype=dtype['data'])
#        else:
#            self._dset['header'].resize(1+index, axis=0)
#            self._dset['attributes'].resize(1+index, axis=0)
#            self._dset['data'].resize(1+index, axis=0)
#        self[index] = value
#
#    def check_index(self, index):
#        if len(self) == 0:
#            raise RuntimeError("Dataset is empty.")
#        if index > len(self):
#            raise ValueError("Invalid index.")  
#
#
#class ImageDictProxy(object):
#    
#    def __init__(self, dset):
#        self._dset = dset
#
#    def __getitem__(self, key):
#        if key not in self:
#            self._dset.require_group(key)
#        return ImageListProxy(self._dset[key])           
#    
#    def __contains__(self, key):
#        return key in self.keys()
#    
#    def keys(self):
#        return [key for key in self._dset if (
#            'header' in self._dset[key] and
#            self._dset[key]['header'].dtype == image_header_dtype
#            )]
#
#
#class ArrayListProxy(object):
#    
#    def __init__(self, dset):
#        self._dset = dset
#    
#    def __getitem__(self, index):
#        if len(self) < 1:
#            raise RuntimeError("Dataset is empty.")
#        return self._dset[index].copy()
#    
#    def __len__(self):
#        if hasattr(self._dset, 'shape'):
#            return self._dset.shape[0]
#        else:
#            return 0
#
#
#class ArrayDictProxy(object):
#    
#    def __init__(self, dset):
#        self._dset = dset
#
#    def __getitem__(self, key):
#        if key not in self:
#            self._dset.require_group(key)
#        return ArrayListProxy(self._dset[key])
#
#    def __contains__(self, key):
#        return key in self.keys()
#    
#    def keys(self):
#        return [key for key in self._dset if (
#            hasattr(self._dset[key], 'shape') and
#            len(self._dset[key].shape) > 1
#            )]
#
#
#class IsmrmrdHeaderProxy(object):
#    
#    def __init__(self, dset):
#        self._dset = dset
#    
#    def __get__(self):
#        if 'xml' not in self._dset:
#            raise RuntimeError("Dataset does not contain an xml header.")
#        return self._dset['xml'][0].decode('utf-8')
#
#
#class OldDataset(object):
#    
#    def __init__(self, header=None, acquisitions=[], images={}, arrays={},
#                 *args, **kwargs):
#        self.header = header
#        self.acquisitions = acquisitions
#        self.images = images
#        self.arrays = arrays
#    
#    @classmethod
#    def load(cls, filename, *args, **kwargs):
#        root = h5py.File(filename, 'a')
#        groupname = kwargs.get('groupname', 'dataset')
#        dset = root[groupname]
#        header = IsmrmrdHeaderProxy(dset)
#        acquisitions = AcquisitionProxy(dset)
#        images = ImageDictProxy(dset)
#        arrays = ArrayDictProxy(dset)
#        this = cls(header=header, acquisitions=acquisitions, images=images,
#                   arrays=arrays)
#        this._root = root  # keeps the HDF5 dataset alive
#        return this
#        
#    def save(filename, *args, **kwargs):
#        pass


class File(object):
    
    def __init__(self, name, *args, **kwargs):
        self._file = h5py.File(name, *args, **kwargs)
    
    def create_dataset(self, name):
        group = self._file.create_group(name)
        return Dataset(group)
    
    def require_dataset(self, name):
        group = self._file.require_group(name)
        return Dataset(group)

    def __getitem__(self, name):
        try:
            return self.create_dataset(name)
        except ValueError:
            return self.require_dataset(name)
    
    def __setitem__(self, name, value):
        if not isinstance(value, Dataset): 
            raise ValueError("Value should be a Dataset object.")
        self[name] = value
        
    def __contains__(self, name):
        return name in self.keys()

    def keys(self):
        return self._file.keys()

    @property
    def filename(self):
        return self._file.filename
    
    @property
    def datasets(self):
        # should return paths where datasets were detected.
        pass       


class Dataset(object):
    
    def __init__(self, group, *args, **kwargs):
        self._group = group
        self.header = HeaderProxy(self._group)
        self.acquisitions = AcquisitionsListProxy(self._group)
        self.images = ImagesDictProxy(self._group)
        self.arrays = ArraysDictProxy(self._group)


class HeaderProxy(object):
    
    def __init__(self, group, *args, **kwargs):
        self._group = group
    
    def read(self):
        return self._group['xml'][0].decode('utf-8')

    def write(self, string):
        pass


class AcquisitionsListProxy(object):
    
    def __init__(self, group, *args, **kwargs):
        self._group = group


class ImagesListProxy(object):
    
    def __init__(self, group, *args, **kwargs):
        self._group = group


class ArraysListProxy(object):
    
    def __init__(self, group, *args, **kwargs):
        self._group = group


class ImagesDictProxy(object):
    
    def __init__(self, group, *args, **kwargs):
        self._group = group


class ArraysDictProxy(object):
    
    def __init__(self, group, *args, **kwargs):
        self._group = group        