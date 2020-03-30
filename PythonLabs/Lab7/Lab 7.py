#Object Rectangle
class Rectangle:
    def __init__(self, width=1, height = 2):
        self.width = width
        self.height = height
    #Get Methods
    def getArea(self):
        return self.width*self.height
    def getPerimeter(self):
        return 2*(self.width+self.height)
#Creates new objects
z = Rectangle(4,40)
w = Rectangle(3.5,35.7)
def main(x,y):
    #prints the width, height, Area, and Perimeter
    print("Rectangle",y)
    print("Width:", x.width)
    print("Height:", x.height)
    print("Area:", x.getArea())
    print("Perimeter:", x.getPerimeter())
    print("")
main(z,1)
main(w,2)
print("")
print("")
print("")




#Question 2x = Rectangle(wid,hei)
class Stock:
    def __init__(self, name="default", symbol="AAAA" , currentPrice =0.0 ,previousClosingPrice=0.0):
        self.__name = name
        self.__symbol = symbol
        self.__currentPrice = currentPrice
        self.__previousClosingPrice = previousClosingPrice
    #Get Methods
    def getStockName(self):
        return self.__name
    def getSymbol(self):
        return self.__symbol
    def getCurrentPrice(self):
        return self.__currentPrice
    def getPreviousClosingPrice(self):
        return self.__previousClosingPrice
    #Sets Current and Previous Prices
    def setCurrentPrice(self,price):
        self.__currentPrice = price
    def setPreviousClosingPrice(self,price):
        self.__previousClosingPrice = price
    #Gets Percentage Increased and returns the %
    def increase(self):
        if self.__previousClosingPrice != 0:
            return (int(((self.__currentPrice - self.__previousClosingPrice)/(self.__previousClosingPrice))*10000)/100)        
Intel = Stock("Intel Corporation", "INTL" , 20.35, 20.5)
print(Intel.getStockName())
print(Intel.getSymbol())
print(Intel.getCurrentPrice())
print(Intel.getPreviousClosingPrice())
print("Increase: ", Intel.increase(), "%", sep = "")
print("")
print("")
print("")




#Question 3
import time
class Stopwatch:
    def __init__(self):
        self.__endTime = 0
        self.__startTime = time.time()
    #Restarts and Stops Timers
    def start(self):
        self.__startTime = time.time()
    def stop(self):
        self.__endTime = time.time()
    #Get Methods
    def getStartTime(self):
        return self.__startTime
    def getEndTime(self):
        return self.__endTime
    def getElapseTime(self):
        return (self.__endTime - self.__startTime)
#Creates Stopwatch and Starts Timer
watch = Stopwatch()
i = 1
totalsum = 0
#Finds sum from 1 to 1000000
while i <= 1000000:
    totalsum += i
    i+= 1
#Stops Timer
watch.stop()

#Prints the sum, and the total time in Milliseconds
print("Total:", totalsum)
print("Time:",(str(int((watch.getElapseTime()*1000)//1))),"Milliseconds")


