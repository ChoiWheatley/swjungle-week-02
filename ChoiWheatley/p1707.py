"""
이분 그래프

https://ko.wikipedia.org/wiki/%EC%9D%B4%EB%B6%84_%EA%B7%B8%EB%9E%98%ED%94%84

> 그래프의 꼭짓점들을 DFS로 나열한 뒤, 각 꼭짓점들을 이웃 꼭짓점들과 다른 색으로 계속해서 칠해 나가면서, 같은 색깔의 꼭짓점이 서로 연결되어 있는 모순이 발생하는지 여부를 확인하면 된다.
"""

from typing import List
from sys import stdin, setrecursionlimit

setrecursionlimit(10**8)

# 연결리스트
g_nodes: List[List[int]] = [[]]


def r_visit(visited: List[bool], idx: int, flag: bool):
    """단순 DFS 순회"""
    visited[idx] = True
    g_colors[idx] = flag

    for next in g_nodes[idx]:
        if visited[next]:
            continue
        r_visit(visited, next, not flag)


def check_bipartite() -> bool:
    for idx, adjs in enumerate(g_nodes[1:], start=1):
        for adj in adjs:
            if g_colors[idx] == g_colors[adj]:
                return False
    return True


if __name__ == "__main__":
    K = int(stdin.readline().strip())
    for _ in range(K):
        V, E = [int(x) for x in stdin.readline().split()]

        # init g_nodes
        g_nodes = [[] for _ in range(V + 1)]  # ∵ index starts 1
        g_colors = [False for _ in range(V + 1)]

        for _ in range(E):
            u, v = [int(x) for x in stdin.readline().split()]
            g_nodes[u].append(v)
            g_nodes[v].append(u)

        visited = [False for _ in range(V + 1)]
        visited[0] = True

        r_visit(visited, 1, True)

        print("YES" if check_bipartite() else "NO")
