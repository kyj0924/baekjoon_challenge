# 백준 11050번
# 자연수 N, 정수 K가 주어졌을 때 이항계수를 구한다.
# 1 <= N <= 10
# 0 <= K <= N
def factorial(a):
    if a <= 1:
        return 1 
    else:
        return a*factorial(a-1)

N, K = map(int, input().split())
binomial_coefficient = factorial(N) // (factorial(K)*factorial(N-K))
print(binomial_coefficient)