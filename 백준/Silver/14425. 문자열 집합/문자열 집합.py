# 백준 14425번
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
S = [0 for i in range(N)]
Mlist = [0 for i in range(M)]
for i in range(0, N, 1):
    S[i] = input().strip()
for i in range(0, M, 1):
    Mlist[i] = input().strip()
checked_dict = {}
for j in range(0, len(S), 1):
    checked_dict[S[j]] = 0
count = 0
for k in range(0, len(Mlist), 1):
    if Mlist[k] in checked_dict:
        count += 1
print(count)