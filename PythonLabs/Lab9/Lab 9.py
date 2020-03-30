


#Question 1
intlist= (input("Enter integers between 1 and 100:")).split()
for i in range(0,101):
    count = 0
    count += intlist.count(str(i))
    if count >= 1:
        print(i, "occurs", count, "time", end ="")
        if count !=1:
            print("s")
        else:
            print("")

            
print("")
print("")
print("")


#Question 2
scores=((input("Enter the scores:")).split())
under=[]
over=[]
#Converts list to Floating Points
for i in range(len(scores)):
    scores[i]=float(scores[i])
#Calulates Average
average = (sum(scores)/len(scores))
print("Average:",average)
#Compares every value in the list to average
for i in range(len(scores)):
    if scores[i]>= average:
        #Categorizes values into seperate list
        over.append(scores[i])
    else:
        under.append(scores[i])
#Takes the lengths of the two categories
print("Over the average:",len(over))
print("Below the average:",len(under))


print("")
print("")
print("")

#Question 3
list1 = input("Enter 10 numbers:").split()
list2=[]
#Adds list 1 values to list 2
for i in range(10):
    #Checks if list1 value is not in list 2 already
    if not(list1[i] in list2):
        list2.append(list1[i])

print("The distinct numbers are: ", end ="")
#Prints the values
for i in range(len(list2)):
    print(list2[i], " ", end="")
    

print("")
print("")
print("")


#Question 4
smallst = input("Enter integers:").split()
#Converts all values in the list to ints
for i in range(len(smallst)):
    smallst[i]=int(smallst[i])
#Returns the Index
def indexOfSmallestElement(lst):
    #Finds smallest value
    smallest = min(lst)
    #Returns first instance of the value
    return lst.index(smallest)
#Calls method and prints the result
index = indexOfSmallestElement(smallst)
if index > 1:
    print("Minimum Value Index:", index)








