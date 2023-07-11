# 백준 11866번
from collections import deque
N, K = map(int, input().split())
sitted_person = deque()
for i in range(1, N+1, 1):
    sitted_person.append(i)
yoseputh = []
while sitted_person:
    for i in range(K-1):
        sitted_person.append(sitted_person.popleft())
    yoseputh.append(sitted_person.popleft())
print("<", end = '')
print(', '.join(map(str, yoseputh)), end = '')
print(">")