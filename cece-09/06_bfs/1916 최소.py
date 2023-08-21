from collections import deque
N = int(input())
M = int(input())
adj = [[0 for _ in range(N)] for _ in range(N)]
cost = [[0 for _ in range(N)] for _ in range(N)]
mincost = [-1 for _ in range(N)]

for _ in range(M):
    u, v, c = map(int, input().split())
    adj[u-1][v-1] = 1
    cost[u-1][v-1] = c

s, e = map(int, input().split())


def bfs(s):
    queue = deque()
    queue.append(s)
