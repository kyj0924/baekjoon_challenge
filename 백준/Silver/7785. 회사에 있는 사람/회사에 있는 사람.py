import sys
input = sys.stdin.readline
n = int(input())
nameinoutdict = {}
for i in range(0, n, 1):
    name, inout = map(str, input().split())
    if inout == 'enter':
        nameinoutdict[name] = inout
    else:
        del nameinoutdict[name]
nameinoutdict = sorted(nameinoutdict, reverse=True)
for i in nameinoutdict:
    print(i)