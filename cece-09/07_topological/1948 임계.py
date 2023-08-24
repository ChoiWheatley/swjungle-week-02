from collections import deque
import sys
from collections import deque

N = int(input())
M = int(input())

graph = [[]*N for _ in range(N)]
backg = [[]*N for _ in range(N)]

indg = [0 for _ in range(N)]
time = [0 for _ in range(N)]  # to get max time

'''
그래프 자료구조는 앞으로 이런 식으로 할 것
class - link는 너무 c스러움
'''
for _ in range(M):
    u, v, c = map(int, sys.stdin.readline().split())
    u, v = u-1, v-1  # index is 0
    graph[u].append((v, c))
    backg[v].append((u, c))
    indg[v] += 1

S, D = map(int, input().split())
S, D = S-1, D-1

queue = deque()
for i in range(N):
    if indg[i] == 0:
        queue.append(i)

while queue:  # topological sort
    u = queue.popleft()

    for v, c in graph[u]:  # u -> v로 가면서 cost의 최대로 갱신
        time[v] = max(time[v], time[u]+c)
        indg[v] -= 1
        if indg[v] == 0:
            queue.append(v)

'''
time은 최대 시간을 저장했으므로
각 정점까지 소요되는 최대 비용이다
즉 임계 경로의 비용이다

따라서 역방향으로 탐색하면서, <v, u>를 탐색했을 때
v의 최대비용이 u의 최대비용 + <v, u> 간선의 비용이라면
(time[v] == time[u]+cost[v][u])
이 간선은 임계 경로에 속한다고 볼 수 있다.
'''
print(time[D])  # 도착점까지 걸리는 최대시간

count = 0
visit = [0 for _ in range(N)]
queue.append(D)

while queue:  # bfs 역방향 탐색
    v = queue.popleft()

    for u, c in backg[v]:
        if time[v] == time[u]+c:
            count += 1
            if visit[u] == 0:
                queue.append(u)
                visit[u] = 1

print(count)
