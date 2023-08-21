"""이진 검색 트리

이진 검색 트리를 전위 순회한 결과가 주어졌을 때, 이 트리를 후위 순회한 결과를 구하는 프로그램을 작성하세요

이진검색트리를 배열에 선언, 0부터 인덱싱. 왼쪽 자식은 i * 2 + 1, 오른쪽 자식은 i * 2 + 2, 부모는 
홀수인 경우 i // 2, 짝수인 경우 (i // 2) - 1
"""


from typing import Iterable, Iterator
from sys import stdin, stdout
from itertools import chain

g_tree = [-1 for _ in range(10_000 * 3)]


def l(i):
    return (i << 1) + 1


def r(i):
    return (i << 1) + 2


def p(i):
    if i == 0:
        return i
    if i & 1 == 1:
        return i >> 1
    return (i >> 1) - 1


def from_preorder(seq: Iterable[int]) -> None:
    """
    전위순회 (방문, 왼쪽, 오른쪽) 결과를 활용한 이진검색트리 구축
    - return: 순회를 마친 뒤의 seq_idx
    """
    cursor = 0  # tree를 자유자재로 돌아다닐 커서
    it = iter(seq)

    # initial visit
    g_tree[cursor] = next(it)

    for node in it:
        if node < g_tree[cursor]:
            # left child
            cursor = l(cursor)
            g_tree[cursor] = node
        else:
            # right child일 수도 있고 parent의 right child일 수도 있고
            # parent.parent의 right child 일 수도 있고..
            while cursor > 0 and node > g_tree[p(cursor)]:
                cursor = p(cursor)
            cursor = r(cursor)
            g_tree[cursor] = node


def postorder_search(idx: int) -> Iterator[int]:
    """후위순회(left, right, visit) 결과를 이터레이터에 모두 chain"""
    it: Iterator[int] = iter([])
    # left
    if g_tree[l(idx)] != -1:
        it = chain(it, postorder_search(l(idx)))
    # right
    if g_tree[r(idx)] != -1:
        it = chain(it, postorder_search(r(idx)))
    it = chain(it, [g_tree[idx]])
    return it


if __name__ == "__main__":
    seq = (int(stream.strip()) for stream in stdin)
    from_preorder(seq)
    for node in postorder_search(0):
        stdout.write(str(node) + "\n")
