#!/usr/bin/env python
def add(x, y, f):
    return f(x) + f(y)

def main():
    print add(-5, 6, abs)

main()

