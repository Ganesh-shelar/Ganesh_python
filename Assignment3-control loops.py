"""
This file covers below
"""
'''
assignment
1.
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
print( end='\n')
print("     First")
for item in range(0,5):
    for item2 in range(0,5):
        print("*", end=' ')
    print( end='\n')



'''
2.
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
'''
print( end='\n')
print("     Second")
for item in range(0,5):
    for item2 in range(0,5):
        print("1", end=' ')
    print( end='\n')

'''
3.
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
'''
print( end='\n')
print("     Third")

for item in range(0,5):
    for item2 in range(0,5):
        if item % 2 == 0:
            print("0", end=' ')
        else:
            print("1", end=' ')

    print( end='\n')

'''
4.
0
1 0
0 1 0
1 0 1 0
0 1 0 1 0
'''
print( end='\n')
print("     Fourth")
for item in range(0,5):
    for item2 in range(0,5):
        if item2 <= item:
            if (item + item2) % 2 == 0:
               print("0", end=' ')
            else:
               print("1", end=' ')

    print( end='\n')


'''
5. 
1
1 0
1 0 1
1 0 1 0
1 0 1 0 1
'''
print( end='\n')
print("     Fifth")
for item in range(0,5):
    for item2 in range(0,5):
        if item2 <= item:
            if item2 % 2 == 0:
               print("1", end=' ')
            else:
               print("0", end=' ')

    print( end='\n')
'''
6.
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''
print( end='\n')
print("     Sixth")
for item in range(1,6):
    for item2 in range(1,6):
        print(item2, end=' ')
    print( end='\n')

'''

7.
01 02 03 04 05
06 07 08 09 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25

'''
print( end='\n')
print("     Seventh")
index=0
for item in range(0,5):
    for item2 in range(0,5):
        index=index+1
        print("{:0>2d}".format(index),end=' ')
    print(end='\n')
'''
'''

'''
8.
1 0 1 0 1
0 1 0 1
1 0 1
0 1
1
'''

print( end='\n')
print("     Eighth")
for item in range(0,5):
    for item2 in range(5,0,-1):
        if item < item2:
            if (item + item2) % 2 == 0:
               print("0", end=' ')
            else:
               print("1", end=' ')

    print( end='\n')

'''
9.
      1
    1   1
  1   1   1
1   1   1   1


'''
print( end='\n')
print("     Ninth")

strPtn = ""
iMax = 5
jMax = 5

for i in range(0,iMax+1):
    strPtn=""
    iSpacesCount = (iMax - i) * 2
    for j in range(0, jMax+1):
        if j <= i:
            if j == 0:
                for k in range(0,iSpacesCount):
                    strPtn = strPtn + " "
            else:
                strPtn = strPtn + "1  "
        else:
            break
    '''strPtn = strPtn + "\n"
    '''
    print(strPtn)
'''

10.
* *    * *
*  *  *  *
*   *    *
*        *
*        *
'''
print( end='\n')
print("     Tenth")
iNoOfRows = 9
iRowsWithMiddleStars = round((iNoOfRows/2)+0.1)
iMiddleLastRowSpaces = iNoOfRows-1
iTopRowSpaces = (iNoOfRows * 2)- 1
iRowInitilSpces=0
iRowMiddlespces=0
iRowLstSpces=0
Mshape=""

for iRowsIndex in range( 0, iNoOfRows):
    if iRowsIndex == 0 or iRowsIndex >= iRowsWithMiddleStars:
        Mshape = ""
        Mshape = Mshape + "*"
        for i in range( 0, iTopRowSpaces):
             Mshape = Mshape+ " "
        Mshape = Mshape + "*"
        print(Mshape)
    elif iRowsIndex < (iRowsWithMiddleStars-1):
        Mshape = ""
        if iRowsIndex == 1:
            iRowInitilSpces = 2
            iRowLstSpces = 2
        else:
            iRowInitilSpces = iRowInitilSpces + 2
            iRowLstSpces = iRowLstSpces + 2

        iRowMiddlespces = iTopRowSpaces - iRowInitilSpces - iRowLstSpces - 2
        Mshape = Mshape + "*"
        for i in range(0,iRowInitilSpces):
            Mshape = Mshape + " "
        Mshape = Mshape + "*"
        for i in range(0,iRowMiddlespces):
            Mshape = Mshape + " "
        Mshape = Mshape + "*"
        for i in range(0,iRowLstSpces):
            Mshape = Mshape + " "
        Mshape = Mshape + "*"
        print(Mshape)
    elif iRowsIndex == (iRowsWithMiddleStars - 1):
        Mshape = ""
        Mshape = Mshape + "*"
        for i in range(0, iMiddleLastRowSpaces):
            Mshape = Mshape + " "
        Mshape = Mshape + "*"
        for i in range(0, iMiddleLastRowSpaces):
            Mshape = Mshape + " "
        Mshape = Mshape + "*"
        print(Mshape)


'''
//*         * 9=TopRowSpaces=(rows*2)-1
//*  *   *  * 2 3 2=(rows/2) ex. if 2.5 then 2;
//*    *    * 4 4=MiddleLastRowSpaces=rows-1
//*         * 9
//*         *

//*           * 11
//*  *     *  * 2 5 2
//*     *     * 5 5
//*           * 11
//*           *
//*           *

//*             * 13
//*  *       *  * 2 7 2
//*    *   *    * 4 3 4
//*      *      * 6
//*             * 13
//*             *
//*             *

//*             * 13
//*  *       *  * 2 7 2
//*    *   *    * 4 3 4
//*      *      * 6
//*             * 13
//*             *
//*             *

11.
01 02 03 04 05
05 04 03 02 01
02 04 06 08 10
10 08 06 04 02
03 06 09 12 15
15 12 09 06 03

'''
print( end='\n')
print("     eleventh")
for item in range(1,4):
    for i in range(1,6):
        print("{:0>2d}".format(i * item), end=' ')
    print(end='\n')

    for j in range(5,0,-1 ):
        print("{:0>2d}".format(j * item), end=' ')
    print(end='\n')


'''

12.
2
2 4
2 4 8
2 4 8 16
2 4 8 16 32
2 4 8 16 32 64
'''
print( end='\n')
print("     Twelveth")
for item in range(1,7):
    for item2 in range(1,7):
        if item2 <= item:
            print(pow(2,item2),end=' ')
    print( end='\n')

