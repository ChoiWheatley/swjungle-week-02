import sys
from collections import deque
from heapq import heappop, heappush

'''
주요 반례
벽을 뚫을 필요가 없는데, 벽을 뚫는 것이 최단거리인 경우
이를 위해 weight이 작은 쪽을 먼저 탐색하는 pq가 필요
5
10111
10101
10101
10101
11101
wrong: 1
right: 0
'''


def bfs(i, j):
    pq = []
    heappush(pq, (0, i, j))  # 필수
    dist[i][j] = 0

    while pq:
        _, fi, fj = heappop(pq)

        for dir in direct:
            di, dj = fi+dir[0], fj+dir[1]
            if 0 <= di < N and 0 <= dj < N:
                if dist[di][dj] == inf:
                    heappush(pq, (dist[fi][fj] + cost[di][dj], di, dj))
                dist[di][dj] = min(dist[di][dj], dist[fi][fj] + cost[di][dj])


inf = float('inf')

N = int(input())
cost = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
dist = [[inf for _ in range(N)] for _ in range(N)]
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(N):
    for j in range(N):
        if cost[i][j] == 1:
            cost[i][j] = 0
        else:
            cost[i][j] = 1  # weight 반전

bfs(0, 0)
print(dist[N-1][N-1])
