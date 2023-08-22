"""
최소비용 구하기

다익스트라인데, 노드로 향하는 길이 여러개인 것에 불과
"""

from collections import defaultdict
from dataclasses import dataclass, field
from heapq import heappop, heappush
from sys import stdin
from typing import Callable

V = int  # vertex
W = int  # weight


@dataclass(order=True)
class Key:
    vertex: V = field(compare=False)
    weight: W


def dijkstra(
    GRAPH: list[list[tuple[V, W]]], start: V, stop_pred: Callable[[V, W], bool]
) -> dict[V, W]:
    dist: dict[V, W] = defaultdict(W)
    queue = [Key(start, 0)]

    while queue:
        cur = heappop(queue)

        if cur.vertex in dist:
            # 이미 최단거리를 구함
            continue
        # 최단거리를 찾았음
        dist[cur.vertex] = cur.weight

        if stop_pred(cur.vertex, cur.weight):
            break
        # 순회를 돌면서 최소경로 우선 집어넣는다.
        for adj_v, adj_w in GRAPH[cur.vertex]:
            # 주의: 두 노드 사이에 여러 경로가 존재할 수 있음
            weight = cur.weight + adj_w
            heappush(queue, Key(adj_v, weight))

    return dist


def sol(n: int, EDGES: list[tuple[V, V, W]], start: V, end: V) -> W:
    graph: list[list[tuple[V, W]]] = [[] for _ in range(n + 1)]  # index starts from 1
    for s, e, w in EDGES:
        graph[s].append((e, w))

    dist = dijkstra(graph, start, lambda v, w: v == end)

    return dist[end]


if __name__ == "__main__":
    n = int(stdin.readline().strip())
    m = int(stdin.readline().strip())

    edges = [tuple(int(x) for x in stdin.readline().split()) for _ in range(m)]

    s, e = [int(x) for x in stdin.readline().split()]

    print(sol(n, edges, s, e))
