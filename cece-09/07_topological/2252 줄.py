'''
위상 정렬의 순서
1. 자기 자신을 가리키는 변이 없는 정점을 찾는다
2. 찾은 정점을 출력하고, 출력한 정점과 그 정점에서 출발하는 변을 삭제한다.
3. 아직 그래프에 정점이 남아있으면 1로 돌아가고, 아니면 알고리즘을 종료한다.
'''

from collections import deque


class Node:
    def __init__(self, idx) -> None:
        self.idx = idx
        self.link = None


N, M = map(int, input().split())
graph = [Node(i) for i in range(N)]
indegree = [0 for _ in range(N)]

for i in range(M):
    u, v = map(int, input().split())
    node = Node(v-1)

    if graph[u-1].link != None:
        tmp = graph[u-1].link
        node.link = tmp

    graph[u-1].link = node
    indegree[v-1] += 1


queue = deque()
for i in range(N):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    u = queue.popleft()
    print(f"{u+1}", end=' ')

    node = graph[u].link  # i에서 가는 간선들을 삭제한다
    while node != None:
        v = node.idx
        indegree[v] -= 1
        if indegree[v] == 0:
            queue.append(v)
        node = node.link
print()
