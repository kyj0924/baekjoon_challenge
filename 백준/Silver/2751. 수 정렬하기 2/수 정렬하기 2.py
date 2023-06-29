import sys
input = sys.stdin.readline
N = int(input())
numlist = []
for i in range(0, N, 1):
    numlist.append(int(input()))
numlist.sort()
for i in range(0, N, 1):
    print(numlist[i])