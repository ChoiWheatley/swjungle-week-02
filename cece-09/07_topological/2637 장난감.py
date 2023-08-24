from collections import deque


class Node:
    def __init__(self, idx, cost) -> None:
        self.idx = idx
        self.cost = cost
        self.link = None


N = int(input())
M = int(input())

graph = [Node(i, 0) for i in range(N)]
needs = [0 for _ in range(N)]

indg = [0 for _ in range(N)]
outdg = [0 for _ in range(N)]

for u in range(M):
    x, y, k = map(int, input().split())
    x, y = x-1, y-1  # first index = 0
    node = Node(y, k)  # x -> y

    if graph[x].link != None:
        tmp = graph[x].link
        node.link = tmp

    graph[x].link = node
    indg[y] += 1
    outdg[x] += 1

queue = deque()
for u in range(N):
    if indg[u] == 0:
        queue.append(u)
    if u == N-1:  # 완제품은 1개 필요함
        needs[u] = 1

while queue:
    u = queue.popleft()
    next = graph[u].link
    while next:  # out 노드들을 처리
        v = next.idx
        needs[v] += needs[u] * next.cost

        indg[v] -= 1  # 만약 in 간선이 없으면
        if indg[v] == 0:
            queue.append(v)
        next = next.link


for i in range(N):
    # if outdg[i] == 0:
    print(i+1, needs[i])
