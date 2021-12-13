def find_pairs(cave, coords):
    if cave == 'end':
        return []
    pairs = []
    for x in coords:
        if cave in x:
            if cave == x[0]:
                pairs.append(x[1])
            else:
                pairs.append(x[0])
    if 'start' in pairs:            
        pairs.remove('start')
    return pairs
            


coords = []
with open('input.txt', 'r') as f:
    for line in f:
        coords.append(line.strip().split('-'))

pFound = False

pDict = {
    "path": ['start'],
    "uCaves": []

    }

L2 = []
paths = [['start']]
uCaves = []
solution1 = []
sInt = 0

for i in range(100):
    print(i)
    pCopy = paths.copy()
    for x in pCopy:
        foundPair = False
        for y in (find_pairs(x[-1], coords)):
            pLine = x.copy()
            uCondition = True
            for z in pLine:
                if not(z.isupper()):
                    if x.count(z) > 1:
                        uCondition = False
            if (y == 'end') or not(not(y.isupper()) and (x.count(y) >= 1)) or (uCondition and not(not(y.isupper()) and (x.count(y) >= 2))):
                foundPair = True
                pLine.append(y)
                paths.append(pLine)
                if x in paths:
                    paths.remove(x)

    for a in paths:
        if (a[-1] == 'end'):
            sInt += 1
            if a in paths:
                paths.remove(a)




print(sInt)


