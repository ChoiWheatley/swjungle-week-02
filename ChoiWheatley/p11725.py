"""
트리의 부모 찾기
"""

from dataclasses import dataclass, field
from sys import stdin, stdout
from typing import List, Self


@dataclass
class Node:
    idx: int
    children: List[Self] = field(default_factory=list)
    parent: Self | None = None


MAXN = 100_000
POOL = tuple(Node(i) for i in range(MAXN + 1))
# 연결 여부를 조사하는 이차원 배열
MAT = [[False for _ in range(MAXN + 1)] for _ in range(MAXN + 1)]


def r_init(node: Node, N: int):
    """1번 노드가 루트임을 알고 있기 때문에 재귀적으로 부모 자식관계를 식별할 수 있다."""
    my_parent = node.parent
    for j in range(N):
        # 부모노드를 제외한 나머지를 순회하며 자식노드를 식별
        if j == node.idx or (my_parent is not None and my_parent == node.idx):
            continue
        if MAT[j][node.idx] or MAT[node.idx][j]:
            child = POOL[j]
            node.children.append(child)
            child.parent = node
            r_init(child, N)


if __name__ == "__main__":
    n = int(stdin.readline().strip())
    # init MAT
    for _ in range(n - 1):
        x, y = [int(x) for x in stdin.readline().split()]
        MAT[x][y] = MAT[y][x] = True
    r_init(POOL[1], n)
