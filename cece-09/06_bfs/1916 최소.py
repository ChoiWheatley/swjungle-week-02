from collections import deque
from heapq import heappop, heappush

N = int(input())
M = int(input())
# adj = [[0 for _ in range(N)] for _ in range(N)]
cost = [[-1 for _ in range(N)] for _ in range(N)]
dist = [-1 for _ in range(N)]

for _ in range(M):
    u, v, c = map(int, input().split())
    # adj[u-1][v-1] = 1
    if cost[u-1][v-1] > c or cost[u-1][v-1] == -1:
        cost[u-1][v-1] = c  # edge cost가 여러 개 나올 수 있으므로 최솟값으로 저장

s, e = map(int, input().split())


def dijkstra(s):
    queue = deque()
    queue.append(s)
    dist[s] = 0  # s to s = 0
    # print(f"[{s+1}]", end=' ')

    while queue:
        fr = queue.popleft()
        # print(f"- {fr+1}", end=' ')
        adj_nodes = []
        for i in range(N):
            if cost[fr][i] >= 0:
                if -1 < dist[i] <= dist[fr] + cost[fr][i]:
                    continue  # 이미 최소 거리인 경우
                if dist[i] == -1:  # 방문하지 않은 인접노드 중 weight이 가장 작은 것부터 탐색
                    heappush(adj_nodes, (cost[fr][i], i))
                dist[i] = dist[fr] + cost[fr][i]

        while adj_nodes:
            min_weight = heappop(adj_nodes)
            queue.append(min_weight[1])

    # print("\n-- mincost --")
    # for i in range(N):
    #     print(f"[{i+1}] {mincost[i]}")


if s == e:
    print(0)
else:
    dijkstra(s-1)
    print(dist[e-1])
