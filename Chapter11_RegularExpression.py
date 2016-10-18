# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 20:32:24 2016

@author: songxf
"""

"""

Chapter Eleven Regular Expressions

"""

cd
E:\Programing\Python\Python_for_everybody

hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if line.find('From:') >= 0:
		print(line)

import re

hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if re.search('From:', line):  # re.search()返回一个True or False的值
		print(line)

hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if line.startswith('From:'):
		print(line)

import re

hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if re.search('^From:', line):  # re.search('^From:',line)在line的开头找From:,看line是否以From:开头
		print(line)

import re

x = 'my 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)  # 使用re.findall()来返回匹配的字符串，得到的是一个python列表
print(y)
y = re.findall('[AEIOU]+', x)
print(y)

# 警告： Greedy matching，贪婪匹配，返回最长的合法字符串

import re

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
# Non-Greedy Matching

import re

x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)

# Fine Tuning String Extraction

import re

x = 'From stepehn.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('\S+@\S+', x)
print(y)

# 在正则表达式中使用括号，括号内部的内容是我们提取的返回字符串

import re

hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if re.search('^From ', line):
		y = re.findall('^From (\S+@\S+)', line)
		print(y)

# 使用一般的Python语言实现提取域名
# 方式一
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if line.startswith('From '):
		atpos = line.find('@')
		sppos = line.find(' ', atpos)
		host = line[atpos + 1:sppos]
		print(host)

# 方式二
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if line.startswith('From '):
		words = line.split()
		email = words[1]
		pieces = email.split('@')
		print(pieces[1])

# 使用正则表达式提取域名
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if re.search('^From ', line):
		y = re.findall('@([^ ]*)', line)
		print(y)
		print(y[0])

import re

lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)', lin)
print(y)

# Spam Confidence

import re

hand = open('mbox-short.txt')
numlist = list()
for line in hand:
	line = line.rstrip()
	stuff = re.findall('X-DSPAM-Confidence: ([0-9.]+)', line)
	if len(stuff) != 1: continue
	num = float(stuff[0])
	numlist.append(num)
print('maximum:', max(numlist))

# Escape Character

import re

x = 'We just received $10.00 for coookies'
y = re.findall('\$[0-9.]+', x)
print(y)

import re

hand = open('regex_sum_315332.txt ')
lst = list()
for line in hand:
	line = line.rstrip()
	num = re.findall('[0-9]+', line)
	for number in num:
		number = int(number)
		lst.append(number)
print(sum(lst))
