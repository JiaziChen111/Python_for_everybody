# -*- coding: utf-8 -*-
"""
Created on  3:47 2016/10/5

author  songxf
"""

import json

pu= '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]'''

info = json.loads(pu)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print ('Id', item['id'])
    print ('Attribute', item['x'])
