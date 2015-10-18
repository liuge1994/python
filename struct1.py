#!/usr/bin/env python

import struct, sys

def isbmp(path):
    f = open(path, 'rb')
    b = f.read(30)

    info = struct.unpack('<ccIIIIIIHH', b)
    if info[0] + info[1] == 'BA' or info[0] + info[1] == 'BM':
        print 'the size of file: %s, the color of file : %s' %(info[6] * info[7], info[9])
    else:
        print 'file is not a bmp!'
    f.close()

isbmp(sys.argv[1])
