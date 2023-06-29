import sys
input = sys.stdin.readline
N = int(input())
xylist = []
for i in range(0, N, 1):
    x, y = map(int, input().split())
    xylist.append([y, x])
xylist.sort()
for j in range(0, len(xylist), 1):
    temp = 0
    temp = xylist[j][0]
    xylist[j][0] = xylist[j][1]
    xylist[j][1] = temp
for k in range(0, len(xylist), 1):
    print(*xylist[k])