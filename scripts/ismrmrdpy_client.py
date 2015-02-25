# coding: utf8

# Copyright (c) 2014-2015 Ghislain Antony Vaillant
#
# This file is distributed under the MIT License, see the LICENSE file or 
# checkout the license terms at http://opensource.org/licenses/MIT).

import enum
import argparse
import h5py
import socket
import struct
import time

@enum.unique
class message_id(enum.IntEnum):
    INT_ID_MIN                                          = 0
    CONFIG_FILE                                         = 1
    CONFIG_SCRIPT                                       = 2
    PARAMETER_SCRIPT                                    = 3
    CLOSE                                               = 4
    INT_ID_MAX                                          = 999
    EXT_ID_MIN                                          = 1000
    ACQUISITION                                         = 1001  # DEPRECATED
    NEW_MEASUREMENT                                     = 1002  # DEPRECATED
    END_OF_SCAN                                         = 1003  # DEPRECATED
    IMAGE_CPLX_FLOAT                                    = 1004  # DEPRECATED
    IMAGE_REAL_FLOAT                                    = 1005  # DEPRECATED
    IMAGE_REAL_USHORT                                   = 1006  # DEPRECATED
    EMPTY                                               = 1007  # DEPRECATED
    ISMRMRD_ACQUISITION                                 = 1008
    ISMRMRD_IMAGE_CPLX_FLOAT                            = 1009
    ISMRMRD_IMAGE_REAL_FLOAT                            = 1010
    ISMRMRD_IMAGE_REAL_USHORT                           = 1011
    DICOM                                               = 1012
    CLOUD_JOB                                           = 1013
    GADGETCLOUD_JOB                                     = 1014
    ISMRMRD_IMAGEWITHATTRIB_CPLX_FLOAT                  = 1015
    ISMRMRD_IMAGEWITHATTRIB_REAL_FLOAT                  = 1016
    ISMRMRD_IMAGEWITHATTRIB_REAL_USHORT                 = 1017
    DICOM_WITHNAME                                      = 1018
    DEPENDENCY_QUERY                                    = 1019
    EXT_ID_MAX                                          = 4096


# command line interface
DESCRIPTION = """Streaming client for ISMRMRD / Gadgetron
"""

EPILOG = """TODO"""

parser = argparse.ArgumentParser(
    description=DESCRIPTION,
    epilog=EPILOG,
    )
parser.add_argument("file", help="input HDF5 file")
parser.add_argument("--host",
                    help="server hostname", default='localhost')
parser.add_argument("--port",
                    help="port number", type=int, default=9002)
parser.add_argument("--config",
                    help="config file", default='default.xml')
parser.add_argument("--group",
                    help="HDF5 group name", default='dataset')
args = parser.parse_args()


# read XML header and acquisitions from the HDF5 file
h5file = h5py.File(args.file)
dset = h5file[args.group]
xml_header = dset['xml'][0]
acqs = dset['data']


# connect to Gadgetron server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((args.host, args.port))
# TODO: handle connection errors
config_msg = struct.pack('<H1024s', message_id.CONFIG_FILE, args.config.encode())
sock.sendall(config_msg)
params_msg = (struct.pack('<H', message_id.PARAMETER_SCRIPT) +
              struct.pack('<I', 1+len(xml_header)) +
              xml_header +
              '\0'.encode())
sock.sendall(params_msg)
for iacq, acq in enumerate(acqs):
    print('sending acquisition %d' %(1+iacq))
    acq_msg = struct.pack('<H', message_id.ISMRMRD_ACQUISITION)
    acq_msg += acq['head'].tostring()
    if acq['traj'].size != 0:
        acq_msg += acq['traj'].tostring()
    acq_msg += acq['data'].tostring()
    sock.sendall(acq_msg)
    time.sleep(5e-3)  # simulate 5ms TR
time.sleep(1)  # give the server some time to process stuff
close_msg = struct.pack('<H', message_id.CLOSE)
sent = sock.send(close_msg)
sock.close()