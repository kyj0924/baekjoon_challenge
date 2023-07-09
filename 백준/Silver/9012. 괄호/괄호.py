# 백준 9012번(문제점 보완, 스택으로 접근)
T = int(input())
for i in range(T):
    PS = input()
    Stack = []
    for j in PS:
        if j == '(':
            Stack.append(j)
        else:
            if len(Stack) == 0:
                Stack.append(j)
                break
            else:
                Stack.pop()
    if len(Stack) != 0:
        print('NO')
    else:
        print('YES')