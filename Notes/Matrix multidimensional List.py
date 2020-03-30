Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
#Multidimensional list
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #matrixing
>>> matrix = [
	[1,2,3]
	[4,5,6]
	[7,8,9]
	]
Traceback (most recent call last):
  File "<pyshell#11>", line 3, in <module>
    [4,5,6]
TypeError: list indices must be integers or slices, not tuple
>>> matrix = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
	]
>>> 
>>> matrix
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> #This is a list within a list
>>> matrix[0]
[1, 2, 3]
>>> matrix[0][2]
3
>>> #can call just the row or the specific point
>>> matrix = [1,2,3,4,5,6,7,8,9]
>>> matrix
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> 
>>> 
>>> 
>>> #Should be initialized with rows and columns in mind
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #Shuffling
>>> #Method can only be used to shuffle singe dimensional indexs
>>> x = [1,2,3,4,5]
>>> import random
>>> random.shuffle(x)
>>> x
[1, 4, 3, 2, 5]
>>> #However we must code the swap method ourselves and randomize every single index
>>> #when copying multimensional arrays, the data will only copy the first layer
>>> #Refer the second
>>> y=x[:]
>>> #y now has the same first layer
>>> #if i change x,y will copy x becuase it is a shallow copy
>>> 
>>> 

>>> 
>>> 
>>> 

>>> #Multiplication creates shallow copies
>>> x = [1]*4
>>> x
[1, 1, 1, 1]
>>> y = x *4
>>> y
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
>>> x = 7
>>> y
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
>>> x = [7]
>>> y
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
>>> y[0][0]=7
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    y[0][0]=7
TypeError: 'int' object does not support item assignment
>>> y = [x] *4
>>> y
[[7], [7], [7], [7]]
>>> x = 8
>>> y
[[7], [7], [7], [7]]
>>> x=[8]
>>> y
[[7], [7], [7], [7]]
>>> y[0][0]=[8]
>>> y
[[[8]], [[8]], [[8]], [[8]]]
>>> #changes all of them
>>> matrix = [random.random]
>>> matrix
[<built-in method random of Random object at 0x103056e18>]
>>> matrix = [random.random()]
>>> 
>>> matrix
[0.28852300188512103]
>>> 
