"""아침산책

실내 - 실외, 실외, ..., - 실내 코스를 짜달라는데 내가 왜?
"""

from dataclasses import dataclass, field
from typing import List, Self
from sys import stdin


@dataclass
class Node:
    idx: int
    inside: bool = False
    adj: List[Self] = field(default_factory=list)


g_in: List[Node] = []
g_out: List[Node] = []
g_edg: List[List[int]] = [[]]
g_pool: List[Node] = []


def r_walk(node: Node, visited: List[bool]) -> int:
    """node에서 출발할 때 만날 수 있는 다른 실내 node들의 개수를 리턴합니다."""
    res = 0
    for next_ in node.adj:
        if visited[next_.idx]:
            continue
        visited[next_.idx] = True

        if next_.inside:
            res += 1
            continue
        # outside
        res += r_walk(next_, visited)

    return res


if __name__ == "__main__":
    n = int(stdin.readline().strip())

    # init g_****
    g_pool = [Node(i) for i in range(n + 1)]  # ∵ i starts with 1
    s = stdin.readline().strip()
    for i, c in enumerate(s, start=1):
        if c == "1":
            g_pool[i].inside = True
            g_in.append(g_pool[i])
        else:
            g_out.append(g_pool[i])

    # init edges
    for _ in range(n - 1):
        u, v = [int(x) for x in stdin.readline().split()]
        g_pool[u].adj.append(g_pool[v])
        g_pool[v].adj.append(g_pool[u])

    # do solve
    res = 0
    for start in g_in:
        visited = [False for _ in range(n + 1)]
        visited[start.idx] = True
        res += r_walk(start, visited)

    print(res)
