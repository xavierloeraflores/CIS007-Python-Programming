#Question 1
SSN= input("Enter your social security number:xxxx-xx-xxxx:")
i = 0
#Checks all characters in the string
while i < len(SSN):
    #Checks for "-"
    if i == 4 or i == 7:
        if SSN[i]!="-":
            print("Invalid SSN")
            break
    #Checks for digits
    elif SSN[i].isdigit()!=True:
        print("Invalid SSN")
        break
    #Checks for length
    elif len(SSN) != 12:
        print("Invalid SSN")
        break
    #Returns Validation on final digit
    elif i+1 == 12:
        print("Valid SSN")
    i+=1
print("")
print("")
print("")




#Question 2
password = input("Please enter your password:")
i = 0
digits = 0
#Checks for password length and characters
if len(password) >= 8 and password.isalnum() == True:
#Counts Number of digits
    while i < len(password):
        if password[i].isdigit() == True:
            digits +=1
        i+=1
    #Checks for at least 2 digits
    if digits<2:
        print("Invalid Password")
    else:
        print("Valid Password")
else:
    print("Invalid Password")
print("")
print("")
print("")



#Question 3
string = input("Enter a string, any string. It doesn't matter:")
#Reverse function
def reverse(string):
    #Count string length
    count = len(string)
    #Print from last to first
    while count>0:
        print(string[count-1], end="")
        count-=1
reverse(string)
