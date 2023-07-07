# 1010번
# 경우의 수는 M*(M-1)*(M-2)*...*(M-N+1) // N!
import sys
input = sys.stdin.readline
T = int(input())
def factorial(a):
    if a <= 1:
        return 1 
    else:
        return a*factorial(a-1)
for i in range(T):
    N, M = map(int, input().split())
    Mcal = M
    for i in range(1, N, 1):
        Mcal = Mcal*(M-i)
    Ncal = factorial(N)
    number_of_cases = Mcal // Ncal
    print(number_of_cases)