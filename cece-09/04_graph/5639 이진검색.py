import sys

# 배열로 다시 풀어볼 것

sys.setrecursionlimit(10**8)  # 없으면 recursion error


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.lchd = None
        self.rchd = None


def insert(n, cnt):
    global head

    node = Node(n)
    if cnt == 0:
        head = node
        return

    curr = head
    while curr != None:
        if curr.data > n:
            next = curr.lchd  # left child
        else:
            next = curr.rchd  # right child
        if next == None:
            break
        curr = next

    if curr.data > n:
        curr.lchd = node
    else:
        curr.rchd = node


def postorder(node: Node):
    if node == None:
        return
    left, right = node.lchd, node.rchd
    postorder(left)
    postorder(right)
    print(node.data)


cnt = 0  # node 개수
head: Node = None  # head node
while True:
    try:
        node = int(sys.stdin.readline())
        insert(node, cnt)
        cnt += 1
    except:
        break

postorder(head)
