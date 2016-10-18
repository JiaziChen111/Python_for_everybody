# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 01:54:54 2016

@author: songxf
"""


try:
    hour=input('Enter hours you worked:')
    hour=float(hour)
    rate=input('Enter your wage rate:')
    rate=float(rate)
    if hour<=40:
        print('You get pay:',hour*rate)
    else:
        print('You get pay:',40*rate+(hour-40)*1.5*rate)
except:
    print('Error,please enter a numeric input')
    #quit()



