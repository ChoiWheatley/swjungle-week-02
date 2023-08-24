"""
이분 그래프

임의의 정점을 가지고 모든 노드를 순회할 수 있다면 그 그래프는 이분 그래프가 아닌거네?
"""

from functools import reduce
from typing import Callable, List, Set, Tuple
from sys import stdin

# 연결리스트
g_nodes: List[List[int]] = [[]]


def r_visit(visited: List[bool], idx: int, hook: Callable[[int], None]):
    """단순 DFS 순회"""
    visited[idx] = True
    hook(idx)
    for next in g_nodes[idx]:
        if visited[next]:
            continue
        r_visit(visited, next, hook)


class PingPong:
    sets: Tuple[Set[int], Set[int]] = (set(), set())
    count = 0

    def hook(self, idx: int):
        self.sets[self.count % 2].add(idx)
        self.count += 1


if __name__ == "__main__":
    K = int(stdin.readline().strip())
    for _ in range(K):
        V, E = [int(x) for x in stdin.readline().split()]

        # init g_nodes
        g_nodes = [[] for _ in range(V + 1)]  # ∵ index starts 1
        for _ in range(E):
            u, v = [int(x) for x in stdin.readline().split()]
            g_nodes[u].append(v)
            g_nodes[v].append(u)

        visited = [False for _ in range(V + 1)]
        visited[0] = True

        pingpong = PingPong()
        r_visit(visited, 1, pingpong.hook)
        if len(reduce(lambda acc, set_: acc.intersection(set_), pingpong.sets)) > 0:
            print("NO")
        else:
            print("YES")
