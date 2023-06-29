N = input()
Nlist = []
for i in range(0, len(N), 1):
    Nlist.append(N[i])
Nlist.sort(reverse=True)
sum = ""
for i in range(0, len(Nlist), 1):
    sum += Nlist[i]
print(sum)