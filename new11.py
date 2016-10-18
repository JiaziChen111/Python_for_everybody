# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 20:48:00 2016

@author: songxf
"""

rawstr=input('Enter a number:')

try:
    ival=int(rawstr)
except:
    ival=-1
    
if ival>0:
    print('Nice work')
else:
    print('Not a number')
    
