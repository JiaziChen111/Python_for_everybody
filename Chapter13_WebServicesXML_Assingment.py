# -*- coding: utf-8 -*-
"""
Created on  8:31 2016/10/3

author  songxf
"""

import urllib.request
import xml.etree.ElementTree as ET

html = "http://python-data.dr-chuck.net/comments_315334.xml"
#url=input('Enter location:')
print('Retrieving', html)
uh = urllib.request.urlopen(html)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
print(data)
tree = ET.fromstring(data)

su = 0
#方式一
results = tree.findall('comments/comment/count')
for result in results:
	a = result.text
	#assert isinstance(a, str)
	b = int(a)
	su = su + b
print('Sum', su)

#方式二

results = tree.findall('comments/comment')
for result in results:
	a = result.find('count').text
	#assert isinstance(a, str)
	b = int(a)
	su = su + b
print('Sum', su)


#方式三
results = tree.findall('comments/comment')
for result in results:
	a = result.find('count').text
	#assert isinstance(a, str)
	b = int(a)
	su = su + b
print('Sum', su)
