import pandas as pd

data = {
    "RollNo": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Percentage": [85, 72, 91],
    "Grade": ["A", "B", "A+"]
}
df = pd.DataFrame(data)
df.to_csv("sample.csv", index=False)
print("sample.csv created successfully!")
df = pd.read_csv("sample.csv")
print(df)


"""
#keyword arguments
def f1(x,y):
    print(x,y)
def intro(name,city,job):
    print(f'My name is {name}, and I am from {city}, and I am  {job}')
    f1(10,20)
intro(name='dhanu',job='sql developer',city='nellore')



def f1(x,y):
    print(x,y)
f1(y=30,x=15)


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