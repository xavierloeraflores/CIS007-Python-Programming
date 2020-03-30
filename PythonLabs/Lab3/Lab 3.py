#Question 1
asc2 = input("Enter an ASCII code:")
char = chr(int(asc2))
print("the character is", char)
print(" ")
#Question 2
print(format(57.467657, "9.3f"))
#   57.468
print(format(12345678.923, "9.1e")) 
#  1.2e+07
print(format(5789.4, "<.2f")) 
#5789.40
print(format(45, "<5d")) 
#45   
print(format(0.457467657, "<9.3%")) 
#45.747%
print(" ")
#Question 3
name = input("Enter employees name:")
hours= eval(input("Enter the number of hours worked in week:"))
payrate= eval(input("Enter hourly payrate:"))
fedtax= eval(input("Enter federal tax withholding rate:"))
statetax= eval(input("Enter State tax withholding rate:"))
gross= hours * payrate
fedDeduct=gross * fedtax
stateDeduct=gross * statetax
totalDeduct = fedDeduct + stateDeduct
netPay = gross - totalDeduct
print("Employee Name:", name, "\n"
    "Pay Rate: $" + str(payrate), "\n" 
    "Gross pay: $"  + str(gross), "\n"
    "Deductions:", "\n"
    "  Federal Withholding (" + str(100* fedtax) + "%): $" + str(round(fedDeduct,2)), "\n"
    "  State Wtihholding (" + str(100*statetax) + "%): $" + str(round(stateDeduct,2)), "\n"
    "  Total Deduction: $" + str(round(totalDeduct,2)), "\n"
    "Net Pay: $" + str(round(netPay,2))    )
