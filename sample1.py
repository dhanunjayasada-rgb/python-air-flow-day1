fo=open('sample_file.txt','r')
fdtls=fo.read()
fo.seek(0)
frdlns=fo.readlines()
print(fdtls)
print(frdlns)
#print(fo.read())

""""
x=10
while x>0:
    if x==0:
        break
    else:
        print(x)
        x-=1
print('bye')


my_name='dhanu'
sur_name='sada'
print(my_name)
print('hi',my_name,'welcome')
print('hi '+my_name+' welcome')
print(f'hi {my_name} {sur_name}')
print(f'my name is {my_name} sur_name {sur_name}')

new_var=input('Enter your name:')
new_num=input(f'Hello {new_var} what is your fav number ? : ')
print(f'Hey {new_var} , i understood your fav number is {new_num} ')

# mutable
var1 = 10
print(id(var1))
var2 = 10
print(id(var2))
# immutable
mylist = [1, 2, 3]
print(id(mylist))
mylist1 = [1, 2]
print(id(mylist1))

# dir -->  display all properties of modules

var1 = input('Enter no var1:')
var2 = input('Enter no var2:')
print(f'sum of {var1} and {var2} is {var1 + var2}')
print(f'sum of {var1} and {var2} is ', int(var1) + int(var2))

var3 = eval(input('Enter no var3:'))
# print(var3)

a = 'hell\'o'
print(a)
b = 'hel\n0'
print(b)
c = 'hel\tlo'
print(c)

str = ["this", "s", "india"]
print(type(str))
var = " # ".join(str)
print(var)
print(type(var))

str.split('s')

str.split(' ')
print(str[0:3])
print(str[:3])
print(str[3:])
print(str[:])
print(str[0:-3])
print(str[0:-1:3])


# for loop syntax and example

my_list = [1, 2, 3,"a","b"]
print(len(my_list))
my_list[1]=10 #replace
print(my_list)

my_list.index('a')
my_list.insert(1, 'a')
print(my_list)

my_list.append('a')
print(my_list)
my_list.extend(['d','r'])
print(my_list)
#my_list.remove('a')
print(my_list)
my_list1=my_list.copy()
print(my_list)
print(id(my_list))
print(id(my_list1))
my_list1.pop()
print(my_list1)

my_list1.sort()
print(my_list1)
my_list1.index('a',4)

my_list2=[]
for i in my_list:
    my_list2.append(str(i)+)
    print(my_list2)

for i in my_list:
    print(i)

x=(1)
x1=(1,0)
x2=(1,2,3)
x3=11,12,13
print(x)
print(x1)
print(x2)
print(x3)
print(type(x))
print(type(x1))
print(type(x2))
print(type(x3))

emp_data={100:'dhanu',102:'abc',103:'dr'}
print(emp_data)
for i in emp_data:
    print(i)
    print(i,emp_data[i])

emp_date = {100: ['dhanu','DW'], 102: ['abc','tem'], 103:['dr','lr']}
print(emp_date)
for i in emp_date:
    print(i)
    print(i, emp_date[i])
    print(i, emp_date[i][1])

y=[1,2,(100,200,300),['abc','dr','lr']]
print(y)
z=y[2]
print(z)
y[3][-2]='sd'
print(y)
print(y[2][1])
#y[2][1]=400 #not replace values in the tuple object
y[2]=(400,500)
print(y)

y1={1:(10,'abc'),2:(20,'def'),3:(30,'ghi')}
for i,j in y1.items():
    print(i,j)

y1.update({2:(40,'jkl')})
print(y1)

a1={10,20,30,40}
a2={20,10,50,60}
print(a1.union(a2))
print(a1.intersection(a2))
print(a1.difference(a2))
print(a1.symmetric_difference(a2))
print(a1.issubset(a2))
print(a1.issuperset(a2))
print(a1)


x=int(input('enter x value:'))
y=int(input('enter y value:'))
print(x,y)
print(f'Sum of {x} and {y} is {x+y}')
print(f'min of {x} and {y} is {min(x,y)}')
print(f'max of {x} and {y} is {max(x,y)}')
print(f'difference of {x} and {y} is {x-y}')
print(f'product of {x} and {y} is {x*y}')
print(f'quotient of {x} and {y} is {x//y}')
print(f'modulo of {x} and {y} is {x%y}')
print(x<y)
print(x>y)
print(x==y)
print(x!=y)
print(x>y or x<y)
print(x==y and y==x)
print(x is y)
print(x is not y)
print(id(x) is id(y))

d=int(input('enter d value:'))
r=int(input('enter r value:'))
if d==r:
    print('inside if ok')
    print('inside if ok')
print('bye')


d=int(input('enter d value:'))
r=int(input('enter r value:'))
if d==r:
    print('inside if ok')
else:
    print('inside else ok')
print('starting second if')
if d is r:
    print('inside second if ok')
    if r != d:
        print('inside d==r if ok')
else:
    print('inside second else ok')
print('bye')
"""