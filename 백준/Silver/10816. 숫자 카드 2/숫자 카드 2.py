# 10816번
# 숫자카드 N개, 정수 M개
import sys
input = sys.stdin.readline
N = int(input())
Nlist = list(map(int, input().split()))
Ndict = {}
M = int(input())
Mlist = list(map(int, input().split()))
for i in range(0, len(Mlist), 1):
    Ndict[Mlist[i]] = 0
for i in range(0, len(Nlist), 1):
    if Nlist[i] in Ndict:
        Ndict[Nlist[i]] += 1
    else:
        Ndict[Nlist[i]] = 1
for i in range(0, len(Mlist), 1):
    print(Ndict[Mlist[i]], end = " ")