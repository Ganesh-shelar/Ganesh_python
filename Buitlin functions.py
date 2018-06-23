"""
Butil in fns-min,max,count,len,spilt,zip,type,sum , sorted
builtin modules:os,sys,re,datetime,glob,math,time
types of fns
function parameter

"""
'''''''''''''''''''''''
Built in functions
'''''''''''''''''''''''
numbers=[1,2,3,4,5]
print(min(numbers))
print(max(numbers))

print(numbers.count(5))

_string =" This is what we want. why we here"

print(_string.count("we",20,50))

print(len(numbers))
print(len(_string))

numbers_2=[item for item in range(0,100)]
print(_string.split(' '))
#slicing
print((_string[0:4]))
print((numbers_2[0:50:2]))

print(_string[::-1])
print(numbers_2[::-1])

print(_string.replace('we','i',1))

x=['a','b','c']
y=[1,2,3]

#for x_item,y_item in zip(x,y)
#    print(F:x_item(y_item))

my_dictionary={'parth':100,'ravi':'1000',
               'srikant':{
                'class':1000
                },
                'ganesh':[10,20,'30',40]
               }

print(sum(y))

print(",".join(x))


print(sorted(numbers,reverse=True))


'''
2) Built in modules
os,sys,re,datetime,glob,math,time

import os
print(os.path.abspath(os.curdir))
print(os.uname())
os.environ['Today']="Saturday"
'''
'''
#print(os.environ)
##for i in os:

#####
#3) Types of function
####----Built in function
# ---user defined function
'''
"""
def <function/method name>:
    '''doc string'''
    return None
"""

def greetings(person):
    print("Hello there.")
    print(F"Hello {person}.")
    greeting_msg = "hello"
    return greeting_msg

greet=greetings(person='Parth')
print(greet)

def _addition(*args,**kwargs):
    """

    :param args:
    :return:
    """
    total=sum(args)
    greeting=[greetings(value) for value in kwargs.values()]

    return total, greetings('parth')

#print(_addition(1,2,3,4))
#print(_addition(*numbers))
total, greet=_addition(*numbers,**{'dept': 'parth', 'abc': 'Ganesh'})
print(total)
'''
#----Closer function
#----Recursive function
#----Anonymous function
#----Async function
'''




