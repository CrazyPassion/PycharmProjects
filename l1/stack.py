__author__ = 'vonking'

class Stack():
    def __init__(self,size):
        self.stack = []
        self.size = size
        self.top = -1

    def push(self,data):
        if self.Full():
            print 'Stack is full'
        else:
            self.stack.append(data)
            self.top += 1

    def Full(self):
        return self.top >= self.size

    def pop(self):
        if self.empty():
            print 'stack is empty'
        else:
            self.stack.remove(self.top)
            self.top -= 1


    def empty(self):
        return self.top == -1