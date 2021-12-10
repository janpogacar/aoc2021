import statistics

lines = []
lineList = []
with open('input.txt', 'r') as f:
    for line in f:
        lines.append(line.strip())


for x in lines:
    tmpLine = []
    for y in x:
        tmpLine.append(y)
    lineList.append(tmpLine)
    #fullList.append(tmpLine)

fullList = lineList.copy()
### Discard incomplete lists first
##corList = []
##
##for i in range(len(lineList)):
##    print(lineList[i].count('<')+lineList[i].count('(')+lineList[i].count('{')+lineList[i].count('[')-lineList[i].count('>')-lineList[i].count(')')-lineList[i].count('}')-lineList[i].count(']'))
##    if ((lineList[i].count('<')+lineList[i].count('(')+lineList[i].count('{')+lineList[i].count('[')-lineList[i].count('>')-lineList[i].count(')')-lineList[i].count('}')-lineList[i].count(']')) == 0):
##        corList.append(lineList[i])
incList = []
    
cChars = []




for i in range(len(lineList)):
    print(lineList[i])
    tInc = lineList[i].copy()
    found = False
    while(not found):
        j=0

        while j < (len(lineList[i])-1):
            if ('>' not in lineList[i]) and ('}' not in lineList[i]) and (']' not in lineList[i]) and (')' not in lineList[i]):
                    print("list is incomplete, no closers left")
                    incList.append(tInc)
                    #print(tInc)
                    found = True
                    break
            
            if (lineList[i][j] == '<'):
                if lineList[i][j+1] == '>':
                    if (j+2) > len(lineList[i]):
                        print("list is incomplete")
                        incList.append(tInc)
                        found = True
                        break
                    lineList[i].pop(j)
                    lineList[i].pop(j)
                elif (lineList[i][j+1] == ']') or (lineList[i][j+1] == '}') or (lineList[i][j+1] == ')'):
                    print("expected: %s, corrupted %s found!" %(lineList[i][j], lineList[i][j+1]))
                    cChars.append(lineList[i][j+1])
                    found = True
                    break
                
            elif (lineList[i][j] == '('):
                if lineList[i][j+1] == ')':
                    if (j+2) > len(lineList[i]):
                        print("list is incomplete")
                        incList.append(tInc)
                        found = True
                        break
                    lineList[i].pop(j)
                    lineList[i].pop(j)
                elif (lineList[i][j+1] == ']') or (lineList[i][j+1] == '}') or (lineList[i][j+1] == '>'):
                    print("expected: %s, corrupted %s found!" %(lineList[i][j], lineList[i][j+1]))
                    cChars.append(lineList[i][j+1])
                    found = True
                    break
                
            elif (lineList[i][j] == '['):
                if lineList[i][j+1] == ']':
                    if (j+2) > len(lineList[i]):
                        print("list is incomplete")
                        incList.append(tInc)
                        found = True
                        break
                    lineList[i].pop(j)
                    lineList[i].pop(j)
                elif (lineList[i][j+1] == '>') or (lineList[i][j+1] == '}') or (lineList[i][j+1] == ')'):
                    print("expected: %s, corrupted %s found!" %(lineList[i][j], lineList[i][j+1]))
                    cChars.append(lineList[i][j+1])
                    found = True
                    break
                
            elif (lineList[i][j] == '{'):
                if lineList[i][j+1] == '}':
                    if (j+2) > len(lineList[i]):
                        print("list is incomplete")
                        incList.append(tInc)
                        found = True
                        break
                    lineList[i].pop(j)
                    lineList[i].pop(j)
                elif (lineList[i][j+1] == ']') or (lineList[i][j+1] == '>') or (lineList[i][j+1] == ')'):
                    print("expected: %s, corrupted %s found!" %(lineList[i][j], lineList[i][j+1]))
                    cChars.append(lineList[i][j+1])
                    found = True
                    break
            j += 1
            
score = 0        
for x in cChars:
    if x == ')':
        score += 3
    if x == ']':
        score += 57
    if x == '}':
        score += 1197
    if x == '>':
        score += 25137

#for x in incList: print(x)

lineScores = []

for x in incList:
    lineScore = 0
    ca = 0 # )
    cb = 0 # ]
    cc = 0 # }
    cd = 0 # >
    i = len(x)-1
    #for i in range(len(x)-1, 0, -1):
    while (i>=0):
        #print(i)

        if x[i] == ')':
            ca += 1
            
        if x[i] == '(':
            ca -= 1

        if x[i] == ']':
            cb += 1
            
        if x[i] == '[':
            cb -= 1

        if x[i] == '}':
            cc += 1
            
        if x[i] == '{':
            cc -= 1

        if x[i] == '>':
            cd += 1
            
        if x[i] == '<':
            cd -= 1

        #print(x[i])
        #print(ca)
        #print(cb)
        #print(cc)
        #print(cd)

        if ca < 0:
            x.append(')')
            lineScore = lineScore*5 + 1
            ca = 0 # )
            cb = 0 # ]
            cc = 0 # }
            cd = 0 # >
            i = len(x)
            
        elif cb < 0:
            #print(i)
            x.append(']')
            lineScore = lineScore*5 + 2
            #print(i)
            ca = 0 # )
            cb = 0 # ]
            cc = 0 # }
            cd = 0 # >
            i = len(x)           
        elif cc < 0:
            ca = 0 # )
            cb = 0 # ]
            cc = 0 # }
            cd = 0 # >
            x.append('}')
            lineScore = lineScore*5 + 3
            i = len(x)
                      
        elif cd < 0:
            ca = 0 # )
            cb = 0 # ]
            cc = 0 # }
            cd = 0 # >
            x.append('>')
            lineScore = lineScore*5 + 4
            i = len(x)
        i -= 1
        
    print(x)
    lineScores.append(lineScore)


print(statistics.median(lineScores))

















