# 백준 1021번
from collections import deque
N, M = map(int, input().split())
want_position = list(map(int, input().split()))
qu = deque([i for i in range(1, N+1)])

count = 0
for i in want_position:
    while True:
        if qu[0] == i:
            qu.popleft()
            break
        else:
            if qu.index(i) < len(qu)/2:
                while qu[0] != i:
                    qu.append(qu.popleft())
                    count += 1
            else:
                while qu[0] != i:
                    qu.appendleft(qu.pop())
                    count += 1
print(count)