

#Question 1
num = 420
poscount = 0
negcount = 0
total = 0
while num !=0:
    num = eval(input("Enter an integer, the input ends if it is 0:"))
    total += num
    if num > 0:
        poscount +=1
    elif num < 0:
        negcount +=1
if poscount + negcount == 0:
    average = 0
    print("You did not enter any number")
else:
    average = (total)/(poscount + negcount)
    print("The number of positives is", poscount)
    print("The number of negatives is", negcount)
    print("The total is", total)
    print("The average is", average)


print("")
#Question 2
linecount = 1
for dividend in range(100, 201):
    if (dividend % 6 ==0 and dividend % 5 !=0 ) or (dividend % 5 ==0 and dividend % 6 !=0):
        if linecount <=10:
            linecount +=1
        else:
            print("")
            linecount = 2
        print (dividend, " ", end="")


        
print("")
#Question 3
n1 = eval(input("Enter number 1:"))
n2 = eval(input("Enter number 2:"))
if n1 > n2:
    (n1,n2)=(n2,n1)
divisor = n1
if n1 != 0:
    for divisor in range(n1, 0, -1):
        if n1 % divisor ==0 and n2 % divisor ==0:
            gcd = divisor
            print("The greatest common divisor is", gcd)
            break
elif n1==0 and n2==0:
    print("Both numbers are equal to 0")
else:
    print("There are no common divisors")
print("")



