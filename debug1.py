#!/usr/bin/env python

def foo():
    r = some_function()
    if r == (-1):
        return (-1)
    #do something
    return r

def bar():
    r = foo()
    if r == (-1):
        print 'Error'
    else:
        pass

try: 
    print 'try...'
    r = 10 / 0
    print 'result:', r
except ZeroDivisionError, e:
    print 'except: ', e
finally:
    print 'finally...'
print 'END'

try:
    print 'try...'
    r = 10 / int('a')
    print 'result: ', r
except ValueError, e:
    print 'ValueError: ', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError: ', e
finally:
    print 'finally...'
print 'END'


try:
    print 'try...'
    r = 10 / int('a')
    print 'result: ', r
except ValueError, e:
    print 'valueError: ', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError: ', e
else:
    print 'no error!'
finally:
    print 'finally...'
print 'END'

try:
    foo()
except StandardError, e:
    print 'StandardError'
except ValueError, e:
    print 'ValueError'


