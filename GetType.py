#!/usr/bin/env python

print type(123)
print type('str')
print type(None)
print type(abs)
print type(123) == type(345)
print type('abc')==type('123')
print type('abc')==type(123)

import types

print type('abc')== types.StringType
print type(u'abc')== types.UnicodeType
print type([]) == types.ListType
print type(str) == types.TypeType

print type(int) == type(str) == types.TypeType

print dir('ABC')
print len('ABC')
print 'ABC'.__len__()

class MyObject(object):
    def __init__(self):
        self.x = 9

    def __len__(self):
        return 100

    
obj = MyObject()
print len(obj)

print 'ABC'.lower()

obj = MyObject()
print hasattr(obj,'x')
print obj.x
print hasattr(obj, 'y')
setattr(obj, 'y', 19)
print hasattr(obj, 'y')
print getattr(obj, 'y')
print obj.y

