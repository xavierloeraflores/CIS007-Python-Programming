Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
#STRINGS
>>> #String Built in functions
>>> x = "Ms ISIS"
>>> len(x)
7
>>> "returns the length"
'returns the length'
>>> 
>>> 
>>> 
>>> #max and min return the smalles ASCII character
>>> max(x)
's'
>>> min(x)
' '
>>> x[1]
's'
>>> x[4]
'S'
>>> #prints ^^^^ the character spot
\
>>> 
>>> 
>>> 
>>> x[1,5]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    x[1,5]
TypeError: string indices must be integers
>>> x[1:5]
's IS'
>>> #prints the range of values
>>> 
>>> 
>>> 
>>> 
>>> x[1,-3]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    x[1,-3]
TypeError: string indices must be integers
>>> x[1:-3]
's I'
>>> #prints the up to the last 3 avluues
>>> #values*
>>> 
>>> 
>>> 
>>> 
>>> 

>>> 
>>> 
>>> 
>>> 
>>> 

>>> 
>>> 

>>> 
>>> 
>>> 
>>> 
>>> 

>>> 
>>> 
>>> 

>>> 

>>> 
>>> 
>>> #Using IN
>>> """In checks to see if a string is within another string"""
'In checks to see if a string is within another string'
>>> 
>>> x=sexy
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    x=sexy
NameError: name 'sexy' is not defined
>>> x= "sexy"
>>> y ="super sexy demon"
>>> x in y
True
>>> y in x
False
>>> "sex" in x
True
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #Alhabetical Comparisons
>>> x= "xavier"
>>> y="xgongiveittoya"
>>> x>=y
False
>>> #x comes before y therefor this is true
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #Testing strings
>>> """
isalnum()       alphanumeric
isalpha()       alphabetic
isdigit()       numeric
islower()       lower case
isupper()       upper case
isspace()       only spaces
isidentifier()  if python identifier
"""
'\nisalnum()       alphanumeric\nisalpha()       alphabetic\nisdigit()       numeric\nislower()       lower case\nisupper()       upper case\nisspace()       only spaces\nisidentifier()  if python identifier\n'
>>> x.isalnum()
True
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #stip to remove spaces
>>> x.lstrip()
'xavier'
>>> x= "Xx __ Dankshooter __ xX"
>>> x.lstip()
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    x.lstip()
AttributeError: 'str' object has no attribute 'lstip'
>>> x.lstrip()
'Xx __ Dankshooter __ xX'
>>> x= "  Xx __ Dankshooter __ xX  "
>>> x.lstrip()
'Xx __ Dankshooter __ xX  '
>>> x.rstrip()
'  Xx __ Dankshooter __ xX'
>>> x.strip()
'Xx __ Dankshooter __ xX'
>>> #l removes left, r removes right, none removes both"
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #Replace
>>> x
'  Xx __ Dankshooter __ xX  '
>>> x.replace("dank","gay")
'  Xx __ Dankshooter __ xX  '
>>> x.replace("Dank","gay")
'  Xx __ gayshooter __ xX  '
>>> #Replaces string values
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #comparing classes
>>> class Circle:
	def__init__(self,r):
		
SyntaxError: invalid syntax
>>> class Circle:
	def__init__(self,r):
		
SyntaxError: invalid syntax
>>> class Circle:
	def__init__(self,r):
		
SyntaxError: invalid syntax
>>> class Circle:
	def__init__(self,r):
		
SyntaxError: invalid syntax
>>> class Circle:
	def __init__(self,r):
		self.radius = r
	def __lt__(self,other):
		return self.radius < other.radius

	
>>> x = Circle(5)
>>> y = Circle(6)
>>> x.__lt(y)
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    x.__lt(y)
AttributeError: 'Circle' object has no attribute '__lt'
>>> x.__lt__(y)
True
>>> #The Circle x has a smaller radius than circle y, therefore this is true
>>> #Comparing objects essentially
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 

>>> 
>>> 
