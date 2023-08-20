"""최소신장트리"""
from typing import List, Tuple
from sys import stdin


MAXE = 100_000
MAXV = 10_000


class NotADisJointSet(Exception):
    ...


def get_parent(disjoint_set: List[int], idx: int) -> int:
    if disjoint_set[idx] == idx:
        # 자기자신이 루트(서로소집합 그 자체)인 경우
        return idx
    return get_parent(disjoint_set, disjoint_set[idx])


def union_parent(disjoint_set: List[int], a, b):
    """두 서로소 집합을 합친다. 만약 서로소 집합이 아닌 경우 에러를 발생시킨다."""
    set_a = get_parent(disjoint_set, a)
    set_b = get_parent(disjoint_set, b)
    if set_a == set_b:
        raise NotADisJointSet()
    if set_a > set_b:
        # 작은 인덱스가 부모가 되도록
        set_a, set_b = set_b, set_a
    disjoint_set[set_b] = set_a


def sol(G: List[Tuple[int, int, int]]) -> int:
    """
    순회를 돌면서 매번 최소 가중치 간선을 찾아 추가하는 알고리즘
    가중치값만 구하면 되므로 최소신장그래프는 작성하지 않는다.

    근데, 순환탐지를 어떻게 하지? => 간선을 추가할 때 중복된 정점이 있다면 순환임.

    근데, 중복된 정점을 어떻게 찾지? => Union Find

    - G: 연결리스트 형식의 그래프, 각 원소는 (시작 정점번호, 인접 정점번호, 가중치)로 이루어져 있다.

    """
    disjoint_set = [i for i in range(MAXV + 1)]  # 순환탐지용
    ret = 0
    G.sort(key=lambda e: e[2])

    for u, v, w in G:
        try:
            union_parent(disjoint_set, u, v)
            ret += w
        except NotADisJointSet:
            continue

    return ret


if __name__ == "__main__":
    V, E = (int(x) for x in stdin.readline().split())
    G: List[Tuple[int, int, int]] = []

    for _ in range(E):
        a, b, c = (int(x) for x in stdin.readline().split())
        G.append((a, b, c))

    result = sol(G)
    print(result)
