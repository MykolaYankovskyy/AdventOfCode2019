import numpy
import math
fuelAmount = 0
file = open("InputDay1.txt","r")
fileLine  = file.readlines()
for x in fileLine:
    fuelRequired = (math.floor(int(x)/3))-2
    fuelAmount += fuelRequired
    while (((math.floor(fuelRequired/3))-2) >=0):
        fuelAmount += (math.floor(fuelRequired/3))-2
        fuelRequired = (math.floor(fuelRequired/3))-2

print(fuelAmount)
