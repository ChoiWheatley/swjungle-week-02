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
    t = set()  # 순환탐지용
    ret = 0  # 가중치합
    G[1:].sort(key=lambda e: e[1])
    for u, v, weight in G[1:]:
        if u in t and v in t:
            # cycle!!!
            continue

        ret += weight
        if u not in t:
            t.add(u)
        if v not in t:
            t.add(v)

    return ret


if __name__ == "__main__":
    V, E = (int(x) for x in stdin.readline().split())
    G: List[Tuple[int, int, int]] = [(maxsize, maxsize, maxsize)]  # 0인덱스는 사용하지 않는다

    for _ in range(E):
        a, b, c = (int(x) for x in stdin.readline().split())
        G.append((a, b, c))

    result = sol(G)
    print(result)
