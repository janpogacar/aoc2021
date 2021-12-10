import csv

# Start by converting file into list
with open('data.txt', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

charSum = [0] * 12
gamma = ""
eps = ""


for x in data:
    for i in range(12):
        charSum[i] += int(x[0][i])

print(charSum)

for x in charSum:
    if x > 500:
        gamma += "1"
        eps += "0"
    else:
        gamma += "0"
        eps += "1"


print("Product = %i" %(int(gamma, 2)*int(eps, 2)))


tmp_list = []


for i in range(len(data)):
    tmp_list.append(data[i][0])

for i in range(len(tmp_list[0])):
    commonSum = 0
    list2 = []
    for x in tmp_list:
        # Find out most common value
        commonSum += int(x[i])
    for x in tmp_list:    
        if (commonSum >= (len(tmp_list)/2)):
            if x[i] == '1':
                list2.append(x)
        else:
            if x[i] == '0':
                list2.append(x)

    check = int(commonSum >= (len(tmp_list)/2))
    tmp_list = list2
    print("*****")
    print("** %i **" % check)
    print(list2)
    if len(list2) == 1: break


oxy = int(list2[0], 2)

tmp_list = []

for i in range(len(data)):
    tmp_list.append(data[i][0])
    
for i in range(len(tmp_list[0])):
    commonSum = 0
    list2 = []
    for x in tmp_list:
        # Find out most common value
        commonSum += int(x[i])
    for x in tmp_list:    
        if (commonSum >= (len(tmp_list)/2)):
            if x[i] == '0':
                list2.append(x)
        else:
            if x[i] == '1':
                list2.append(x)

    check = int(commonSum >= (len(tmp_list)/2))
    tmp_list = list2
    print("*****")
    print("** %i **" % check)
    print(list2)
    if len(list2) == 1: break

co2 = int(list2[0], 2)

print("Result: %i" %(co2*oxy))
        
        
    
    
    

