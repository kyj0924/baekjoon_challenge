# 백준 13241번
import sys
input = sys.stdin.readline
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
A, B = map(int, input().split())
max_measure = gcd(A, B)
min_multiple = A*B // max_measure
print(min_multiple)