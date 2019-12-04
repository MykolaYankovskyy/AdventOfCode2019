
file = open("InputDay3.txt", "r")
fileLines  = file.readlines()
WirePath1 = fileLines[0]
WirePath1 = WirePath1.split(",")
WirePath2 = fileLines[1]
WirePath2 = WirePath2.split(",")
print(len(WirePath1))
print(len(WirePath2))
coordinate1 = [0,0]
coordinate2 = [0,0]
i = 0
while (i < len(WirePath1)):
    print(i)
    command1 = WirePath1[i]
    command2 = WirePath2[i]
    direction1 = command1[0]
    direction2 = command2[0]
    if(direction1 == "U"):
        coordinate1[1] += int(command1[1:])
    elif(direction1 == "D"):
        coordinate1[1] -= int(command1[1:])
    elif(direction1 == "R"):
        coordinate1[0] += int(command1[1:])
    elif(direction1 == "L"):
        coordinate1[0] -= int(command1[1:])
    if(direction2 == "U"):
        coordinate2[1] += int(command2[1:])
    elif(direction2 == "D"):
        coordinate2[1] -= int(command2[1:])
    elif(direction2 == "R"):
        coordinate2[0] += int(command2[1:])
    elif(direction2 == "L"):
        coordinate2[0] -= int(command2[1:])

    if(coordinate1[0] == coordinate2[0] and coordinate1[1] == coordinate2[1]):
        print("overlap found")
        print(coordinate1)
        continue
    else:
        print(coordinate1)
        print(coordinate2)
        i+=1
        continue