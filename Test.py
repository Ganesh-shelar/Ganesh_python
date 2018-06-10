"""
This file cvers following topics
1. tuples, set, bool dta type
2. conditional stmt
3. loops
4. break & cntinue
"""

# tuples- use for storing column names

my_tuple = ('a', 'b', 'c')
my_list = ['a', 'b', 'c','s','a']
my_set=set(['a','b'])
print(my_set)
print(type(set(my_list)),set(my_list))
UNIQUE_CHAR=list()

#first=int(input("enter a number"))
#for item in range(11,0,-1):
 #   print(item)
x=0;
while True:
    if x ==  11:
        break
    print(x)
    x += 1

for item in my_list:
    if item in UNIQUE_CHAR:
        continue
    UNIQUE_CHAR.append(item)

print(type(UNIQUE_CHAR),UNIQUE_CHAR)

if type(my_list) is list:
    print("this is list")

my_list2=list()

def this_func():
    return True

def func_1():
    print("func 1")

def func_2():
    print("func 2")

def func_3():
    print("func 3")

my_functions=[
    func_1,#0
    func_2,#1
]

my_functions_key={
'org':func_1()
}

my_functions[1]()
if this_func():
    print("this is func")
if my_list:
    print(("this is list"))
if my_list2:
    print("this is list 2")
elif this_func():
    print("this is func")
else:
    print("blank list")
'''
USR_DATA ={
    "Parth": {'Parth', 'Pune'}
}
# single line cmment

multi line cmment
'''
print('hello')

'''
class MyClass(object):
    def _init_(self):

def function_function():
  '''


'''
1) print maximum value from 2 variables
2) print minimum value frm 2 variables
3) print maximum value from 10 variables without using built in functions 
4) print minimum value from 10 varibales without using built in functions
'''