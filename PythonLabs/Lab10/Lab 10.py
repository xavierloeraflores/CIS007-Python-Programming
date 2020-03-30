#Question 1
#Create Matrix
m3x4 = []
#Accept User input
for i in range(3):
    row3x4=input("Enter a 3x4 matrix row for row "+str(i)+":").split()
    #Convert to float
    for b in range(4):
        row3x4[b]=(eval(row3x4[b]))
    m3x4.append(row3x4)
#Returns Sum of a column
def sumColumn(m, columnIndex):
    columnsum=0
    for i in range(3):
        columnsum+=m[i][columnIndex]
    return columnsum
#Calls the sumCpumn Function 4 times
for i in range(3):
    columnsum = sumColumn(m3x4,i)
    print("The sum of the elements for Column",i,"is",columnsum)



#Question 2
#Create n X n Matrix
nxnmatrix = []
#Ask user for # of rows
nxnsize = int(eval(input("Enter the number of rows:")))
#Input for the matrix
for i in range(nxnsize):
    nxnrow=input("Enter a "+str(nxnsize) +"-by-"+str(nxnsize) + " Matrix for row "+str(1+i)+":").split()
    for b in range(nxnsize):
        nxnrow[b] = eval(nxnrow[b])
    nxnmatrix.append(nxnrow)
#Takes the sum of the Diagonal
def sumMajorDiagonal(m):
    diagonalsum = 0
    #adds only the diagonal indexes
    nxnsize=len(nxnmatrix)
    for i in range(nxnsize):
        diagonalsum += m[i][i]
    return diagonalsum
#calls the sum of the diagonal
diagonal = sumMajorDiagonal(nxnmatrix)
print("Sum of the elements in the major diagonal is", diagonal)



#Question 3
import random
#Create matrix
randmatrix=[]
#Create a row
for i in range(4):
    randrow = []
    for b in range(4):
    #Add random numbers of 1 & 0
        randrow.append(int(round(random.random())))
    #Add row to the matrix
    randmatrix.append(randrow)
#Count the number of 1s in each row
rowcount = []
for i in range(4):
    count = randmatrix[i].count(1)
    rowcount.append(count)
#Count the number of 1s in each column
columncount = []
for i in range(4):
    count =0
    for b in range(4):
        count +=randmatrix[b][i]
    columncount.append(count)
print(randmatrix)
#Returns indexes with the most 1s
def comp(counts):
    m=max(counts)
    indexes=[]
    for i in range(4):
        if counts[i]==m:
            indexes.append(i)
    return indexes

print("The Largest Row index is:"+str(comp(rowcount))[1:-1])
print("The Largest Column Index is:"+str(comp(columncount))[1:-1])




