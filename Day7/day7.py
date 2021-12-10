with open('data.txt', 'r') as f:
    for line in f:
        grade_data = line.strip().split(',')

crabs = []
for x in grade_data:
    crabs.append(int(x))


minFuel = 999999999

for i in range(0, max(crabs)):
    fuel = 0
    for x in crabs:
        dist = abs(x-i)
        for j in range(dist+1):
            fuel += j
    if fuel < minFuel:
        minFuel = fuel
        print(minFuel)
