print('Hello world')
c=[1,2,3,4]
for a in c:
    print(a)

fhand=open('mbox-short.txt','r')
lst=list()
dct=dict()
for line in fhand:
    line=line.rstrip()
    if line.startswith('From '):
        line=line.split()
        lst.append(line[2])

for list in lst:
    dct[list]=dct.get(list,0)+1

print(dct)
