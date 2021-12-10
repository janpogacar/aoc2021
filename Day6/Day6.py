with open('input.txt', 'r') as f:
    for line in f:
        grade_data = line.strip().split(',')

fishes = []
for x in grade_data:
    fishes.append(int(x))

dayCount = []
#fishes = [8]

# Array containing a number of fish with a specific value
fishValues = []
for i in range(10): # count the number of fishes with a certain value
    fishValues.append(fishes.count(i))

print(fishValues)

for i in range(256):
    fishValues[0] = fishValues[1]
    fishValues[1] = fishValues[2]
    fishValues[2] = fishValues[3]
    fishValues[3] = fishValues[4]
    fishValues[4] = fishValues[5]
    fishValues[5] = fishValues[6]
    fishValues[6] = fishValues[7]
    fishValues[7] = fishValues[8]
    fishValues[8] = fishValues[9]
    fishValues[9] = 0
        
    print("after day %i:" %(i+1))
    print(fishValues)
    print(sum(fishValues))
    fishValues[7] += fishValues[0]
    fishValues[9] = fishValues[0]



            

     
    
        
