# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 20:00:55 2016

@author: songxf
"""
"""
Chapter Nine Dictionary

"""

cd E:\Programing\Python\Python_for_everybody

purse=dict()
purse['money']=12
purse['candy']=3
purse['tissues']=75
print(purse)

print(purse['candy'])
purse['candy']=purse['candy']+2
print(purse['candy'])
print(purse)

# 列表和字典都可以存储许多值，不同的是如何标识数据，如何存储，如何读取
# 字典和列表很像，不同之处是字典使用keys（键值）代替numbers（数字）来寻找存储在其中的value（值）
# 字典内部没有排序

lst=list()
lst.append(21)
lst.append(183)
print(lst)
lst[0]=23
print(lst)

ddd=dict()
ddd['age']=21
ddd['course']=182
print(ddd)
ddd['age']=23
print(ddd)

# Dictinary Literals
jjj={'chuck':1,'fred':42,'jan':100}
print(jjj)

ooo={}
print(ooo)

ccc=dict()
ccc['csev']=1
ccc['cwen']=1
print(ccc)

ccc['cwen']=ccc['cwen']+1
print(ccc)

ccc=()
print(ccc['csev'])

print ('csev' in ccc) # 字典中也可以使用 in 操作符，in 可以使用在 string, list, dictionary 中

# 使用字典来计数列表中元素的出现次数

counts=dict()
names=['csev','cwin','csev','zqian','cwen']
for name in names:
    if name not in counts:  #要考虑是否已经在字典中出现了，如果没出现，就新加一个key进去，如果存在了，那就对此key的value加一
        counts[name]=1
    else:
        counts[name]=counts[name]+1
print(counts)

# 字典的built-in函数
names=['csev','cwin','csev','zqian','cwen']

for name in names:
    if name in counts:
        print(counts[name])
    else:
         print(0)
    print(counts.get(name,0))


#使用get()来简化字典计数
counts=dict()
names=['csev','cwin','csev','zqian','cwen']
for name in names:
    counts[name]=counts.get(name,0)+1
print(counts)


# 文本计数
counts=dict()
print('Enter a line of text:')
line=input('')

words=line.split()
print('Words:',words)

print ('Counting...')
for word in words:
    counts[word]=counts.get(word,0)+1
print('Counts:',counts)

# 在字典中循环

counts={'chuck':1,'fred':42,'jan':100}
for key in counts:
    print(key,counts[key])


# Retrieving lists of keys and values(Retrieving n.检索（过程），取还; v.恢复; 取回( retrieve的现在分词 ); 寻回; 检索)
jjj={'chuck':1,'fred':42,'jan':100}
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())

# Bonus:Two iteration variables!
jjj={'chuck':1,'fred':42,'jan':100}
for aaa,bbb in jjj.items():
    print(aaa,bbb)

# 最开始的程序
name=input('Enter file:')
handle=open(name,'r')
text=handle.read() #读入成为string
words=text.split() #分割siring成为list，去掉所有空格和换行，纯粹全部是单词

counts=dict()
for word in words:
    counts[word]=counts.get(word,0)+1


bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count
print(bigword,bigcount)







