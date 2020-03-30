Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
#FUNCTIONS
>>> #Used to carry out multiple lines by calling the function
>>> def main():#Define funtion Main as
	print("dank")
	print("sex")

	
>>> main()
dank
sex
>>> #executes the entire funtion
>>> def main (var1, var2) #Defines the function using these variables
SyntaxError: invalid syntax
>>> def main (var1, var2):#Defines the function using these variables
	var1 +=var2
	print(var1, var2)

	
>>> var1=6
>>> var2=7
>>> main()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    main()
TypeError: main() missing 2 required positional arguments: 'var1' and 'var2'
>>> main(5,6)
11 6
>>> def functionName ( Parameter1, Parameter2, Parameterx)
SyntaxError: invalid syntax
>>> 
>>> def functionName ( Parameter1, Parameter2, Parameterx):
	print("Function")

	
>>> functionName(45,45,45)
Function
>>> 
>>> 

>>> 

>>> 
>>> 

>>> 
>>> #Using return to store a value
>>> def weed(money, rate):
	return  money*rate
weedGrams = weed(54,10)
SyntaxError: invalid syntax
>>> def weed(money, rate):
	return  money*rate

>>> weedGrams = weed(54,10)
>>> print(weedGrams)
540
>>> #return will save it to the variable
>>> #when a value is not returned, it defaults to none
>>> def main():

dank = main()
SyntaxError: expected an indented block
>>> def main():
	a =6

	
>>> k = main()
>>> print(k)
None
>>> weed(54,10)
540
>>> #Functions can be added
>>> weedGrams = weed(54,10) + weed(40,5)#Different parameters
>>> print(weedGrams)
740
>>> #Its better to return becuase it will return a variable that can be used
>>> #printing doesnt do much
>>> eval(None)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    eval(None)
TypeError: eval() arg 1 must be a string, bytes or code object
>>> eval(None)
Traceback (most recent call last):


  File "<pyshell#63>", line 1, in <module>
    eval(None)
TypeError: eval() arg 1 must be a string, bytes or code object
>>> 
>>> 
>>> 
>>> 
>>> #IF multiple returns are executed in a function, it will end the function
>>> def main():
	return 5
	return 6

>>> x = main()
>>> print(x)
5
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #nPrintln
>>> nPrintln("a",3)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    nPrintln("a",3)
NameError: name 'nPrintln' is not defined
>>> 
>>> "ERROR"""
'ERROR'
>>> 
>>> 
>>> 
>>> 
>>> def main (var1, var2,var3):
	var1 += var2
	var1 += var3
	print(var1)

	
>>> main (1,2,3)
6
>>> main (var3= 3,var2=2, var1 = 1)
6
>>> #Python can allow you to directly give the value of each vairable
>>> #Doesnt even have to be in order
>>> 
>>> 
>>> 

>>> 
>>> 
>>> 
>>> 

>>> #Importing functions
>>> import random #imports random function
>>> random.random()
0.3875667085758935
>>> #calls function random() from file random
>>> from random import * # importing a specific function
>>> random
<built-in method random of Random object at 0x102040c18>
>>> random()
0.415427403690968
>>> #can now be specifically called without stating the name since it was only
>>> #imported from file
>>> #py files must be in the same directory
>>> 
>>> 

>>> 
>>> 
>>> 
>>> 

>>> #SCOPE of VARIABLES
>>> x = 69
>>> def main():
	x =420

	
>>> print(x)
69
>>> main
<function main at 0x113b06c80>
>>> main()
>>> print(x)
69
>>> #even thought the value of x is changed in the main(), it does not change
>>> #main() has created a new x
>>> 
>>> 
>>> x =69
>>> def main():
	global x =420
	
SyntaxError: invalid syntax
>>> def main():
	global x =420
	
SyntaxError: invalid syntax
>>> def main():
	global x =420
	
SyntaxError: invalid syntax
>>> def main():
	global x #will call the true global x
	x = 420

	
>>> print(x)
69
>>> main()
>>> print(x)
420
>>> #now x is changed when the function is called
>>> 
>>> 
>>> 
>>> 
>>> #DEFAULT ARGUMENTS
>>> 
>>> def main(x=5,z=6,c=7):
	print(x,z,c)

	
>>> main()
5 6 7
>>> #prints defaults
>>> 
>>> main(z=700)
5 700 7
>>> #prints defaults unless explicitly changed
>>> 
>>> 
>>> 
>>> 
>>> x = 7
>>> def main(x):
	print(x)

	
>>> x=6
>>> main()
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    main()
TypeError: main() missing 1 required positional argument: 'x'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> x=7
>>> def main(y=x):
	print(y)

	
>>> x=8
>>> main()
7
>>> #defaulted to what was the original
>>> 
