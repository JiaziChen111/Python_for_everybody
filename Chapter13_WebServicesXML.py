# -*- coding: utf-8 -*-
"""
Created on  5:28 2016/10/2

author  songxf
"""

#cd E:\Programing\Python\Python_for_everybody

# xml1.py
import xml.etree.ElementTree as ET

data = '''
<person>
	<name>Chuck</name>
	<phone type="intl">
 		+1 734 303 4456
	</phone>
	<email hide="yes"/>
</person>
'''

# 三个英文单引号，不是一个双引号加一个单引号！

tree = ET.fromstring(data)  # 调用fromstring将XML的字符串表示转换成一颗XML节点树，当XML被视为一棵树，我们有一系列方法来抽取XML中数据片段
print('Name:', tree.find('name').text)  # 在节点树中找到name，并返回其中包括的文本
print('Attr:', tree.find('email').get('hide'))  # 在节点树中找到email，并使用method get得到hide的值

# xml2.py

import xml.etree.ElementTree as ET

data = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
            </user>
        </users>
</stuff>'''

stuff = ET.fromstring(data)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))




