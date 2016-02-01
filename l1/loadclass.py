__author__ = 'vonking'


import classtest

h1 = classtest.Hello("test")
h1.sayHello()

from classtest import Hello

h2 = Hello("test2")
h2.sayHello()