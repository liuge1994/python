#!/usr/bin/env python

class Student(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object(name: %s)' %self.name

    __repr__ = __str__

print Student('Michael')

s = Student('Michael')
s

class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def next(self):
        self.a, self.b = self.b, self.a + self.a
        if self.a > 100000:
            raise StopIteration()
        return self.a

class Fib2(object):

    def __init__(self):
        self.a, self.b = 0, 1

    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a 

for n in Fib():
    print n
    
f = Fib2()
print f[0]
print f[1]
print f[2]
print f[3]
print f[10]
print f[100]

class Fib3(object):
    
    def __init__(self):
        self.a, self.b = 0, 1

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a 
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib3()
print f[0:5]
print f[:10]

class Student2(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25

class Student3(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' %attr)

s = Student2()
print s.name
print s.score
print s.age()

    
class Chain(object):

    def __init__(self, path =''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' %(self._path, path))

    def __str__(self):
        return self._path

print Chain().status.user.timeline.list
