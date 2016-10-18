# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 13:40:28 2016

@author: songxf
"""
"""
Chapter Ten Tuples

"""

cd E:\Programing\Python\Python_for_everybody


# Tuples(元组)和list(列表)很像，

x=('Glenn','Sally','Joseph')
print(x[2])
y=(1,9,2)
print(y)

print(max(y))


for iter in y:
    print(iter)


# Tuples are "immutable",like strings, unlike tuples,与字符串类似，元组是不可更改的，但是列表是可更改的
# lists are mutable
x=[9,8,7]
x[2]=6
print(x)


# Strings are immutable
y='ABC'
y[2]='D'

# Tuples are immutable
z=(5,4,3)
z[2]=0

# Things not to do with tuples
x=(3,2,1)
x.sort()
x.append(5)
x.reverse()

dir(x)

"""
元组的优点：
元组更加的有效率，Python不需要为元组构建可更改的结构，
因此是更加简单和更加有效率的，与列表相比，在存储使用和运行速度上是更好的。
如果我们创建存储暂时的变量，如果我们不会修改其中的内容的话，我们更加偏好使用元组数据结构


"""
# Tuples and Assignment，可以使用元组来为多个变量赋值

(x,y)=(4,'fred')
print(y)

(a,b)=(99,98)
print(a)

"""
元组与字典：

"""
d=dict()
d['csev']=2
d['cwen']=4

for (k,v) in d.items():
    print(k,v)

tups=d.items() #得到一个tuples列表，列表的元素是tuple
print(tups)

"""
Tuples are comparable
元组之间是可以相互比较的

"""
(0,1,2)<(5,1,2)

(0,1,200000)<(0,3,4)

('Jones','Sally')<('Jones','Fred')

('Jones','Sally')>('Adams','Sam')

"""
为元组列表排序(Sorting lists of tuples)
"""
d={'a':10,'b':1,'c':22}

t=d.items()

print(t)

t1=t.sort()  #AttributeError: 'dict_items' object has no attribute 'sort'

t1

# Using sorted()

d={'a':10,'b':1,'c':22}
d.items()
t=sorted(d.items())
t

for (k,v) in sorted(d.items()):
    print (k,v)

"""
Sort by values instead of key
"""

c={'a':10,'b':1,'c':22}
tmp=list()
for k,v in c.items():
    tmp.append((v,k))
print(tmp)
tmp.sort(reverse=True)
print(tmp)

"""
"""

fhand=open('mbox-short.txt')
counts=dict()
for line in fhand:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

lst=list()
for (key,val) in counts.items():
    lst.append((val,key))
    
lst.sort(reverse=True)
for val,key in lst[:10]:
    print(val,key)


"""
Even shorter version(adv)
"""
c={'a':10,'b':1,'c':22}
print(sorted([(v,k) for (k,v) in c.items()]))

""""

""""




