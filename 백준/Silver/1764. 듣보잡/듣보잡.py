# 백준 1764번
# 듣도 못한 사람 수 N
# 보도 못한 사람 수 M
# 듣도 보도 못한 사람 명단 구하기
N, M = map(int, input().split())
Ndict = {}
for i in range(0, N, 1):
    Ndict[i] = input()
Mdict = {}
for i in range(0, M, 1):
    Mdict[input()] = 0
namelist = []
count = 0
for i in range(0, len(Ndict), 1):
    if Ndict[i] in Mdict:
        count += 1
        namelist.append(Ndict[i])
namelist.sort()
print(count)
for i in range(0, len(namelist), 1):
    print(namelist[i])