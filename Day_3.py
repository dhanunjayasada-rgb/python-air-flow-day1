x=10
def f1():
    global y
    y=20
    z=30
    print(x,y,z)
def f2():
    a=40
    print(a)
    print(x)
    print(y)
    #print(z)
f1()
f2()

"""
def test(x,y):
    x1=x+y
    y1=x-y
    return x1,y1
z=test(3,2)
print(z)

print('hi')
def f1():
    print('i am in f1')
f1()
print('bye f1')
def f2():
    print('i am in f2')
f2()
print('bye f2')
f1()
f2()
print('bye f1 and f2')


import re
with open('sample_file.txt','r') as fo:
    for i in fo:
        #if re.match('^\d+$',i):
        #if re.search('[6-9][0-9]{9}',i):
        #if re.search('^[6-9][0-9]{9}$', i):
        if re.search(r'\w+[@]\w+[.]\w+', i):
        #if re.search('cd',i):
            print(i,end='')
print('\nbye')

with open('sample_file.txt','r') as fo:
    x=fo.readlines()
    print(x)
    for i in x:
        print(i,end='')
    fo.seek(0)
    print('\n#######')
    y=fo.read()
    print(y)
    print(fo.tell())
print('bye')

with open('sample_file.txt','r') as fo:
    x=fo.readlines()
    print(x)
    for i in x:
        print(i,end='')
    fo.seek(0)
    print('\n#######')
    y=fo.read()
    print(y)
print('bye')
"""