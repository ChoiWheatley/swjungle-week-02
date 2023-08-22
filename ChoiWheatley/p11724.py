"""연결 요소의 개수

그냥 visited가 전부 True가 될 때까지 순회 돌고, 순회가 끊기면 cnt 1 증가하고 그렇게 하면 되나?

> 아니다, 서로소 집합 개념을 활용하면 된다.

union_disjoint을 할 때 하나만 갱신하면 안된다. 재귀적으로 parent를 타고 올라가며 dsj_set을 계속 갱신해주어야 한다.
"""

from typing import List
from sys import stdin


def get_disjoint_parent(dsj_set: List[int], idx: int) -> int:
    """idx가 어느 서로소 집합에 포함되어있는지를 검사한다."""
    if dsj_set[idx] == idx:
        # root-self
        return idx

    dsj_set[idx] = get_disjoint_parent(dsj_set, dsj_set[idx])
    return dsj_set[idx]


def union_disjoint(dsj_set: List[int], lhs: int, rhs: int) -> int:
    """두 서로소 집합 dsj_set[lhs], dsj_set[rhs]를 병합한다.
    - return: 병합한 후 서로소집합의 루트"""
    set_a = get_disjoint_parent(dsj_set, lhs)
    set_b = get_disjoint_parent(dsj_set, rhs)

    if set_b < set_a:
        # 작은 인덱스가 더 위로 올라간다.
        set_a, set_b = set_b, set_a
    dsj_set[set_b] = set_a

    return set_a


if __name__ == "__main__":
    N, M = [int(x) for x in stdin.readline().split()]
    disjoint_set = [i for i in range(N + 1)]  # ∵ N starts from 1
    for _ in range(M):
        u, v = [int(x) for x in stdin.readline().split()]
        union_disjoint(disjoint_set, u, v)

    cnt = 1
    set_ = set()
    for root in disjoint_set[1:]:
        set_.add(get_disjoint_parent(disjoint_set, root))

    print(len(set_))
