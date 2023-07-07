# 백준 1037번
# N에 대하여 1과 자기 자신을 제외한 약수가 모두 주어질때 N의 값을 구하라.
# 주어진 약수 중에서 가장 큰 값과 가장 작은값을 서로 곱하면 N의 값을 알 수 있다.
import sys
input = sys.stdin.readline
count = int(input())
measure_list = list(map(int, input().split()))
min_measure = measure_list[0]
max_measure = measure_list[0]
for i in range(0, len(measure_list), 1):
    if measure_list[i] <= min_measure:
        min_measure = measure_list[i]
    if measure_list[i] >= max_measure:
        max_measure = measure_list[i]
N = min_measure*max_measure
print(N)
