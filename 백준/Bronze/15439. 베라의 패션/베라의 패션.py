# 백준 15439번
# 상의 N벌, 하의 N벌이 있고 각각의 색상은 모두 다르다.
# 서로 다른 색상인 조합은 N*N - N가지
N = int(input())
not_duplicate = N*N - N
print(not_duplicate)