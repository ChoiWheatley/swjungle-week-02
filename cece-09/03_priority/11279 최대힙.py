import sys
from collections import deque


def heapify(n):  # first index is 1
    for p in range(n//2, 0, -1):
        root = X[p]

        c = p*2
        while c < n:
            if c+1 < n and X[c+1] > X[c]:
                c += 1
            if root > X[c]:
                break
            else:
                X[c//2] = X[c]
                c = c*2
        X[c//2] = root


def heap_push(x):
    X.append(x)  # 배열의 끝에 새 원소 삽입
    c = len(X)-1
    p = c//2
    # 끝부터 parent로 올라가며 child > parent 이면 swap
    while p > 0:
        if X[c] > X[p]:
            X[c], X[p] = X[p], X[c]  # swap
        else:
            break
        c, p = p, p//2


def heap_pop():
    if len(X) == 1:
        return 0

    root = X[1]
    last = X.pop()

    if len(X) == 1:  # 루트를 pop함
        return root

    X[1] = last  # 마지막 원소를 루트로
    p = 1
    c = p*2
    # 루트를 자식과 비교하여 swap
    while c < len(X):
        if c+1 < len(X) and X[c+1] > X[c]:
            c += 1
        if X[c] > X[p]:
            X[p], X[c] = X[c], X[p]
        else:
            break
        p, c = c, c*2

    return root


N = int(input())
X = deque([-1])  # first index is 1

for _ in range(N):
    x = int(sys.stdin.readline())

    if x > 0:
        heap_push(x)
    else:
        root = heap_pop()
        print(root)
