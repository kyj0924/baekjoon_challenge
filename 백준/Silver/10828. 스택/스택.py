# 백준 10828번
import sys
input = sys.stdin.readline
N = int(input())
Stack = []
for i in range(0, N, 1):
    command = input().split()
    if command[0] == 'push':
        Stack.append(command[1])

    if command[0] == 'pop':
        if len(Stack) == 0:
            print(-1)
        else:
            print(Stack[len(Stack)-1])
            del Stack[len(Stack)-1]

    if command[0] == 'size':
        print(len(Stack))

    if command[0] == 'empty':
        if len(Stack) == 0:
            print(1)
        else:
            print(0)

    if command[0] == 'top':
        if len(Stack) == 0:
            print(-1)
        else:
            print(Stack[len(Stack)-1])