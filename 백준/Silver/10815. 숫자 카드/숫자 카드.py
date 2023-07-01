# 백준 10815번
# 숫자카드 N개, 카드는 서로 다른 수들
# 정수 M개가 주어졌을때 이 수가 적혀있는 숫자카드를 가지고 있는지 구하는 프로그램
N = int(input())
Nlist = list(map(int, input().split()))
M = int(input())
Mlist = list(map(int, input().split()))
checked_dict = {}
for i in range(0, len(Nlist), 1):
    checked_dict[Nlist[i]] = 0
for j in range(0, len(Mlist)):
    if Mlist[j] not in checked_dict:
        print(0, end=' ')
    else:
        print(1, end=' ')