# 백준 2485번
import sys
input = sys.stdin.readline
N = int(input())
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
tree_locate = {}
tree_interval = [0 for i in range(N-1)]
for i in range(0, N, 1):
    tree_locate[i] = int(input())
for i in range(0, N-1, 1):
    tree_interval[i] = tree_locate[i+1] - tree_locate[i]
tree_interval = list(set(tree_interval))
min_interval = tree_interval[0]
for i in range(0, len(tree_interval), 1):
    min_interval = gcd(min_interval, tree_interval[i])
all_trees = ((tree_locate[len(tree_locate)-1] - tree_locate[0]) // min_interval) + 1
print(all_trees - N)