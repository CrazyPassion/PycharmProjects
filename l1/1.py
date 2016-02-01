__author__ = 'vonking'

# len in + * str[start:finish]  str[start:finish:countBy]  str is immutable; str.replace, str.find, str.split(dir(str))
#open('1.txt') f.close str.strip():delete enter str.title:  first :Upper , other lower
#regular expression : . 任意字符 \d+ 表示一系列数字 [a-z] 表示一个小写字母  需要import re  re.search(pattern, string)
# list.append list.extend([a,b]) list.insert(position, element)  list.pop list.remove  list.sort  list.reverse
# list.index  sorted list.sort
# dict.items() dict.keys() dict.values() dict.clear()
print len('helloworld')

#radius = raw_input("radius is:")

"""
def fib1(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib1(n-1) + fib1(n-2) + 3

n = input("input a num:")
print fib1(n)


def fun1(n):
    if n == 1:
        #print "oh herererer"
        return 1
    else:
        #print "here"
        return 2 * fun1(n - 1) + 1


def main():
    n = int(raw_input("Input count:"))
    #print "num is", n
    print fun1(n)

main()
"""

lambda