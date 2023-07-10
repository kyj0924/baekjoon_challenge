# 백준 1312번
A, B, N = map(int, input().split())
for i in range(N):
    A = (A%B)*10 # 실제 나눗셈을 하듯이 남은 수에 10을 곱해서 나누는 수로 나눈다.
    result = A//B # 나눴을 때 몫이 각 소수자리의 수이다.
print(result)