# 백준 10773번
K = int(input())
num_Stack = []
for i in range(K):
    num = int(input())
    if num == 0:
        del num_Stack[len(num_Stack)-1]
    else:
        num_Stack.append(num)
sum = 0
if len(num_Stack) == 0:
    sum = 0
else:
    for i in range(0, len(num_Stack), 1):
        sum += num_Stack[i]
print(sum)