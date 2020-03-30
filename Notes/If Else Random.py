Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
#IF and else statements, to execute different functions depending on condition
>>> dank = 5
>>> if dank > 2: print("dank af")
else: print("not so dank")

dank af
>>> #use, >,<,= to check the truth
>>> dank < 6
True
>>> dank >  1
True
>>> dank < 2
False
>>> #can store the boolean as a variable
>>> x = dank < 6
>>> x
True
>>> #True = 1, False = 0
>>> print(int(True))
1
>>> #can convert boolean to floats to string too
>>> print(str(True))
True
>>> print(float(True))
1.0
>>> ### cut off
>>> #any number that isnt 0, will return True
>>> boolean(0)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    boolean(0)
NameError: name 'boolean' is not defined
>>> bool(0)
False
>>> bool(0.1)
True
>>> bool(-100)
True
>>> #Can add booleans to integers
>>> x=True
>>> x+6
7
>>> #Adding a float to an int will convert value to float
>>> 2.0 + 7 + x
10.0
>>> #Permanently Converting numbers
>>> x = 69
>>> x = float()
>>> x
0.0
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #Generating random  numbers
>>> # randint(a,b) to generate from a to b
>>> #import random
>>> import random
>>> randint(0,115)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    randint(0,115)
NameError: name 'randint' is not defined
>>> random.randint(0,115)
106
>>> # == is a check to see if answers match
>>> x = 6
>>> y=7
>>> x == y
False
>>> y = 6
>>> x == 6
True
>>> #FOR INTEGERS
>>> #randint (a,b) can produce a-b including a and b
>>> #randrange(a,b) can produce a-b excluding b including a
>>> #FOR FLOATS
>>> #random() can producefrom 0.0 to 1.0 exlude 1
>>> #uniform(a,b) produces a-b exludes b
>>> 
>>> 
>>> 
>>> 
>>> #If Statements
>>> #one way and nested
>>> #If else statements
>>> #two way and multiway if-elf-else
>>> 
>>> 
>>> #If requires tabs to be included
>>> x =6
>>> if x >3
SyntaxError: invalid syntax
>>> if x >3:
	print("dankaf")
	("its no use")

	
dankaf
'its no use'
>>> #Using eli
>>> #elif*
>>> x = 6
>>> y = 6
>>> z = 6
>>> if x ==6:
	print("dank")
elif y==6:
	print("y is dank")
elif z==6:
	print("z is dank")

	
dank
>>> x  = 7
>>> z = 7
>>> if x ==6:
	print("dank")
elif y==6:
	print("y is dank")
elif z==6:
	print("z is dank")

	
y is dank
>>> #It will do the first operation it satisfies
>>> #EXAMPLE 1: x met condition so "dank"
>>> #EXAMPLE 2: y met it before z so its "y is dank"
>>> if x ==6, z == 6:
	
SyntaxError: invalid syntax
>>> if x ==6:
	print("dank")
else:print("not dank")
elif y==6:
	print("y is dank")
elif z==6:
	print("z is dank")
	
SyntaxError: invalid syntax
>>> #not, and, or will combine multiple arguments logically
>>> if x==7 and z==7:
	print("both are dank")

	
both are dank
>>> #can be used in order of operations
>>> # x and (y or z)
>>> # x and not(y and z)
>>> 
>>> # not is the same as !=
>>> x != 7
False
>>>  #Can use to assign and pick values
>>> a = 6
>>> b = 5
>>> max = a if a>b else b
>>> max
6
>>> #order of operations
>>> """
1. Unary 
2. Exponents
3. Pemdas
4. Comparison
5. Equality
6. And
7. Or
8. Self Assigning Operators"""
'\n1. Unary \n2. Exponents\n3. Pemdas\n4. Comparison\n5. Equality\n6. And\n7. Or\n8. Self Assigning Operators'
>>> #Operators
>>> #binary operations from left to right
>>> 5 + 6 -7 + 8
12
>>> #(((5+6)-7)+8)
>>> 
>>> 
>>> #Self Assigning Operators from right to left
>>> x=z=y=6
>>> x
6
>>> #(x=(z=(y=6)))
>>> 
