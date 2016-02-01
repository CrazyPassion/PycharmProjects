#-*-coding:utf8-*-

import re
source = "s2f程序员杂志一2d3程序员杂志二2d3程序员杂志三2d3程序员杂志四2d3"
print source.decode('ascii')
temp = source.decode('utf8')
print temp
#pattern = re.compile(xx)
results =  re.findall('程序员(.*?)2',temp,re.S)
for result in results :
  print result