Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
# For Loops
>>> #Used when you know exactly how many times you want the program to run
>>> #For var in range(x,y)
>>> for v in range(4.8):
	print(v)

	
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    for v in range(4.8):
TypeError: 'float' object cannot be interpreted as an integer
>>> for v in range(4,8):
	print(v)

	
4
5
6
7
>>> for x in range(1,3):
	sum +=x
	print(sum)

	
Traceback (most recent call last):
  File "<pyshell#11>", line 2, in <module>
    sum +=x
TypeError: unsupported operand type(s) for +=: 'builtin_function_or_method' and 'int'
>>> for x in range(1,3):
	sum = 0
	sum = sum + x
	print(sum)

	
1
2
>>> #Prints from [x,y)
>>> 
>>> 
>>> #For loops  using strings
>>> for x in "fuckoff":
	print(x)

	
f
u

c
k
o
f
f
>>> #For loops use all the characters in a string as a single characer value
>>> 
>>> 
>>> 
>>> 
>>> #Using for loop list
>>> for x in (0,10,2):
	print(x)

	
0
10
2
>>> 


for x in range(0,10,2):
	print(x)

	
0
2
4
6
8
>>> #Use the third value to print in increments
