# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 20:43:01 2016

@author: songxf
"""

astr="Hello Bob"
try:
    istr=int(astr)
except:
    istr=-1
print('First',istr)    

astr='123'
try:
    istr=int(astr)
except:
    istr=-1

print('Second',istr)