import numpy as np

lines = []

with open('input.txt', 'r') as f:
    for line in f:
        indLine = []
        indLine.append(0)
        for x in line.strip():
            indLine.append(int(x))
        indLine.append(0)   
        lines.append(indLine)

lines.insert(0, np.zeros(len(lines[0])))
lines.append(np.zeros(len(lines[0])))
 
meduze = np.array(lines, dtype = int)

flashes = np.ones((len(meduze[0]), len(meduze)))
flashes[0] = np.zeros(len(flashes[0]))
flashes[len(flashes[0])-1] = np.zeros(len(flashes[0]))

for i in range(len(flashes)):
    flashes[i][0] = 0
    flashes[i][len(flashes[i]) -1] = 0

result = 0

zeroCheck = np.zeros((len(meduze[0]), len(meduze)))
    
for n in range(10000):
    tmpf = np.copy(flashes)
    for i in range(1, len(meduze) - 1):
        for j in range(1, len(meduze[i]) - 1):
            meduze[i][j] += 1
    foundAll = False
    while(foundAll is False):
        foundAll = True
        for i in range(1, len(meduze) - 1):
            for j in range(1, len(meduze[i]) - 1):
                if meduze[i][j] > 9:
                    result += 1
                    meduze[i][j+1] += 1
                    meduze[i][j-1] += 1
                    meduze[i+1][j+1] += 1
                    meduze[i+1][j] += 1
                    meduze[i+1][j-1] += 1
                    meduze[i-1][j-1] += 1
                    meduze[i-1][j] += 1
                    meduze[i-1][j+1] += 1
                    tmpf[i][j] = 0
                    foundAll = False
        meduze = meduze * tmpf
    print(meduze)
    if np.array_equal(meduze, zeroCheck):
        print(n+1)
        break
                
                
            
