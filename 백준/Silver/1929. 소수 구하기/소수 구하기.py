# 백준 1929번
# M 이상 N 이하의 소수를 모두 출력하는 프로그램
M, N = map(int, input().split())
seive = [True for i in range(N+1)]
prime_num_list = []
n = N**(0.5)
seive[1] = False
if N > 1:
    for i in range(2, N+1, 1):
        for j in range(i+i, N+1, i):
            seive[j] = False
for i in range(M, N+1, 1):
    if seive[i] == True:
        print(i)