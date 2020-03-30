"""Question 1"""

number = eval(input("Enter a number:"))
degree = 1
place=1
i=0
#Finds the number of places
while place>0:
    if number /(10**degree)  >= 10:
              degree+=1
    else:
        break
#Reverses a number with opposite number
def reverse(deg,degree):
    char1 = (number// (10**deg))%10
    char2=(number// (10**(degree - (deg))))%10
    (char1,char2)=(char2,char1)
    return(char2)
#Swaps until it has swapped to the same number of places
while i <= degree:
    deg=i

    printer = reverse(deg,degree)
    i+=1
    print(printer,end="")
print("")
print("")
print("")


"""Question 2"""


#ask user for input
numline = eval(input("How many characters per line?:"))
term1 = input("Enter your first term:")
term2 = input("Enter your second term:")
ord1 = ord(term1)
ord2 =ord(term2)
#sets the terms in order
if ord2 < ord1:
    (ord1,ord2)=(ord2,ord1)
#prints the terms
def printChars(ch1,ch2,numbersPerLine):
    i=0
    while (ch1+i)<=ch2:
        print(chr(ch1+i), end =" ")
        i+=1
        if i % numbersPerLine==0:
            print("")
printChars(ord1,ord2,numline)
print("")
print("")
print("")



"""Question 3"""


import random
matrix = eval(input("Enter n:"))

def printMatrix(n):
    i=0
    #Prints n^2 random numbers of 0 & 1
    while i < n**2:
        print (round(random.random()), end =" ")
        i+=1
        #Starts new line ever n times
        if i%n==0:
            print("")
printMatrix(matrix)
print("")
print("")
print("")


"""Question 4"""


number = eval(input("Enter an integer:"))
width = eval(input("Enter the width:"))
def format(number,width):
    count = 0
    #Finds the number of places
    while (10**count)<(number+.01):
        count+=1
    #Finds the number of zeroes needed to achieve the width
    zeros = "0"*(width-count)
    num = (zeros+str(number))
    print(num)
format(number,width)

    


