import sys

N = int(input())
T = [sys.stdin.readline() for _ in range(N)]
node = []
left = []
right = []

# 자료구조
for i in range(N):
    node.append(T[i].split()[0])

for i in range(N):
    l, r = T[i].split()[1], T[i].split()[2]
    left.append(node.index(l) if l != '.' else -1)
    right.append(node.index(r) if r != '.' else -1)


def preorder(i):  # i 를 루트로 하는 트리 검색
    if i == -1:
        return
    print(node[i], end='')
    preorder(left[i])
    preorder(right[i])


def inorder(i):
    if i == -1:
        return
    inorder(left[i])
    print(node[i], end='')
    inorder(right[i])


def postorder(i):
    if i == -1:
        return
    postorder(left[i])
    postorder(right[i])
    print(node[i], end='')


preorder(0)
print()
inorder(0)
print()
postorder(0)
print()
