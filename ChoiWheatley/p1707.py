"""
이분 그래프

임의의 정점을 가지고 모든 노드를 순회할 수 있다면 그 그래프는 이분 그래프가 아닌거네?
"""

from typing import List
from sys import stdin

# 연결리스트
g_nodes: List[List[int]] = [[]]


def r_visit(visited: List[bool], idx: int):
    """단순 DFS 순회"""
    visited[idx] = True
    for next in g_nodes[idx]:
        if visited[next]:
            continue
        r_visit(visited, next)


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
        r_visit(visited, 1)
        # 순회가 끝났는데 하나라도 visited가 True가 아니라면 이건 이분 그래프가 가능하다.
        print("YES" if all(visited) else "NO")
