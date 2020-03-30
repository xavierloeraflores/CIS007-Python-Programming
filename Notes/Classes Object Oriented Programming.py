Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
#OBJECTS & CLASSES
>>> """
Class Name:
Data Fields:
Methods:
"""
'\nClass Name:\nData Fields:\nMethods:\n'
>>> """Circle"""
'Circle'
>>> 
>>> class Circle:
	def __init__(self, radius = 1):
		self.radius = radius

	
>>> 
>>> import math
>>> class Circle:
	def __init__(self, radius = 1):
		self.radius = radius

		
>>> class Circle:
	def __init__(self, radius = 1):
		self.radius = radius
	def getPerimeter(self):
		return 2*self.radius*math.pi
	def getArea(self):
		return self.radius*self.radius*math.pi
	def setRadius(self,radius):
		self.radius = radius

		
>>> ###   __init__    initializes an objects new state    ###
>>> class Circle:
	"""Initializes a new variable(state): radius"""
	def __init__(self, radius = 1):
		self.radius = radius

	"Normal Methods that can be called""
	def getPerimeter(self):
		return 2*self.radius*math.pi
	def getArea(self):
		return self.radius*self.radius*math.pi
	def setRadius(self,radius):"""sets new radius"""
		self.radius = radius
		
SyntaxError: EOL while scanning string literal
>>> class Circle:
	"""Initializes a new variable(state): radius"""
	def __init__(self, radius = 1):
		self.radius = radius

	"""Normal Methods that can be called"""
	def getPerimeter(self):
		return 2*self.radius*math.pi
	def getArea(self):
		return self.radius*self.radius*math.pi
	def setRadius(self,radius):"""sets new radius"""
		self.radius = radius
		
SyntaxError: unexpected indent
>>> class Circle:
	"""Initializes a new variable(state): radius"""
	def __init__(self, radius = 1):
		self.radius = radius

	"""Normal Methods that can be called"""
	def getPerimeter(self):
		return 2*self.radius*math.pi
	def getArea(self):
		return self.radius*self.radius*math.pi
	def setRadius(self,radius):
		"""sets new radius"""
		self.radius = radius

		
>>> Circle.getPerimeter()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    Circle.getPerimeter()
TypeError: getPerimeter() missing 1 required positional argument: 'self'
>>> Circle.getPerimeter(5)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    Circle.getPerimeter(5)
  File "<pyshell#28>", line 8, in getPerimeter
    return 2*self.radius*math.pi
AttributeError: 'int' object has no attribute 'radius'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> ### CALLING A CLASS AND AN OBJECT ###
>>> x = Circle(10)
>>> x.getPerimeter
<bound method Circle.getPerimeter of <__main__.Circle object at 0x11430ecf8>>
>>> print(x)
<__main__.Circle object at 0x11430ecf8>
>>> print(x.getPerimeter)
<bound method Circle.getPerimeter of <__main__.Circle object at 0x11430ecf8>>
>>> class Circle:
	"""Initializes a new variable(state): radius"""
	def __init__(self, radius = 1):
		self.radius = radius
	"Normal Methods that can be called""
	def getPerimeter(self):
		return 2*self.radius*math.pi
	def getArea(self):
		return self.radius*self.radius*math.pi
	def setRadius(self,radius):"""sets new radius"""
		self.radius = radius
		
SyntaxError: EOL while scanning string literal
>>> class Circle:
	def __init__(self, radius = 1):
		self.radius = radius
	def getPerimeter(self):
		return 2*self.radius*math.pi
	def getArea(self):
		return self.radius*self.radius*math.pi
	def setRadius(self,radius):
		self.radius = radius

		
>>> x=Circle(10)
>>> print(x.getArea)
<bound method Circle.getArea of <__main__.Circle object at 0x11427f828>>
>>> x=Circle
>>> 
>>> x.getArea
<function Circle.getArea at 0x10365c1e0>
>>> y = x.getArea
>>> print(y)
<function Circle.getArea at 0x10365c1e0>
>>> import math
>>> x=Circle(10)
>>> print(x.getArea)
<bound method Circle.getArea of <__main__.Circle object at 0x11430ecf8>>
>>> class Circle:
	def __init__(self, radius):
		self.radius = radius
	def getPerimeter(self):
		return 2*self.radius*math.pi
	def getArea(self):
		return self.radius*self.radius*math.pi
	def setRadius(self,radius):
		self.radius = radius

		
>>> x = Circle(10)
>>> print(x.getArea)
<bound method Circle.getArea of <__main__.Circle object at 0x11427f828>>
>>> class Circle:
	def __init__(self, radius=1):
		self.radius = radius
	def getPerimeter(self):
		return 2*self.radius*math.pi

	
>>> x = Circle()
>>> print(x.getPerimeter())
6.283185307179586
>>> ###Errors###
>>> 
>>> 
>>> 
>>> """When calling a method inside the class, we do not call the parameters"""
'When calling a method inside the class, we do not call the parameters'
>>> x.getPerimeter()  #CORRECT
6.283185307179586
>>> x.getPerimeter() #INcorrect
6.283185307179586
>>> x.getPerimeter(5) #INcorrect
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    x.getPerimeter(5) #INcorrect
TypeError: getPerimeter() takes 1 positional argument but 2 were given
>>> class Circle:
	def __init__(self, radius=1):
		self.radius = radius #Notice how we dont have to use "global"
	def getPerimeter(self):
		return 2*self.radius*math.pi#All selfs are global within classes

	
>>> #SCOPE^^^^^^
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
>>> ###Professionals use a UML CLASS DIAGRAM to write out classes
>>> ###IMMUTABLE VS MUTABLE OBJECTS
>>> ###IMMUTABLE: Objects that cant be changed
>>> ###MUTABLE: Objects that can be changed(like classes with parameters)
>>> 
>>> 
>>> 
>>> #Private methods
>>> #USE:     __name   to hide vairable name
>>> class Circle:
	def __init__(self, radius=1):
		self.__radius = radius
	def getPerimeter(self):
		return 2*self.__radius*math.pi

	
>>> x = Circle(10)
>>> x.__radius
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    x.__radius
AttributeError: 'Circle' object has no attribute '__radius'
>>> #THIS CAN HIDE DATA FROM USER
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #Abstraction and Encapsulation: allow us to hide our classes from
>>> #people who want to use our class
>>> #Import methods from a seperate file or class
>>> 
