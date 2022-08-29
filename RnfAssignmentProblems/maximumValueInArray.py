# Find the maximum value in Array without using Collection?array {3,7,95,16,52,44,1,100}

maxVal = 0

l = [3, 7, 95, 16, 52, 44, 1, 100]

for i in l:
    if i > maxVal:
        maxVal = i

print(maxVal)
