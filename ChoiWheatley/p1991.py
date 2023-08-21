from dataclasses import dataclass
from typing import Self


@dataclass
class Node:
    """A가 0번 인덱스, Z가 25번 인덱스"""

    idx: int
    left: Self | None = None
    right: Self | None = None

    def alpha(self):
        return Node.int2alpha(self.idx)

    @classmethod
    def int2alpha(cls, i: int) -> str:
        return chr(i + 65)

    @classmethod
    def alpha2int(cls, a: str) -> int:
        return ord(a) - 65


g_tree = [Node(i) for i in range(26)]


def preorder_search(node: Node) -> str:
    """visit -> left -> right"""
    if node.left is None and node.right is None:
        return node.alpha()
    ret = node.alpha()
    if node.left:
        ret += preorder_search(node.left)
    if node.right:
        ret += preorder_search(node.right)
    return ret


def inorder_search(node: Node) -> str:
    """left -> visit -> right"""
    if node.left is None and node.right is None:
        return node.alpha()
    ret = ""
    if node.left:
        ret += inorder_search(node.left)
    ret += node.alpha()
    if node.right:
        ret += inorder_search(node.right)
    return ret


def postorder_search(node: Node) -> str:
    """left -> right -> visit"""
    if node.left is None and node.right is None:
        return node.alpha()
    ret = ""
    if node.left:
        ret += postorder_search(node.left)
    if node.right:
        ret += postorder_search(node.right)
    ret += node.alpha()
    return ret


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        p, l, r = input().split()
        g_tree[Node.alpha2int(p)].left = None if l == "." else g_tree[Node.alpha2int(l)]
        g_tree[Node.alpha2int(p)].right = (
            None if r == "." else g_tree[Node.alpha2int(r)]
        )
    print(preorder_search(g_tree[0]))
    print(inorder_search(g_tree[0]))
    print(postorder_search(g_tree[0]))
