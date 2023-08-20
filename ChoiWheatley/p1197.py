"""최소신장트리"""
from typing import List, Tuple
from sys import stdin, maxsize


MAXE = 100_000
MAXV = 10_000


def sol(G: List[Tuple[int, int, int]]) -> int:
    """순회를 돌면서 매번 최소 가중치 간선을 찾아 추가하는 알고리즘
    가중치값만 구하면 되므로 최소신장그래프는 작성하지 않는다.
    근데, 순환탐지를 어떻게 하지? => 간선을 추가할 때 중복된 정점이 있다면 순환임.
    - G: 연결리스트 형식의 그래프, 각 원소는 (시작 정점번호, 인접 정점번호, 가중치)로 이루어져 있다. 1부터 센다.

    """
    parent = [i for i in range(len(G))]  # 순환탐지용
    G[1:].sort(key=lambda e: e[1])
    parent[G[1][1]] = G[1][0]  # 루트노드를 G[1][0]으로 설정한다.
    ret = G[1][2]  # 가중치합
    for u, v, weight in G[2:]:
        if parent[u] == G[1][0] and parent[v] == G[1][0]:
            # cycle!
            continue

        ret += weight

        # 루트노드를 parent로 지정하는 것으로 간편하게 순환검사를 할 수 있다.
        parent[u] = G[1][0]
        parent[v] = G[1][0]

    return ret


if __name__ == "__main__":
    V, E = (int(x) for x in stdin.readline().split())
    G: List[Tuple[int, int, int]] = [(maxsize, maxsize, maxsize)]  # 0인덱스는 사용하지 않는다

    for _ in range(E):
        a, b, c = (int(x) for x in stdin.readline().split())
        G.append((a, b, c))

    result = sol(G)
    print(result)
