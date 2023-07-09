# 백준 1874번
n = int(input())
Stack = []
answer = []
true0_false1 = 0
stacking_num = 1

for i in range(n):
    num = int(input())
    while stacking_num <= num:
        Stack.append(stacking_num)
        answer.append('+')
        stacking_num += 1

    if Stack[len(Stack)-1] == num:
        Stack.pop()
        answer.append('-')
    else:
        print("NO")
        true0_false1 = 1
        break
if true0_false1 == 0:
    for i in answer:
        print(i)