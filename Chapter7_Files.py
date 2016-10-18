# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 15:49:44 2016

@author: songxf
"""
"""

首先，我们学习文本文件的读写。这里的文本文件是指我们在文本编辑器中创建的。然后，我们会了解如何与数据库文件进
行交互，例如，二进制文件，通过数据库软件进行读写。

"""

#得到当前工作路径present working directory
#pwd

#将工作路径导向mbox.txt文档所在区域

# cd E:/Programing/Python/Python_for_everybody

fhand=open('mbox.txt','r')

#另起一行特殊字符,the newline character
stuff='Hello\nWorld'
stuff
print(stuff)
stuff='X\nY'
print(stuff)
len(stuff)

xfile=open('mbox.txt')
for cheese in xfile:
    print (cheese)

fhand=open('mbox.txt')
count=0
for line in fhand:
    count=count+1
print ('Line count:',count)

fhand=open('mbox.txt')
inp=fhand.read()
print(len(inp))
print(inp[:20])


#Searching through a file

fhand=open('mbox.txt')
for line in fhand:
    if line.startswith('From:'):
        print(line)


#print函数自动在每行前面加一行
fhand=open('mbox.txt')
for line in fhand:
    line=line.rstrip() #strip()函数会将空格和换行都视为空格来去掉
    if line.startswith('From:'):
        print(line)

#skipping with continue，continue直接回到for的位置执行代码
fhand=open('mbox.txt')
for line in fhand:
    line=line.rstrip()
    #skipping uninteresting line
    if not line.startswith('From:'):
        continue  #continue直接回到for的位置执行代码
    print(line)

#使用  in 来选择行，unsing in to select lines
fhand=open('mbox.txt.')
for line in fhand:
    line=line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)

##
fname=input('Enter the file name:')
fhand=open(fname)
count=0
for line in fhand:
    if line.startswith('Subject:'):
        count=count+1
print('There were',count,'subject line in',fname)


## Open file with try,打开文件带Try
fname=input('Enter the file name:')
try:
    fhand=open(fname)
    count=0
    for line in fhand:
        if line.startswith('Subject:'):
            count=count+1
    print('There were',count,'subject line in',fname)
except:
    print('File cannot be opened:',fname)
