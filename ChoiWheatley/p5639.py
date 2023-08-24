"""이진 검색 트리
"""

from dataclasses import dataclass, field
from itertools import chain
from sys import stdin, stdout, setrecursionlimit
from typing import Iterable, Iterator, Self

setrecursionlimit(10**8)

MAXN = 10_000


@dataclass(order=True)
class Node:
    key: int = field(default=0)
    l: Self | None = field(compare=False, default=None)
    r: Self | None = field(compare=False, default=None)

    def __init__(self, key: int):
        self.key = key


def from_preorder(seq: Iterable[int]) -> Node:
    """
    전위순회(방문, 왼쪽, 오른쪽) 결과를 이용한 이진검색트리 구축
    - return : root node
    """
    it = iter(seq)
    root = Node(next(it))

    for key in it:
        # 항상 루트에서부터 내려간다
        cur = root
        while True:
            if key < cur.key:
                child = cur.l
            else:
                child = cur.r
            if child is None:
                break
            cur = child

        if key < cur.key:
            cur.l = Node(key)
        else:
            cur.r = Node(key)

    return root


def postorder_search(cur: Node) -> Iterator[int]:
    """후위순회(왼쪽, 오른쪽, 방문) 결과를 이터레이터에 chain"""
    it: Iterator[int] = iter([])

    # left
    left = cur.l
    if left:
        it = chain(it, postorder_search(left))

    # right
    right = cur.r
    if right:
        it = chain(it, postorder_search(right))

    # visit
    it = chain(it, [cur.key])

    return it


if __name__ == "__main__":
    seq = (int(stream.strip()) for stream in stdin)
    root = from_preorder(seq)

    for pointer in postorder_search(root):
        stdout.write(str(pointer) + "\n")

"""
50
30
24
5
27
25
26
28
29
45
98
52
60
106
109
108
110
"""
