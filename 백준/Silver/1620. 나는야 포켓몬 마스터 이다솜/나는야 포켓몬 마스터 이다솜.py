# 백준 1620번
# 포켓몬의 개수 N
# 맞춰야하는 문제의 개수 M
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
Pocketmondict = {}
rev_Pocketmondict = {}
problemdict = {}
for i in range(1, N+1, 1):
    temp1 = input().strip()
    Pocketmondict[i] = temp1
    rev_Pocketmondict[temp1] = i
for i in range(1, M+1, 1):
    temp2 = input().strip()
    if (temp2.isdigit()) == True:
        print(Pocketmondict[int(temp2)])
    else:
        print(rev_Pocketmondict[temp2])