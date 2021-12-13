import numpy as np

def fold_array(axis, foldLine, array):
    if axis == 'x':
        array = np.transpose(array)
        upper = array[:(foldLine)]
        lower = array[(foldLine+1):]
        lower = np.flip(lower, 0)
        #print(upper)
        #print("----")
        #print(lower)
        return np.transpose(np.logical_or(upper, lower))
        
        
    elif axis == 'y':
        upper = array[:(foldLine)]
        lower = array[(foldLine+1):]
        lower = np.flip(lower, 0)
        #print(upper)
        #print(lower)
        return np.logical_or(upper, lower)
    

coords = []
with open('input.txt', 'r') as f:
    for line in f:
        coords.append(line.strip().split(','))

coords = np.array(coords, dtype=int)


folds = []
with open('folds.txt', 'r') as f:
    for line in f:
        folds.append(line.strip().split('='))

for x in folds:
    x[0] = x[0][-1]
    x[1] = int(x[1])

maxX = 0
maxY = 0
for x in coords:
    if x[0] > maxX:
       maxX =  x[0]
    if x[1] > maxY:
       maxY =  x[1]       
    

field = np.zeros((maxY+1, maxX+1))

##for i in range(len(field)): # Y axis
##    for j in range(len(field[i])): # X axis
##        if [j,i] in coords.tolist():
##            print([j, i])
##            field[i][j] = 1

for x in coords:
    field[x[1]][x[0]] = 1

for x in folds:
    field = fold_array(x[0], x[1], field)

#count = np.count_nonzero(f1 == True)
for x in field: print(x)

dcd = np.array(field, dtype=int)

np.set_printoptions(linewidth=999999)
for x in dcd: print(x)
# Use conditional formatting in excel to decode :)
