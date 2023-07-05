# 백준 4948번(시간 단축 시도)
# 1<=n<=123456 이므로 2*n+1의 최댓값은 123456*2+1 이다.
import sys
input = sys.stdin.readline
numlist = [True for i in range((123456*2)+1)]
m = int((2*123456)**(0.5))
for i in range(2, m+1, 1):
            for j in range(i+i, (123456*2)+1, i):
                numlist[j] = False
while True:
    n = int(input())
    if n == 0:
        break
    elif n == 1:
        print(1)
    else:
        count = 0
        for i in range(n+1, (2*n)+1, 1):
            if numlist[i] == True:
                count += 1
        print(count)