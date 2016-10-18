# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 12:35:10 2016

@author: songxf
"""
def hello():
    print('Hello')
    print('Fun')

hello()
print('Zip')
hello()


big=max('Hello world')
print(big)
tiny=min('Hello world')
print(tiny)

print( float(99)/100)

i=42 
type(i)

#def print_lyrics():
#    print("I'm a lumberjack, and I'm okay")
#    print("I sleep all night")
    
    
x=5
print('Hello')

def print_lyrics():
    print("I'm a lumberjack, and I'm okay")
    print("I sleep all night")
    
print('Yo')
x=x+2
print(x)

def greet1(lang):
    if lang=='es':
        print('Hola')
    elif lang=='fr':
        print('Bonjour')
    else:
        print('Hello')
        
        
        
def greet2(lang):
    if lang=='es':
        return 'Hola'
    elif lang=='fr':
        return 'Bonjour'
    else:
        return 'Hello'


print(greet2('en'),'Glenn')

print(greet2('es'),'Sally')

print(greet2('fr'),'Michael')




def addtwo(a,b):
    added=a+b
    return added

x=addtwo(3,5)
print(x)





