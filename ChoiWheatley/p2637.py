"""
장난감 조립

1. 기본부품을 찾는다 -- indegree 개념을 활용해보자
2. DFS 돌리면서 각 곱셈 결과를 더한다
"""

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


def dfs(idx: V, pi: int) -> int:
    """
    - pi: 중간값은 곱하고
    - return: 리턴값끼리는 더한다
    """
    global g_graph
    if len(g_graph[idx]) == 0:
        return pi

    adder = 0
    for v, w in g_graph[idx]:
        adder += dfs(v, pi * w)

    return adder


n = int(stdin.readline().strip())
m = int(stdin.readline().strip())
g_graph: list[list[tuple[V, W]]] = [[] for _ in range(n + 1)]  # index starts from 1

for _ in range(m):
    x, y, k = (int(x) for x in stdin.readline().split())
    # NOTE - y -> x 관계이다
    g_graph[y].append((x, k))

indegree = create_indegree(g_graph)

# indegree가 0인 원소들이 바로 기본부품이다. 이 녀석들을 가지고 dfs를 돌려보자.
for idx, degree in enumerate(indegree[1:], start=1):
    if degree == 0:
        amt = dfs(idx, 1)
        print(idx, amt)
