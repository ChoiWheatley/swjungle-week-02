"""특정 거리의 도시 찾기

모든 건물간의 거리가 1인 도시에서 최단거리 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력하시오
"""

from collections import defaultdict
from dataclasses import dataclass, field
from heapq import heappop, heappush
from sys import stdin
from typing import Any, Any, Generator

V = int  # vertex
W = int  # weight


@dataclass(order=True)
class Key:
    vertex: V = field(compare=False)
    weight: W


def dijkstra(GRAPH: list[list[V]], start: V) -> dict[V, W]:
    queue: list[Key] = [Key(start, 0)]
    dist: dict[V, W] = defaultdict(W)

    while queue:
        cursor = heappop(queue)

        if cursor.vertex in dist:
            # 이미 찾은 거리
            continue

        # 최단거리를 찾았다.
        dist[cursor.vertex] = cursor.weight

        # 인접노드들을 검사
        for adj in GRAPH[cursor.vertex]:
            weight = cursor.weight + 1  # 1만큼 먼 건물이기 때문
            heappush(queue, Key(adj, weight))

    return dist


def sol(n: int, EDGES: list[tuple[V, V]], start: V, k: W) -> Generator[V, Any, Any]:
    graph = [[] for _ in range(n + 1)]  # index starts from 1
    for s, e in EDGES:
        graph[s].append(e)
        graph[e].append(s)
    dist = dijkstra(graph, start)

    filtered = [v for v, w in dist.items() if w == k]
    if len(filtered) == 0:
        yield -1
        return

    yield from filtered


if __name__ == "__main__":
    n, m, k, x = [int(x) for x in stdin.readline().split()]
    edges = [tuple(int(x) for x in stdin.readline().split()) for _ in range(m)]

    for v in sol(n, edges, x, k):
        print(v)
