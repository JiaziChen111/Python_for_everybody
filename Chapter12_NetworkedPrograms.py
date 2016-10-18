# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 03:43:14 2016

@author: songxf
"""
"""

Chapter Twelve Networked Programs

"""

# cd E:\Programing\Python\Python_for_everybody

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))

# An HTTP Request in Python

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))

mysock.sendfile('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
	data = mysock.recv(512)
	if (len(data) < 1):
		break
	print(data)
mysock.close()

# Urllib
import urllib.request

fhand = urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in fhand:
	print(line.rstrip())

import urllib.request

fhand = urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt')

counts = dict()
for line in fhand:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word, 0) + 1
print(counts)

# Understanding HTML
import urllib.request

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
	print(line.strip())

# Parsing HTML with BeautifulSoup
import urllib
from bs4 import BeautifulSoup

url = input('Enter-')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html)
# soup=BeautifulSoup(html,"lxml")

tags = soup('a')
for tag in tags:
	print(tag.get('href', None))

# 阅读教材 Python for informatics
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n'.encode())

while True:
	data = mysock.recv(512)  # 从套接字中接受512个字符的数据片段
	if (len(data) < 1):
		break
	print(data)

# 通过HTTP检索图像

import socket
import time

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send(b'GET http://www.py4inf.com/cover.jpg HTTP/1.0\n\n')

count = 0
picture = ""
picture = picture.encode()
while True:
	data = mysock.recv(5120)
	if (len(data) < 1): break
	time.sleep(0.25)
	count = count + len(data)
	print(len(data), count)
	picture = picture + data
mysock.close()

# Look for the end fo the header(2 CRLF)
picture = str(picture)
pos = picture.find("\r\n")
print('Header length', pos)
print(picture[:pos])

# Skip past the header and save the picture data
picture = picture[pos + 4:]
fhand = open("stuff.jpg", "wb")
picture = picture.encode()
fhand.write(picture)
fhand.close()

"""
使用urllib检索网页
"""

import urllib.request

fhand = urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in fhand:
	line = line.decode()
	print(line.strip())

# 获取romeo.txt的数据，计算文件中每个单词的频率

import urllib.request

counts = dict()
fhand = urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in fhand:
	line = line.decode()
	words = line.split()
	for word in words:
		counts[word] = counts.get(word, 0) + 1
print(counts)

"""
解析HTML和Web抓取，使用正则表达式解析HTML
"""

"""
一个简单的网页源代码

<h1>The First Page</h1>
<p>
If you like, you can switch to the
<a href="http://www.dr-chuck.com/page2.htm">
Second Page</a>.
</p>
"""

"""
构造一个符合语法规则的正则表达式，匹配和抽取以上网页文本中的超链接，正则表达式如下：
href="http://.+?"

这个正则表达式查找一ref="http://”开头的字符串，之后是一个或者多个字符".+?"，
?表示以非贪婪方式进行匹配，而不是贪婪方式；
非贪婪方式试图找到最小可能匹配的字符串，贪婪匹配试图找到最大可能匹配的字符串
"""

import urllib.request
import re

url = input('Enter-')
linkregex = re.compile('<a\s*href=[\'|"](.*?)[\'"].*?>')
html = urllib.request.urlopen(url).read().decode()
# html=html.read().decode()
links = re.findall('href="(http://.+?)"', html)
for link in links:
	print(link)

"""
使用BeautifulSoup解析HTML


"""

import urllib.request
from bs4 import BeautifulSoup

url = input('Enter-')
html = urllib.request.urlopen(url).read().decode()
soup = BeautifulSoup(html)
tags = soup('a')
for tag in tags:
	print(tag.get('href', None))

# 使用BeautifulSoup取出每部分标签的不同部分，代码如下

import urllib.request
from bs4 import BeautifulSoup

url = input('Enter-')
html = urllib.request.urlopen(url).read().decode()
soup = BeautifulSoup(html, "lxml")
tags = soup('a')
for tag in tags:
	print('TAG:', tag)
	print('URL:', tag.get('href', None))
	print('Content:', tag.contents[0])
	print('Attrs:', tag.attrs)

"""
使用urllib读取二进制文件
"""
import urllib.request
from bs4 import BeautifulSoup

img = urllib.request.urlopen('http://www.py4inf.com/cover.jpg').read()
img = str(img)
# img=img.read()
fhand = open('cover.jpg', 'w')
fhand.write(img)
print(len(img))
fhand.close()

import urllib.request
from bs4 import BeautifulSoup

img = urllib.request.urlopen('http://www.py4inf.com/cover.jpg')
# img=img.read()
# img=str(img)
fhand = open('cover.jpg', 'w')
size = 0
while True:
	info = img.read(10000)
	info = str(info)
	if len(info) < 1: break
	size = size + len(info)
	fhand.write(info)
print(size, 'characters copied')
fhand.close()
