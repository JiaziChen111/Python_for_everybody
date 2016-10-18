# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 03:25:00 2016

@author: songxf
"""

"""

Chapter Eleven Regular Expressions Assigment 

"""

cd E:\Programing\Python\Python_for_everybody

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
