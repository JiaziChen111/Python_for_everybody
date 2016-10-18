# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 20:57:03 2016

@author: songxf
"""

hour=input('Enter hours you worked:')
hour=float(hour)

if hour<=40:
    print('You get pay:',hour*10)
elif hour>40:
    print('You get pay:',40*10+(hour-40)*15)