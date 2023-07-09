# 백준 4949번
while True:
    sentense = input().rstrip()
    if sentense == '.':
        break
    Stack = []
    for j in sentense:
        if j == '(':
            Stack.append(j)
        elif j == '[':
            Stack.append(j)
        elif j == ')':
            if '(' not in Stack:
                Stack.append(j)
                break
            elif Stack[len(Stack)-1] == '[':
                Stack.append(j)
                break
            else:
                Stack.reverse()
                Stack.remove('(')
                Stack.reverse()
        elif j == ']':
            if '[' not in Stack:
                Stack.append(j)
                break
            elif Stack[len(Stack)-1] == '(':
                Stack.append(j)
                break
            else:
                Stack.reverse()
                Stack.remove('[')
                Stack.reverse()
    if len(Stack) != 0:
        print('no')
    else:
        print('yes')