import csv
import numpy as np
from numpy import savetxt


coords = []
# Start by converting file into list
with open('input.txt', 'r') as f:
    for line in f:
        grade_data = line.strip().split(' -> ')
        coords.append([grade_data[0].split(","), grade_data[1].split(",")])

# find all inline coords
inlineCoords = []

for x in coords:
    if (x[0][0] == x[1][0]) or (x[0][1] == x[1][1]):
        inlineCoords.append(x)


#lineField = np.zeros((1000,1000))
lineField = np.zeros((1000,1000))
for x in coords:
    if x[0][0] == x[1][0]: # horizontal
        for i in range(int(x[0][1]), int(x[1][1])+1, 1):
            lineField[i, int(x[0][0])] += 1
            #print(i)
        for i in range(int(x[1][1]), int(x[0][1])+1, 1):
            lineField[i, int(x[0][0])] += 1
##            #print(i)
    elif x[0][1] == x[1][1]: # vertical
        for i in range(int(x[0][0]), int(x[1][0])+1, 1):
            lineField[int(x[1][1]), i] += 1
            #print(i)
        for i in range(int(x[1][0]), int(x[0][0])+1, 1):
            lineField[int(x[1][1]), i] += 1
            #print(i)
    else: # diagonals
    #(DR)
        j=0
        for i in range(int(x[0][0]), int(x[1][0])+1, 1):
            if  int(x[1][1]) > int(x[0][1]):
                lineField[int(x[0][1])+j, int(x[0][0])+j] += 1 #RD
            else:
                lineField[int(x[0][1])-j, int(x[0][0])+j] += 1 #RU
            j+=1

        j=0        
        for i in range(int(x[1][0]), int(x[0][0])+1, 1):
            if  int(x[1][1]) > int(x[0][1]):
                lineField[int(x[0][1])+j, int(x[0][0])-j] += 1 #LD
            else:
                #lineField[int(x[0][0])-j, int(x[0][1])-j] += 1
                lineField[int(x[0][1])-j, int(x[0][0])-j] += 1  #LU
            j+=1
        print(x)
        print(lineField)
        
    
        
    

        
#savetxt('lineField.csv', lineField, delimiter=',')            
    
print(len(np.where(lineField>1.5)[1]))
