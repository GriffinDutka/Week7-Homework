"""
Griffin Dutka
9/16/21
Assignment 6.1 Classes
"""

#Vehicle class
class Vehicles:
    def __init__(self,make,model,color,fuelType,options):
      self.make=make
      self.model=model
      self.color=color
      self.fuelType=fuelType
      self.options=options

#Obtain Information

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getColor(self):
        return self.color

    def getFuelType(self):
        return self.fuelType

    def getOptions(self):
        return self.options

#Child for vehicles = pickup child class
class Pickup(Vehicles):

    def __init__(self,make,model,color,fuelType,options,cabStyle,bedLength):
        Vehicles.__init__(self,make,model,color,fuelType,options)
        self.cabStyle=cabStyle
        self.bedLength=bedLength
    
    def getCabStyle(self):
        return self.cabStyle
    def getBedLength(self):
        return self.bedLength

    def printDetails(self):
        print("Pickup make: ",self.make)
        print("Pickup model: ",self.model)
        print("Pickup color: ",self.color)
        print("Pickup fuel type: ",self.fuelType)
        print("Pickup options: ",self.options)
        print("Pickup cab style: ",self.cabStyle)
        print("Pickup bed length: ",self.bedLength)
        print("--------------------------------------")

#Child for vehicles = car child class

class Car(Vehicles):
    def __init__(self,make,model,color,fuelType,options,engineSize,numDoor):

        Vehicles.__init__(self,make,model,color,fuelType,options)
        self.engineSize=engineSize
        self.numDoor=numDoor
        
    def getEngineSize(self):
        return self.engineSize

    def numDoors(self):
        return self.numDoor

    def printDetails(self):
        print("Car make:",self.make)
        print("Car model: ",self.model)
        print("Car color: ",self.color)
        print("Car fuel type: ",self.fuelType)
        print("Car options: ",self.options)
        print("Car engine size: ",self.engineSize)
        print("Car number of doors: ",self.numDoor)
        print("--------------------------------------")
thegarage=[]
#Loop user input
while(True):
    option = int(input("Choose from the following menu (1,2,3): \n1 To add a Car \n2 To add a Pickup \n3 To view Garage and exit \n"))
    if (option==1): #for Car
        make=input("Enter car make: ")
        model=input("Enter car model: ")
        color=input("Enter car color: ")
        fuelType=input("Enter car fuel type (Premium or Unleaded): ")
        options=input("Enter car options separated by commas, \n Options include (Power Mirrors, Power Locks, Remote Start, Backup Camera, Bluetooth, Cruise Control, Heated Seats, Leather Seats): ")
        engineSize=input("Enter car engine size: ")
        numDoor=input("Enter car number of doors: ")
        p=Car(make,model,color,fuelType,options,engineSize,numDoor)
        thegarage.append(p)
    elif(option==2): #For Pickup
        make=input("Enter pickup make:")
        model=input("Enter pickup model:")
        color=input("Enter pickup color:")
        fuelType=input("Enter pickup fuel type (Diesel, Premium, or Unleaded):")
        options=input("Enter pickup options separated by commas \n Options include (Power Mirrors, Power Locks, Remote Start, Backup Camera, Bluetooth, Cruise Control, Heated Seats, Leather Seats): ")
        cabStyle=input("Enter pickup cab style (Regular, Extended, or Crew):")
        bedLength=(input("Enter pickup bed length (60-96 inches)"))
        t=Pickup(make,model,color,fuelType,options,cabStyle,bedLength)
        thegarage.append(t)
    else: 
        break
#Print Garage Info
print ("Your Garage includes the following Vehicles:")
print("--------------------------------------")

for v in thegarage:
        v.printDetails()
