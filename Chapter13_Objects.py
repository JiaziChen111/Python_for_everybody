# -*- coding: utf-8 -*-
"""
Created on  15:20 2016/10/15

author  songxf
"""

usf=input('Enter the US Floor:') #在Python3中input返回一个string，可使用int(some_string)将其转化成为一个整数

usf=int(usf)
wf=usf-1
print('Non-US Floor Number is',wf)



movies=list()
movie1=dict()
movie1['Director']='James Cameron'
movie1['Title']='Avatar'
movie1['Release date']='18 December 2009'
movie1['Running Time']='162 Minutes'
movie1['Rating']='PG-13'
movies.append(movie1)

movie2=dict()
movie2['Director']='David Fincher'
movie2['Title']='The Social Network'
movie2['Release date']='01 October 2010'
movie2['Running Time']='120 Minutes'
movie2['Rating']='PG-13'
movies.append(movie2)

print(movies)


keys=['Title','Director','Rating','Running Time']
print('-------------')
print(movies)
print('-------------')
print('keys')

for item in movies:
	print('------------')
	for key in keys:
		print(key,':',item[key])
print('-------------')


class PartyAnimal: #定义一个类
	x=0

	def party(self):
		self.x=self.x+1
		print('So far',self.x)
an=PartyAnimal() #使用定义的类来创建一个对象
an.party()
an.party()
an.party()

x=list()
type(x)
dir(x)


y='Hello there'
dir(y)

print('Type:',type(an))
print('Dir:',dir(an))

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


class PartyAnimal:
	x=0
	name=""
	def __init__(self,z):
		self.name=z
		print(self.name,'constructed')

	def party(self):
		self.x=self.x+1
		print(self.name,"party count",self.x)

s=PartyAnimal("Sally")
s.party()

j=PartyAnimal("Jim")
j.party()
s.party()

class FootballFan(PartyAnimal):
	points=0
	def touchdown(self):
		self.points=self.points+7
		self.party()
		print(self.name,'points',self.points)

s=PartyAnimal("Sally")
s.party()

j=FootballFan("Jim")
j.party()
j.touchdown()








