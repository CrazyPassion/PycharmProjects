__author__ = 'vonking'

import os

#pattern = re.compile(r'abc+\s*=\s*\d') match = pattern.match(line)

readtime = 0
data = []
for path, dirname, filenamelist in os.walk('/Users/vonking/Desktop/test'):
    for filename in filenamelist:
        f = open(str(path) + '/' + str(filename))
        print filename
        for line in f.readlines():
            readtime += 1
            if readtime in range(3, 5):
                data.append(line)

print data

