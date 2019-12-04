import numpy
import math
from random import randint
tries = 0
result = 0
while (result != 19690720):
    file = open("InputDay2.txt","r")
    data = file.readline()
    datalist = data.split(",")
    datalist = list(map(int,datalist))
    i = 0
    j = 1
    k = 2
    l = 3
    datalist[1] = randint(0,(len(datalist)-1))
    datalist[2] = randint(0,(len(datalist)-1))
    while (i < len(datalist)):
        positionJ = datalist[j]
        positionK = datalist[k]
        positionL = datalist[l]
        if (datalist[i] == 1):
            value = datalist[positionJ]+datalist[positionK]
            datalist[positionL] = value
            i += 4
            j += 4
            k += 4
            l += 4
            continue
        elif(datalist[i] == 2):
            value = datalist[positionJ]*datalist[positionK]
            datalist[positionL] = value
            i += 4
            j += 4
            k += 4
            l += 4
            continue
        elif(datalist[i] == 99):
            tries +=1
            result = datalist[0]
            break
        else:
            print("Error")
            i += 4
            j += 4
            k += 4
            l += 4
            continue
        continue
print(tries)
print(datalist[0])
print(datalist[1])
print(datalist[2])
finalresult = 100*datalist[1]+datalist[2]
print(finalresult)
