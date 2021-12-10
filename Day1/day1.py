import csv

# Start by converting file into list
with open('measurements.txt', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
    
count = 0
falsecount = 0

# Puzzle 1
for i in range(0, len(data)):
  if (int(data[i][0]) > int(data[i-1][0])):
      count += 1
  else:
      falsecount += 1

print("Number of larger numbers is %i" %count)

winCount = 0

# Puzzle 2
for i in range(1, len(data)-2):
    win1 = int(data[i-1][0]) + int(data[i][0]) + int(data[i+1][0])
    win2 = int(data[i-1+1][0]) + int(data[i+1][0]) + int(data[i+1+1][0])
    if win2>win1:
        winCount += 1

print("Number of larger windows is %i" %winCount)

    
