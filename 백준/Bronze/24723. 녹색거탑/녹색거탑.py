# 백준 24723번
# 1층일때 경우의 수 2
# 2층일때 4
# 3층일때 8
# 4층일때 16
# N층일때 2**N개
N = int(input())
number_of_cases = 2**N
print(number_of_cases)