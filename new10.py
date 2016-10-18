# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 20:46:20 2016

@author: songxf
"""

astr='Bob'

try:
    print('Hello')
    istr=int(astr)
    print('There')
except:
    istr=-1
    
print('Done',istr)