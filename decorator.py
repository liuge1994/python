#!/usr/bin/env python
def now():
    print '2013-12-25'

f = now
f()
print now.__name__
print f.__name__

def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' %func.__name__
        return func(*args, **kw)
    return wrapper

@log      
def now():
    print '2013-12-25'
#== now = log(now)

now()

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' %(text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print '2013-12-25'
#now = log('execute')(now)

now()
print now.__name__

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' %func.__name__
        return func(*args, **kw)
    return wrapper

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' %(text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator


