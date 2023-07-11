# 백준 2164번
N = int(input())
from collections import deque
queue = deque([i for i in range(1, N+1, 1)])

while (len(queue) > 1):
        queue.popleft()
        temp = queue.popleft()
        queue.append(temp)
print(queue[0])