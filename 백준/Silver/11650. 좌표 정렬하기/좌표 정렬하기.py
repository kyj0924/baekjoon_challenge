import sys
input = sys.stdin.readline
N = int(input())
xylist = []
for i in range(0, N, 1):
    x, y = map(int, input().split())
    xylist.append([x, y])
xylist.sort()
for i in range(0, N, 1):
    print(*xylist[i])