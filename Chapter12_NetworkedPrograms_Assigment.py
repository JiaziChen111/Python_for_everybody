# -*- coding: utf-8 -*-
"""
Created on  3:26 2016/10/2

author  songxf
"""
# First Assigment

import urllib.request
from bs4 import BeautifulSoup

url = input('Enter-')
html = urllib.request.urlopen(url).read().decode()
soup = BeautifulSoup(html)

su = 0

tags = soup('span')

for tag in tags:
	a = tag.contents[0]
	a = int(a)
	su = su + a
print(su)

# Second Assigment

import urllib.request
from bs4 import BeautifulSoup

url = input('Enter URL:')
count = input('Enter count:')
count = int(count)
pos = input('Enter Position:')
pos = int(pos)

print('Retrieving:', url)
for i in range(count):
	html = urllib.request.urlopen(url).read().decode()
	soup = BeautifulSoup(html, "lxml")
	tags = soup('a')
	a = tags[pos - 1]
	url = a.get('href', None)
	print('Retrieving:', url)
