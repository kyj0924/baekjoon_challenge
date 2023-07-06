# 백준 17103번
# 테스트 케이스의 개수 T
# 정수 N은 짝수이고 2 < N <= 1000000
# N이 주어졌을 때 N에 대한 골드바흐 파티션의 개수
# 소수를 구하고 N보다 작은 소수들 중 2개를 더해서 N이 되는 값의 개수를 찾는다.
# 즉, N보다 작은 소수 a, b가 있다면
# 소수값 리스트에서N보다 작은 a에 대하여 반복하고
# b = N-a 인데 b가 N보다 작은 소수값 리스트에 있는지 확인하고 개수를 세면 된다.
import sys
input = sys.stdin.readline
T = int(input())
prime_dict = {}
prime_dict[1] = False
prime_dict[2] = True
for i in range(3, 1000001, 2): # 소수는 짝수가 안나오니까 홀수로만 구성
    prime_dict[i] = True
for i in range(3, 1000001, 2): # 짝수는 없으니까 홀수만 배수 있는지 검사
    # 홀수+홀수+홀수는 홀수이므로 3배, 5배, 7배 등 홀수의 홀수배 검사
    for j in range(i+i+i, 1000001, i+i):
        prime_dict[j] = False

for i in range(0, T, 1):
    N = int(input())
    count = 0
    for j in range(1, (N//2)+1, 2):
        if N == 4:
            count = 1
            break
        else:
            if prime_dict[j] and prime_dict[N-j]:
                count += 1
    print(count)
