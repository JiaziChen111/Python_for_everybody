# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 01:18:51 2016

@author: songxf
"""

hour=input('Enter hours you worked:')
try:
    hour=int(hour)
    rate=input('Enter your wage rate:')
    try:
        rate=int(rate)
        print(hour*rate)
    except:
        print('Error,please enter numeric input')
except:
    print('Error,please enter numeric input')
    

    