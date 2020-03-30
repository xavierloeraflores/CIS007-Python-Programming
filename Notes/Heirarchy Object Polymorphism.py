Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
#Inheritance
>>> #Relates classes together
>>> #Reuses other software classes
>>> #Superclasses & Subclasses
>>> #Superclass extracts common methods from the subclasses
>>> #Subclasses inherit methods from the superclasses
>>> 
>>> 
>>> 
>>> 
>>> 
>>> Terminology
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    Terminology
NameError: name 'Terminology' is not defined
>>> #   x extends y
>>> 
>>> 
>>> 
>>> #    def __str__(self):
>>> #         return "" + self.__x
>>> # returns a string representation of the class
>>> class Superclass():
	def red:
		
SyntaxError: invalid syntax
>>> class Superclass():
	def red():
		return "sss"

	
>>> class Subclass(Superclass):
	def blue():
		return "xxx"

	
>>> Subclass()
<__main__.Subclass object at 0x112ad0c18>
>>> Subclass().blue()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    Subclass().blue()
TypeError: blue() takes 0 positional arguments but 1 was given
>>> x = Subclass()
>>> x.blue()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    x.blue()
TypeError: blue() takes 0 positional arguments but 1 was given
>>> 
>>> 

>>> 
>>> 
>>> 
>>> 
>>> #When initializing a subclass, you must reference the superclass init
>>> #       superclass().__init__()
>>> 
>>> 
>>> 
>>> 
>>> 

>>> #Using the same name for a method subclass and superclass
>>> #will cause the subclass to override the superclasss
>>> #Unless superclass()METHOD()
>>> 
>>> 
>>> 
>>> #3 or more levels-- superclass will call above it, then that will call above that
>>> #multiple Inheritance
>>> #IT IS POSSIBLE
>>> #SHAPE
>>> #QUADRO SHAPE
>>> #CLASS SQUARE ( SHAPE, QUADRO SHAPE)
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

>>> 

>>> 
>>> 
>>> #Object Class
>>> """The Default class that is being inherited by everything by default /
	 top of the hierarchy /
	 class CLASSNAME inherits methods from OBJECT

"""
'The Default class that is being inherited by everything by default /\n\t top of the hierarchy /\n\t class CLASSNAME inherits methods from OBJECT\n\n'
>>> #OBJECT METHODA
>>> """ /
	___init()__
	__str()__
	__eq__(other)
	"""
' /\n\t___init()__\n\t__str()__\n\t__eq__(other)\n\t'
>>> 
>>> 
>>> 
>>> #That weird <MEthod name object at 7jhbs3ugy3hbd3iudh47dukjd3n4> error is /
>>> #the defuault Object str method
>>> 
>>> 
>>> 
>>> #Default eq method refers to the memory adress from the str method
>>> 
>>> 

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #Polymorphism
>>> #Any method can be called down to the subclasses saftely simply
>>> 
>>> 
>>> #LOOK AT 12.5
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
>>> # isinstance
>>> 
>>> 
>>> 
>>> #Checks if an object is of a type
>>> isintance(10, int)
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    isintance(10, int)
NameError: name 'isintance' is not defined
>>> isinstance(10, int)
True
>>> isinstance(10.0, int)
False
>>> #isinstance(Variable, Class Type)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #Class Relationships
>>> #Classes can have multiplicity
>>> # *-infinit
>>> # m..n -m to n number of
>>> #does not have to be the same bothways
>>> #No number= default =1
>>> #Can create list to store respective relations
>>> """ Associtation types:/
	Agregation
	composition"""
' Associtation types:/\n\tAgregation\n\tcomposition'
>>> 
>>> 
>>> 
>>> 'Aggregation'
'Aggregation'
>>> #represents ownership between 2 objects
>>> #owner/subject-Aggregation object
>>> #class - Aggreagation class
>>> #Object can be owned by many classes
>>> 
>>> 'Composition'
'Composition'
>>> #Exlusive ownership
>>> x = raw_input("What do you want")
Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    x = raw_input("What do you want")
NameError: name 'raw_input' is not defined
>>> 
