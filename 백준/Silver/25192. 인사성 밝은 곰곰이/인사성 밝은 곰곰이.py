# 백준 25192번
# "ENTER" 이후에 처음 채팅을 친사람은 곰곰티콘을 사용하고 이외에는 일반 채팅이다.
# 곰곰티콘 사용횟수를 구하라.
# "ENTER"를 기준으로 나눠서 각각 리스트를 만들고 각각의 리스트를 set로 중복을 제거한다.
# 그 후 각 리스트의 길이를 모두 더한다.
import sys
input = sys.stdin.readline
N = int(input())
person_list = ["ENTER" for i in range(N)]
ENTER_index = []
answer_list = []
for i in range(N):
    person_list[i] = input().strip()

for i in range(0, len(person_list), 1):
    if person_list[i] == "ENTER":
        ENTER_index.append(i)

lensum = 0
for i in range(0, len(ENTER_index), 1):
    if (i+1) < len(ENTER_index):
        lensum += len(set(person_list[(ENTER_index[i]+1):(ENTER_index[i+1])]))
    else:
        lensum += len(set(person_list[(ENTER_index[i]+1):]))

print(lensum)