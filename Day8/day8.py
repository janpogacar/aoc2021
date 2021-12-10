def myFunc(e):
  return len(e)

def decode_7s(codes):
    decoded = [0,0,0,0,0,0,0,0,0,0]
    #codes = ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']
    codes.sort(key=myFunc) # sort by length, index 0 will be 1, 1 will be 7 and so on
    decoded[1] = codes[0]
    decoded[4] = codes[2]
    decoded[7] = codes[1]
    decoded[8] = codes[9]
    codes.remove(codes[9])
    codes.remove(codes[2])
    codes.remove(codes[1])
    codes.remove(codes[0])
    # find 3
    for i in range(len(codes)):
        if (len(codes[i])==5) and (decoded[1][0] in codes[i]) and (decoded[1][1] in codes[i]):
            decoded[3] = codes[i]
            codes.pop(i)
            break
    # find 9
    for i in range(len(codes)):
        if (len(codes[i])==6) and (decoded[3][0] in codes[i]) and (decoded[3][1] in codes[i]) and (decoded[3][2] in codes[i]) and (decoded[3][3] in codes[i]) and (decoded[3][4] in codes[i]):
            decoded[9] = codes[i]
            codes.pop(i)
            break

    # find 0
    for i in range(len(codes)):
        if (len(codes[i])==6) and (decoded[1][0] in codes[i]) and (decoded[1][1] in codes[i]):
            decoded[0] = codes[i]
            codes.pop(i)
            break
            
    # find 6
    for i in range(len(codes)):
        if (len(codes[i])==6):
            decoded[6] = codes[i]
            codes.pop(i)
            break

        
    # find 5
    # find overlap between 6 and 1
    for x in decoded[6]:
        if x in decoded[1]:
            overlap = x

    for i in range(len(codes)):
        if (overlap in codes[i]):
            decoded[5] = codes[i]
            codes.pop(i)
            break

    decoded[2] = codes[0]
    return decoded

codes = []
with open('input.txt', 'r') as f:
    for line in f:
        codes.append(line.strip().split(' | '))

uDigits = 0

for x in codes:
    tmpList = x[1].strip().split(' ')
    for y in tmpList:
        if (len(y) == 2) or (len(y) == 4) or (len(y) == 3) or (len(y) == 7):
            uDigits += 1
    
print("Number of codes containing 1, 4, 7 or 8: %i" %uDigits)

solution = []

for x in codes:
    tmpList = x[0].strip().split(' ')
    display = x[1].strip().split(' ')
    decoded = decode_7s(tmpList)

    for y in display:
        if len(y) == 2: # 1
            solution.append(1)
        elif len(y) == 3: #7
            solution.append(7)
        elif len(y) == 4: #4
            solution.append(4)
        elif len(y) == 5:
            if set(y).issubset(decoded[3]):
                solution.append(3)
            elif set(y).issubset(decoded[5]):
                solution.append(5)
            elif set(y).issubset(decoded[2]):
                solution.append(2) 
        elif len(y) == 6:
            if set(y).issubset(decoded[6]):
                solution.append(6)
            elif set(y).issubset(decoded[0]):
               solution.append(0)
            elif set(y).issubset(decoded[9]):
               solution.append(9) 
        elif len(y) == 7: #8
            solution.append(8)
        else:
            print("Error, no code found")

    
solutionSum = 0            
for i in range (0, len(solution), 4):
    solutionSum = solutionSum + solution[i]*1000 + solution[i+1]*100 + solution[i+2]*10 + solution[i+3]
    print(solution[i]*1000 + solution[i+1]*100 + solution[i+2]*10 + solution[i+3])
        
        
        
        
        
        
    
    


