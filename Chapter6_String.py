# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 00:17:17 2016

@author: songxf
"""
print('Hello world')


str1="Hello"
str2="there"

bob=str1+str2
print(bob)

str3='123'
str3=str3+1

x=int(str3)+1
print (x)


name=input('Enter:')
print(name)

fruit='banana'
letter=fruit[1]


fruit='banana'
print(len(fruit))

fruit='banana'
x=len(fruit)
print(x)


fruit='banana'
index=0
while index<len(fruit):
    letter=fruit[index]
    print(index,letter)
    index=index+1

fruit='banana'
for letter in fruit:
    print(letter)


word='banana'
count=0
for letter in word:
    if letter=='a':
        count=count+1
print(count)

s='Monty Python'
print(s[0:4]) #输出前四个元素，不包括[4],包括[0]-[3]
print(s[6:7])
print(s[6:20])

print(s[:2])
print(s[8:])
print(s[:])

#字符串连接
a='hello'
b=a+'there'
print(b)

c=a+' '+'there'

print(c)

#用in当作操作符

fruit='banana'
'n' in fruit

'm' in fruit

#字符串比较

word=input('Please enter word:')
if word=='banana':
    print ('all right,bananas.')

if word<'banana':
    print ('your word,'+word+',comes before banana.')
elif word>'banana':
    print('your word,'+word+',comes after banana.')
else:
    print('all right,bananas.')

##字符串库 有很多可以被字符串类型的对象调用的函数

greet='Hello Bob'
zap=greet.lower()
print(zap)
print(greet)
print('Hi There'.lower())

dir(greet)

#Search a string
fruit='banana'
pos=fruit.find('na')
print(pos)
aa=fruit.find('z')
print(aa)

#Upper case
greet='Hello Bob'
nnn=greet.upper()
print(nnn)
www=greet.lower()
print(www)

#search and replace
greet='Hello Bob'
nstr=greet.replace('Bob','Jane')
print(nstr)

greet='Hello Bob'
nstr=greet.replace('o','X')
print(nstr)

#Stripping Whitespace 去掉字符串开头或者结尾的空白格

greet='   Hello Bob '
greet.lstrip()
greet.rstrip()
greet.strip()

#Prefixes

line='Please have a nice day'
line.startswith('Please')
line.startswith('p')


data='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos=data.find('@')
print(atpos)

sppos=data.find(' ',atpos)#，找到@符号之后第一个空格所在的位置
print(sppos)

host=data[atpos+1:sppos]
print(host)

#格式操作符

camels=42
'%d' % camels #格式序列'%d'表示第二个操作对象会被格式化为整数型（d表示十进制）

camels=42
'I have spotted %d camels.' % camels

#'%d'格式化整数，'%g'格式化浮点数，'%s'格式化字符串
'In %d years, I have spotted %g %s' % (3,0.1,'camels')

'%d %d %d'%(1,2)
'%d'% 'dollars'

#调试
while True:
    line=input('>')
    if line[0]=='#': #什么都不输入，直接Enter就会出现bug
        continue
    if line=='done':
        break
    print(line)
print ('Done!')

while True:
    line=input('>')
    if len(line)>0 and line[0]=='#': 
        continue
    if line=='done':
        break
    print(line)
print ('Done!')

#术语
#计数器：用来统计的变量，通常初始化为零，然后递增
#空字符串：不包含字符、长度为零的字符串，用两个引号表示
#格式操作符：%操作符对格式字符串和元组进行操作，根据特定格式字符串，对元组元素进行格式化后生成一个字符串
#标记：用来表示条件是否为真的布尔变量。
#调用：方法的召唤语句。
#不可变：序列的一种属性，序列中的数据项不能被赋值。
#索引：用来选择序列中数据项的一个整数值，例如，表示字符串中的一个字符的位置。
#数据项：序列中的一个值。
#方法：与对象相关的函数，使用据点来调用。
#对象：变量可以引用的东西，现在，你可以交替使用“对象”或者“值”
#搜索：找到所要找的内容才会停止的一种遍历模式。
#序列：一个有序集合，集合中的每个值都通过一个整数索引定位。
#切片：根据索引区间制定字符串的一部分。
#遍历：遍历序列中的数据项，对每个数据项执行类似的操作。


#练习
str='X-DSPAM-Confidence: 0.8475'
a=str.find(':')
print(a)
b=str[a+1:]
type(b)
print(b)
c=float(b)
print(c,type(c))













