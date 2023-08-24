"""
트리의 부모 찾기

1과 연결된 간선을 시작으로 정점을 추가해가며 부모자식 관계를 정의하여야 한다.
"""

from sys import stdin
from typing import List
from collections import deque


def sol(GRAPH: List[List[int]], parent_out: List[int]):
    """1과 연결된 간선부터 출발, BFS?"""
    queue = deque([1])
    visited = [False for _ in range(len(parent_out))]

    while len(queue) > 0:
        cursor = queue.popleft()
        if visited[cursor]:
            continue
        visited[cursor] = True

        adjacent = GRAPH[cursor]
        my_parent = parent_out[cursor]

        for node in adjacent:
            if node != my_parent:
                parent_out[node] = cursor

        queue.extend(adjacent)


if __name__ == "__main__":
    n = int(stdin.readline().strip())
    parent = [i for i in range(n + 1)]  # 1 start
    graph = [[] for _ in range(n + 1)]

    for u, v in [[int(x) for x in stdin.readline().split()] for _ in range(n - 1)]:
        graph[u].append(v)
        graph[v].append(u)

    sol(graph, parent)

    for i in parent[2:]:
        print(i)
