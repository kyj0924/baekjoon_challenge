# 백준 13909번
# N은 실습실의 창문 개수이자 현재 실습실 내의 사람 수
# k번째 사람은 k의 배수번째 창문이 열려있으면 닫고, 닫혀있으면 연다.
# 처음에는 모든 창문이 닫혀있고 k번 실행해서 마지막에 열려있는 창문 개수는 몇개인가?
# 딕셔너리로 key가 1부터 k까지 value를 0으로 구성하고 열때는 1로 닫을때는 0으로 바꾼다.
'''N = int(input())
open_close_dict = {}
for i in range(1, N+1, 1):
    open_close_dict[i] = 0
for i in range(1, N+1, 1):
    for j in range(i, N+1, i): # 1의 배수~N의 배수까지 창문 여닫기
        if open_close_dict[j] == 0:
            open_close_dict[j] = 1
        else:
            open_close_dict[j] = 0
count = 0
for i in range(1, N+1, 1):
    if open_close_dict[i] == 1:
        count += 1
print(count)'''

# 위 코드는 메모리 초과가 발생함.
# 위 코드를 1부터 25까지 반복해본 결과 N의 제곱근의 정수값 만큼 창문이 열려있음
# 따라서 값을 구하는 코드를 간소화 하면 다음 코드와 같다.
N = int(input())
answer = int(N**(0.5))
print(answer)