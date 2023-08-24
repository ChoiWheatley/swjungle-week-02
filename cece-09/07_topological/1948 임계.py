import sys
from collections import deque
from heapq import heappop, heappush

inf = float('inf')
N = int(input())
M = int(input())
cost = [[inf for _ in range(N)] for _ in range(N)]
indg = [0 for _ in range(N)]


queue = deque()

for _ in range(N):
    u, v, c = map(int, sys.stdin.readline().split())
    cost[u-1][v-1] = c
    indg[v-1] += 1

S, D = map(int, input().split())
for i in range(N):
    if indg[i] == 0:
        queue.append(i)


while queue:
    u = queue.popleft()
    print(u, end=' ')
    for v in range(N):
        if cost[u][v] < inf:
            indg[v] -= 1
            if indg[v] == 0:
                queue.append(v)
