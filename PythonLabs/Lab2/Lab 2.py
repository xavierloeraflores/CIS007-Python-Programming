
celsius = eval(input("Enter a degree in Celsius:"))
fahrenheit = (9/5) * celsius + 32
print (celsius, "Celsuis is", fahrenheit, "farenheit") 

investmentAmount = eval(input("Enter Investment amount:"))
monthlyInterestRate = (1/1200) * eval(input("Enter annual interest rate:"))
numberOfMonths = 12 * eval(input("Enter number of years:"))
 
futureInvestmentValue = investmentAmount * (1 + monthlyInterestRate)**numberOfMonths
Finalvalue = int(futureInvestmentValue * 100)/100
print ("Accumalated value is", Finalvalue)

originalValue = eval(input("Enter a number between 0 and 1000:"))
first = originalValue % 10
second = (originalValue % 100 - first)/10
third = (originalValue % 1000 - (first + (10*second)))/100
fourth = (originalValue //1000)
sum = fourth + third + second + first
print ("The sum of the digits is", int(sum))

weight = (.45359237) * eval(input("Enter weight in pounds:"))
height = (.0254) * eval(input("Enter height in inches:"))
BMI = weight / (height)**2
print ("BMI is", int(BMI*10000)/10000)












