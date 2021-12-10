import numpy as np
from scipy.ndimage.measurements import label

nines = ''

for i in range(100+2):
    nines += '9'
    
lines=[nines]
with open('input.txt', 'r') as f:
    for line in f:
        lines.append('9'+line.strip()+'9')

lines.append(nines)

mins = []

regions = np.zeros((102,102), dtype=int)

for i in range(1,101):
    for j in range(1,101):
        if (lines[i][j]<lines[i+1][j]) and (lines[i][j]<lines[i-1][j]) and (lines[i][j]<lines[i][j+1]) and (lines[i][j]<lines[i][j-1]):
            mins.append(int(lines[i][j])+1)
        if (lines[i][j] != '9'):
            regions[i][j] = 1
            
labeled, ncomponents = label(np.array(regions))
sizes = []

for i in range(1, np.max(labeled)):
    count = np.count_nonzero(labeled == i)
    print("%i, %i" %(i, count))
    sizes.append(count)


sizes.sort()
