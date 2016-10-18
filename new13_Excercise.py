# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 21:02:40 2016

@author: songxf
"""
hour=input('Enter hours you worked:')
#rate=input('Enter your wage rate:')
try:
    hour=int(hour)
except:
    hour=-1

if hour>0:
    print('Nice work')
    if hour<=40:
        print('You get pay:',hour*10)
    elif hour>40:
        print('You get pay:',40*10+(hour-40)*15)
    
else:
    print('Error,please enter a numeric input')


