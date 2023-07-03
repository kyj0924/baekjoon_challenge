# 백준 1269번(시간단축)
# 집합은 중복되는 값이 들어갈 수 없다.
# set() 함수로 집합을 생성하고 중복되는 값을 없앤다.
# set() 함수로 집합을 생성하면 교집합, 합집합, 차집합 등의 집합끼리의 연산이 가능하다.
import sys
input = sys.stdin.readline
A_num, B_num = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
print(len(A-B) + len(B-A))