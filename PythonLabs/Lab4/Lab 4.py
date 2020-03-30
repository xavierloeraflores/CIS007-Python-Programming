#Question 1
import random
ran1 = random.randint(0,100)
ran2 = random.randint(0,100)
sum = ran1 + ran2
user = eval(input("What is " + str(ran1) + " + " + str(ran2) + "?"))
if user == sum:
    print("Correct")
else:
        print("Wrong")

print(' ')
#Question 2
month = eval(input("Enter the month number:"))
year = eval(input("Enter the year:"))
if month == 1:
    print("January, " + str(year) + " has 31 days")
elif month == 2:
    if year % 4 == 0:
        print("Febuary," + str(year) + " has 29 days")
    else:
        print("Febuary, " + str(year) + " has 28 days")
elif month == 3:
    print("March," + str(year) + " has 31 days")
elif month == 4:
    print("April, " + str(year) + " has 30 days")
elif month == 5:
    print("May, " + str(year) + " has 31 days")
elif month == 6:
    print("June, " + str(year) + " has 30 days")
elif month == 7:
    print("July, " + str(year) + " has 31 days")
elif month == 8:
    print("August, " + str(year) + " has 31 days")
elif month == 9:
    print("September, " + str(year) + " has 30 days")
elif month == 10:
    print("October, " + str(year) + " has 31 days")
elif month == 11:
    print("November, " + str(year) + " has 30 days")
elif month == 12:
    print("December, " + str(year) + " has 31 days")

print(' ')


#Question 3
x =  eval(input("Enter an integer:"))
y =  eval(input("Enter an integer:"))
z =  eval(input("Enter an integer:"))
if z < x and z <= y:
    if x >= y: print ( z, y, x)
    else: print(z, x, y)
elif y < x and y <= z:
    if x > z: print(y, z, x)
    else: print(y, x, z)
elif x < y and x <= z:
    if y > z:  print(x, z, y)
    else: print(x, y, z)
else:print(x, y, z)
