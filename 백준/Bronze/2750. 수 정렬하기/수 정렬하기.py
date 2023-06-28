N = int(input())
Nlist = [0 for i in range(N)]
for i in range(0, N, 1):
    Nlist[i] = int(input())
Nlist.sort()
for j in range(0, N, 1):
    print(Nlist[j])