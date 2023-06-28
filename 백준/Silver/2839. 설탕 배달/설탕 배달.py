N = int(input())
fivebag = 0
threebag = 0
while N >= 0:
    if N % 5 == 0:
        fivebag = N // 5
        break
    elif N % 5 == 3:
        fivebag = N // 5
        threebag += (N % 5) // 3
        break
    else:
        N -= 3
        threebag += 1
if N < 0:
    print(-1)
else:
    print(fivebag + threebag)