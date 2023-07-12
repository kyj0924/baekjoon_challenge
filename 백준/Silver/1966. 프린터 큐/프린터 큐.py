# 백준 1966번
import sys
input = sys.stdin.readline
from collections import deque
Testcase = int(input())
for j in range(Testcase):
    doc_number, queue_order = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    count = 0
    while queue:
        best = max(queue)
        front = queue.popleft()
        queue_order -= 1
        if best == front:
            count += 1
            if queue_order < 0:
                print(count)
                break
        else:
            queue.append(front)
            if queue_order < 0:
                queue_order = len(queue) - 1