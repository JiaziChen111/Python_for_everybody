# -*- coding: utf-8 -*-
"""
Created on  16:45 2016/10/15

author  songxf
"""

class PartyAnimal:
	x=0

	def __init__(self):
		print('I am constructed')

	def party(self):
		self.x=self.x+1
		print('So far',self.x)

	def __del__(self):
		print('I am destructed',self.x)

an=PartyAnimal()
an.party()
an.party()
an.party()