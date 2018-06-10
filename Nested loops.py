"""
This covers following topics
. nested loops
2 control looping
. comprehension
"""

'''
nested loops
create pattern using for a while loop
'''

for item in range(0,5):
    for item2 in range(0,5):
        print(item, end=' ')
    print(end='\n')


'''
assignment
1.
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *

2.
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1

3.
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0

4.
0
1 0
0 1 0
1 0 1 0
0 1 0 1 0

5. 
1
1 0
1 0 1
1 0 1 0
1 0 1 0 1

6.
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

7.
01 02 03 04 05
06 07 08 09 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25

8.
1 0 1 0 1
0 1 0 1
1 0 1
0 1
1

9.
      1
    1   1
  1   1   1
1   1   1   1

10.
* *    * *
*  *  *  *
*   *    *
*        *
*        *


11.
01 02 03 04 05
05 04 03 02 01
02 04 06 08 10
10 08 06 04 02
03 06 09 12 15
15 12 09 06 03

12.
2
2 4
2 4 8
2 4 8 16
2 4 8 16 32
2 4 8 16 32 64

  

'''

'''
control looping
'''

for item in range(0, 30):
    if item % 3==0 :
        print("Fiz")
    elif item%5==0:
        print("Buz")
    elif item%15==0:
        print("FizBuz")
    else:
        print(item)

'''
comprehensin
'''

new_power= [
    pow(2, item) for item in range(1,7)
]
print(new_power)


#odd numbers

new_odd= [
   item for item in range(1,7) if item % 2 == 1
]
print(new_odd)


_power = dict()

_new_power = {
    item : pow(item, item) for item in range(0,10)
}
print("power")
print(_new_power)

