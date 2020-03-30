Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
#Python debugger called PDB to see how the program runs
>>> #Import PDB
>>> 
>>> 
>>> 
>>> 
>>> #Looping
>>> #Better for saving time, work, and can be controlled by the user.
>>> #by Reapeating a task an x number of times
>>> 
>>> #While loop
>>> #While a variable or condition is true, it will repeat the function
>>> 
>>> count = 0
>>> while count < 5:
	count = count + 1

	
>>> #count is now 5
>>> 
>>> counter = 0
>>> while counter < 5
SyntaxError: invalid syntax
>>> 
>>> while counter < 5:
	counter = counter + 1
	print("dank")

	
dank\
dank
dank
dank
dank
>>> #Since while was under 5, it printed dank and added a value to itself until it reached 5
>>> 
>>> 
>>> 
>>> #Use control- C to stop an infinite while loop
>>> #While loops are useful for test and quizes
>>> 
>>> 
>>> 
>>> #To time a user
>>> #use 2 time.time() variables
>>> #one at the beginning & one at the end
>>> #it will take the time at the time its executer
>>> #executed*
>>> #Then take the difference
>>> import time
>>> dank = time.time()
>>> af = time.time()
>>> Sec= af - dank
>>> print sec
SyntaxError: Missing parentheses in call to 'print'
>>> print Sec
SyntaxError: Missing parentheses in call to 'print'
>>> print (Sec)
17.644436836242676
>>> #It took me 17 seconds to write it out
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #use user input to ask user to continue loop
>>> contloop = "yes"
>>> while contloop == "yes":
	contloop=input("do you want to continue?")

	
do you want to continue?yes
do you want to continue?yes
do you want to continue?yes
do you want to continue?fuck no
>>> 
>>> 
>>> 
>>> #Output and Input Redirection
>>> #Use python SentinelValue.py < input.txt to use a txt file as input
>>> #Use python Script.py > output.txt tosave results as a text file
>>> #Python Program < input for input
>>> #PythonProgram > output for output
>>> 
