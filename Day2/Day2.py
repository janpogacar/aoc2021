import csv

# Start by converting file into list
with open('data.txt', newline='') as f:
    reader = csv.reader(f,  delimiter=' ')
    data = list(reader)

hpoz = 0
dep = 0

# Puzzle 1
for x in data:
    if x[0] == 'forward':
        hpoz += int(x[1])
    elif x[0] == 'up':
        dep -= int(x[1])
    elif x[0] == 'down':
        dep += int(x[1])

print("Depth: %i, Horizontal position: %i, d*h = %i" %(dep, hpoz, dep*hpoz))

# Puzzle 2
aim = 0
hpoz = 0
dep = 0

for x in data:
    if x[0] == 'forward':
        hpoz += int(x[1])
        dep += (aim*int(x[1]))
    elif x[0] == 'up':
        aim -= int(x[1])
    elif x[0] == 'down':
        aim += int(x[1])
    print(aim)

print("Depth: %i, Horizontal position: %i, d*h = %i" %(dep, hpoz, dep*hpoz))
