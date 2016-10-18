# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 13:58:26 2016

@author: songxf
"""
"""
Chapter eight List

"""


cd E:/Programing/Python/Python_for_everybody
#A list is a kind of collection
for i in [5,4,3,2,1]:
    print(i)
print('Blastoff')



friends=['Joseph','Blenn','Sally']

for friend in friends:
    print('Happy new year:',friend)
print('Done!')


friends=['Joseph','Blenn','Sally']
print(friends[1])

# Mutable and not mutable, strings are not mutable, list is mutable
fruit='Banana'
fruit[0]='b'

x=fruit.lower()
print(x)

lotto=[2,14,26,41,63]
print(lotto)
lotto[2]=28
print(lotto)

#How long is a list?
greet='Hello Bob'
print(len(greet))

x=[1,2,'joe',99]
print(len(x))

# Using the range function

print(range(4))

friends=['Joseph','Blenn','Sally']
print(len(friends))

print(range(len(friends)))

# A tale of two loops
friends=['Joseph','Blenn','Sally']

for friend in friends:
    print('Happy new year:',friend)

for i in range(len(friends)):
    friend=friends[i]
    print("Happy new year:",friend)

# concatenating lists using+，使用 + 来连接列表

a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)
print(a)

# lists can be sliced using,列表和字符串一样，可以被sliced
t=[9,41,12,3,74,15]
t[1:3]
t[:4]
t[3:]
t[:]

# Methods related to List
x=list()
type(x)
dir(x) #显示type(x)可以使用的方法


stuff=list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

# Is something in a list? Use in to test weather a object is in a list.

some=[1,9,21,10,16]
9 in some
15 in some
20 not in some

# a list is an ordered sequence,列表是个有序的序列

friends=['Joseph','Blenn','Sally']
friends.sort()
print(friends)
print(friends[1])

# Built in functions and lists
nums=[3,41,12,9,74,15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

# Two ways to averaging with a list
total=0
count=0
while True:
    inp=input('Please enter a number:')
    if inp=='done':break
    value=float(inp)
    total=total+value
    count=count+1
average=total/count
print('Average:',average)

numlist=list()
while True:
    inp=input('Please enter a number:')
    if inp=='done':
        break
    value=float(inp)
    numlist.append(value)
average=sum(numlist)/len(numlist)
print('Average:',average)

# connecting strings and list: strings and lists

abc='With three words'
stuff=abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])

for w in stuff:
    print(w)


line='A lot                 of spaces'
etc=line.split()
print(etc)
line='first;second;third'
thing=line.split()
print(thing)
print(len(thing))
thing=line.split(';')
print(thing)
print(len(thing))

fhand=open('mbox.txt')
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From '):
        continue
    words=line.split()
    print(words[2])
    
line='From stephen.marquard@uct.zc.za Sat Jan 5 09:14:16 2008'
words=line.split()
print (words)
email=words[1]
pieces=email.split('@')
print(pieces[1])


# Or you can do it in this way
"""
a=email.find('@')
print(email[a+1:])
"""

















