numlist = []
for i in range(0, 5, 1):
    numlist.append(int(input()))
numlist.sort()
sum = 0
for j in range(0, 5, 1):
    sum += numlist[j]
aver = sum // 5
print(aver)
print(numlist[2])