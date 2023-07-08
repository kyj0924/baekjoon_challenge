# 백준 26069번
# 딕셔너리로 이름을 key, 무지개 댄스 또는 노멀을 value로 갖게 한다.
# 이후 모든 key값에 대해서 value가 무지개 댄스인 개수를 count하고 count를 출력한다.
# 테스트 케이스는 N개
# 만나는 사람이 ChongChong인지 아닌지만 확인하면 된다.
# ChongChong이면 상대도 춤을 추게 된다.
# add 함수는 집합에 요소를 추가해준다.
import sys
input = sys.stdin.readline
N = int(input())
Rainbow_Dance = {'ChongChong'} # 집합은 중괄호로 만든다.
for i in range(0, N, 1):
    name1, name2 = map(str, input().strip().split())
    if name1 in Rainbow_Dance:
        Rainbow_Dance.add(name2)
    if name2 in Rainbow_Dance:
        Rainbow_Dance.add(name1)
print(len(Rainbow_Dance))
