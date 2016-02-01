__author__ = 'vonking'

students = ['hello','world','python','java']
print students[1]

students[1]='marse'
print students[1]

word = ('hello','world','python','java')
print word[1]

# word[1]='marse'
print word[1]

set1 = set("abcdeffffggss")
set2 = set("dcdsfsdfw")
print set1

print set1&set2

print set1|set2

print set1 - set2

print set(set1)

print set('sdfasfedfdsfh')

info={'name':'vonking','home':"hebei",'interesting':'music'}
print info["name"]

info["birth"]='1986/05/28'
print info['birth']
info['name'] = 'vk'
print info['name']
