import sys
input = sys.stdin.readline
N = int(input())
numlist = [0 for i in range(10000)]
for i in range(N):
    num = int(input())
    numlist[num-1] += 1
for j in range(0, 10000, 1):
    if numlist[j] != 0:
        for k in range(0, numlist[j], 1):
            print(j+1)