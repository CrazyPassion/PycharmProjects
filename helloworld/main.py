__author__ = 'vonking'
# coding=utf-8


class Hello:

    def __init__(self,name):
        self.name = name

    def sayHello(self):
        print("hello {0}".format("name"))


class Hi(Hello):
    def sayHi(self):
        print("hi{0}".format(self.name))

he = Hello("haha")
he.sayHello()
hi = Hi("abc")
hi.sayHi()


def level(score):
    if score >= 70:
        print("haha")
    elif score >= 60:
        print("yeah")
    else:
        print("oh no 蛋疼")

#level(59)
#for i in range(0, 100):
#    print("item {0},{1}".format(i,"hello python"))