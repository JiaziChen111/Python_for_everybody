# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 14:27:36 2016

@author: songxf
"""

n=5
while n>0:
    print (n)
    n=n-1
print ('Blastoff')
print (n)



while True:
    line=input('>')
    if line=='done':
        break
    print(line)
print('Done')



while True:
    line=input('>')
    if line[0]=='#':
        continue
    if line=='done':
        break
    print('line')
print('Done')


for i in [5,4,3,2,1]:
    print(i)
print('Blastoff')


friends=['Joseph','Glenn','Sally']
for friend in friends:
    print('Happy new year:',friend)
print('Done!')



print('Before')
for thing in [9,41,12,3,74,15]:
    print(thing)
print('After')

largest_so_far=-1
print('Before',largest_so_far)
for the_num in [9,41,12,3,74,15]:
    if the_num>largest_so_far:
        largest_so_far=the_num
    print (largest_so_far,the_num)
print('After',largest_so_far)


zork=0
print('Before',zork)
for thing in [9,41,12,3,74,15]:
    zork=zork+1
    print(zork,thing)
print('After',zork)



count=0
sum=0
print('Before',count,sum)
for value in [9,41,12,3,74,15]:
    count=count+1
    sum=sum+value
    print(count,sum,value)
print('After',count,sum,sum/count)


print('Before')
for value in [9,41,12,3,74,15]:
    if value>20:
        print('Large number',value)
print('After')



found=False
print('Before',found)
for value in [9,41,12,3,74,15]:
    if value==3:
        found=True
    print(found,value)
print('After',found)




found=False
print('Before',found)
for value in [9,41,12,3,74,15]:
    if value==3:
        found=True
        print(found,value)
        break
    print(found,value)
print('After',found)




smallest_so_far=-1
print('Before',smallest_so_far)
for the_num in [9,41,12,3,74,15]:
    if the_num<smallest_so_far:
        smallest_so_far=the_num
    print (smallest_so_far,the_num)
print('After',smallest_so_far)


smallest_so_far=None
print('Before',smallest_so_far)
for the_num in [9,41,12,3,74,15]:
    if smallest_so_far==None:
        smallest_so_far=the_num
    elif the_num<smallest_so_far:
        smallest_so_far=the_num
    print (smallest_so_far,the_num)
print('After',smallest_so_far)






