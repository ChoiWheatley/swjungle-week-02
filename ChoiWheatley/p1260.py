"""DFS와 BFS"""

from collections import deque
import math
from typing import Any, Generator, List
from sys import stdin

MAXN = 1000
MAXM = 10_000
MAX_BITSET_BUCKET = math.ceil(MAXN / 32)


def bucket_no(idx: int) -> int:
    return idx // MAX_BITSET_BUCKET


def bucket_offset(idx: int) -> int:
    return idx % MAX_BITSET_BUCKET


def bs_get(bs: List[int], idx: int) -> bool:
    return bs[bucket_no(idx)] >> bucket_offset(idx) & 1 == 1


def bs_set(bs: List[int], idx: int, to: bool = True):
    if to:
        bs[bucket_no(idx)] |= 1 << bucket_offset(idx)
    else:
        bs[bucket_no(idx)] ^= 1 << bucket_offset(idx)


def dfs(GRAPH: List[List[int]], start: int) -> Generator[int, Any, Any]:
    if len(GRAPH[start]) == 0:
        yield from ()

    stack = [start]
    visited = [0 for _ in range(MAX_BITSET_BUCKET + 1)]

    while len(stack) > 0:
        cursor = stack.pop()
        is_visited = bs_get(visited, cursor)

        if is_visited:
            continue

        bs_set(visited, cursor)
        yield cursor

        for node in sorted(GRAPH[cursor], reverse=True):
            stack.append(node)


def bfs(GRAPH: List[List[int]], start: int) -> Generator[int, Any, Any]:
    if len(GRAPH[start]) == 0:
        yield from ()

    queue = deque([start])
    visited = [0 for _ in range(MAX_BITSET_BUCKET + 1)]

    while len(queue) > 0:
        cursor = queue.popleft()
        is_visited = bs_get(visited, cursor)

        if is_visited:
            continue

        bs_set(visited, cursor)
        for node in sorted(GRAPH[cursor]):
            queue.append(node)

        yield cursor


if __name__ == "__main__":
    n, m, start = [int(x) for x in stdin.readline().split()]
    graph = [[] for _ in range(n + 1)]  # index starts from 1

    for _ in range(m):
        u, v = [int(x) for x in stdin.readline().split()]
        graph[u].append(v)
        graph[v].append(u)

    print(" ".join((str(x) for x in dfs(graph, start))))
    print(" ".join((str(x) for x in bfs(graph, start))))
