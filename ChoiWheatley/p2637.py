"""
장난감 조립

1. 기본부품을 찾는다 -- indegree 개념을 활용해보자
2. DFS 돌리면서 각 곱셈 결과를 더한다
"""

from collections import deque
from sys import stdin


V = int
W = int


def create_indegree(graph: list[list[tuple[V, W]]]) -> list[int]:
    N = len(graph)
    indegrees: list[int] = [0 for _ in range(N)]
    for i in range(N):
        # graph[i] -> [j, k] 일 경우, indegree[j], indegree[k] +=1씩 해준다.
        for j, _ in graph[i]:
            indegrees[j] += 1
    return indegrees


def topological_sort(graph: list[list[tuple[V, W]]]) -> list[int]:
    indegree = create_indegree(graph)
    queue = deque(i for i, x in enumerate(indegree[1:], 1) if x == 0)
    ret = [0]

    while queue:
        cur = queue.popleft()
        ret.append(cur)

        for child, _ in graph[cur]:
            indegree[child] -= 1
            if indegree[child] == 0:
                queue.append(child)

    return ret


def solve(graph: list[list[tuple[V, W]]], needs: list[list[tuple[V, W]]]) -> list[int]:
    N = len(needs) - 1
    topo_ls = topological_sort(graph)  # topo_ls의 마지막 원소는 완제품이다.
    dp = [0 for _ in range(N + 1)]
    dp[topo_ls[N]] = 1

    for i in range(N, 0, -1):
        # 개수 역전파
        node = topo_ls[i]
        for dependency, cnt in needs[node]:
            dp[dependency] += cnt * dp[i]

    return dp


n = int(stdin.readline().strip())
m = int(stdin.readline().strip())
g_graph: list[list[tuple[V, W]]] = [[] for _ in range(n + 1)]  # index starts from 1
g_needs: list[list[tuple[V, W]]] = [[] for _ in range(n + 1)]  # reversed graph

for _ in range(m):
    x, y, k = (int(x) for x in stdin.readline().split())
    # NOTE - y -> x 관계이다
    g_graph[y].append((x, k))
    g_needs[x].append((y, k))

parts = solve(g_graph, g_needs)

for i, x in enumerate(parts[1:], start=1):
    if len(g_needs[i]) == 0:
        print(i, x)
