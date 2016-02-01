__author__ = 'vonking'

class Hello:
    def __init__(self,name):
        self._name = name;

    def sayHello(self):
        print("Hello {0}".format(self._name))


class Hi(Hello):
    def __init__(self,name):
        self._name = name;

    def sayHi(self):
        print("Hello 2nd {0}".format(self._name))
#
# h1 = Hello("vk")
# h1.sayHello()
#
# h2 = Hi("vvkk")
# h2.sayHello()
# h2.sayHi()
# h2._name