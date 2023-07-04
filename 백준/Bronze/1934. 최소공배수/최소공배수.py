# 백준 1934번
# 두 수 A, B의 최소 공배수는 A*B / (두 수의 최대공약수) 이다.
import sys
input = sys.stdin.readline
T = int(input())
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
for i in range(T):
    A, B = map(int, input().split())
    max_measure = gcd(A, B)
    min_multiple = A*B // max_measure
    print(min_multiple)