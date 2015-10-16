#!/usr/bin/env python

class Animal(object):
    pass

class Bird(Animal):
    pass

class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

class Runnable(object):
    def run(self):
        print 'Running...'

class Flyable(object):
    def fly(slef):
        print 'Flying...'

class Bat(Mammal, Flyable):
    pass

class Dog(Mammal, RunnalbeMixin, CarnivorousMixin):
    pass

class MyTCPServer(TCPServer, ForkingMixin):
    pass

class MyUDPServer(UDPServer, ThreadingMixin):
    pass
