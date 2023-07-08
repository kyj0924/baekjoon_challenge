# 백준 2108번
# N은 홀수(1 <= N <= 500,000)
# 산술평균 : N개의 수들의 합을 N으로 나눈값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# 위 4가지 기본 통계값을 구하는 프로그램
import sys
input = sys.stdin.readline
N = int(input())
numlist = [0 for i in range(N)]
for i in range(0, N, 1):
    numlist[i] = int(input())

sum = 0
for i in range(0, len(numlist), 1):
    sum += numlist[i]
avg = round((sum / len(numlist)))

numlist.sort()
center_value = numlist[(int(len(numlist) // 2))]

count_dict = {}
for i in numlist:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1
mode_numlist = []
max_count = max(count_dict.values())
for i in count_dict.keys():
    if count_dict[i] == max_count:
        mode_numlist.append(i)
if len(mode_numlist) == 1:
    mode = mode_numlist[0]
else:
    # count_dict의 key값은 numlist의 요소들인데 이미 순차정렬되어있어서 다시 정렬할 필요는 없다.
    mode = mode_numlist[1]

num_range = numlist[len(numlist)-1] - numlist[0]

print(avg)
print(center_value)
print(mode)
print(num_range)