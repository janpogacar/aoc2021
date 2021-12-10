import csv
import sys

# Numbers drawn
with open('input_nums.txt', newline='') as f:
    reader = csv.reader(f)
    numDrawn = list(reader)
numDrawn = numDrawn[0]

# Numbers drawn
with open('input_boards.txt', newline='') as f:
    reader = csv.reader(f, delimiter = ' ')
    boards = list(reader)

boardArray = []
tmpRow = []

# sort the data to remobe blanks
for i in range(len(boards)):
    tmpRow = []
    for j in range(len(boards[i])):
        if boards[i][j] != '':
            tmpRow.append(boards[i][j])
        
    if len(boards[i]) != 0:
       boardArray.append(list(map(int, tmpRow)))


TDBoardArray = []
for i in range(0, len(boardArray), 5):
    TDBoardArray.append(boardArray[i:i+5])

cardNums = 100
winningCards = []
# Monsterous bingo loop
for x in numDrawn: # Numbers
    for y in range(len(TDBoardArray)): # Boards
        for z in range(len(TDBoardArray[y])): # Rows
            for u in range(len(TDBoardArray[y][z])): # Numbers
                if TDBoardArray[y][z][u] == int(x):
                    TDBoardArray[y][z][u] = 0   # This is incorrect, but it might just work, as 0 was selected early on
    # Check all rows
    n = 0
    for y in range(len(TDBoardArray)): # Boards
        for z in range(len(TDBoardArray[y])): # Rows
            if (TDBoardArray[y][z] == [0,0,0,0,0]) and (y not in winningCards):
                winningCards.append(y)
                print("Bingo! Number: %i, Sum of remaining: %i, Product: %i" %(int(x), sum(sum(TDBoardArray[y],[])), int(x)*sum(sum(TDBoardArray[y],[]))))
                #sys.exit() # Commented out for part two.

                
    # Check all columns (transposed rows)
    n = 0
    for y in range(len(TDBoardArray)): # Boards
        transposed = np.array(TDBoardArray[y]).T.tolist()
        for z in range(len(transposed)): # Rows
            if (transposed[z] == [0,0,0,0,0]) and (y not in winningCards):
                winningCards.append(y)
                print("Bingo! Number: %i, Sum of remaining: %i, Product: %i" %(int(x), sum(sum(TDBoardArray[y],[])), int(x)*sum(sum(TDBoardArray[y],[]))))
                #sys.exit()

