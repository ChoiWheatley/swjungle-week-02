from collections import deque
from heapq import heappop, heappush

N = int(input())
M = int(input())

inf = float('inf')
cost = [[inf for _ in range(N)] for _ in range(N)]
dist = [inf for _ in range(N)]

for _ in range(M):
    u, v, c = map(int, input().split())
    # edge cost가 여러 개 나올 수 있으므로 최솟값으로 저장
    cost[u-1][v-1] = min(cost[u-1][v-1], c)

s, e = map(int, input().split())


def dijkstra(s):
    queue = []
    heappush(queue, (0, s))

    dist[s] = 0  # s to s = 0

    while queue:
        d, u = heappop(queue)

        if dist[u] < d:
            continue  # 최소 거리로 업데이트 할 필요가 없는 경우

        for v in range(N):  # u - v
            if d + cost[u][v] < dist[v]:  # 인접해 있지 않으면 cost/dist는 inf
                dist[v] = d + cost[u][v]
                heappush(queue, (dist[v], v))  # 현재까지의 경로가 가장 짧은 경우를 먼저 검사


dijkstra(s-1)
print(dist[e-1])
