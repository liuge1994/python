#!/usr/bin/env python
import os
print range(1, 11)

L = []
for x in range(1, 11):
    L.append(x*x)

print L

print [x * x for x in range(1, 11)]

print [x * x for x in range(1, 11) if x % 2 == 0]

print [m + n for m in 'ABC' for n in 'XYZ']

print [d for d in os.listdir('.')]

d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.iteritems():
    print k, '=', v

L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]

L = ['Hello', 'World', 18, 'Apple', None]
L = [s.lower() if isinstance(s, str) else s for s in L]
print L
