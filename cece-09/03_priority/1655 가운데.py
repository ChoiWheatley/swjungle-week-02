import sys
from collections import deque

N = int(input())
N = deque([-1])  # 최소힙
X = deque([-1])


def mincmp(x, y):
    return x < y  # 비교함수


def maxcmp(x, y):
    return x > y


def pop(cmp, H):
    if len(H) == 1:
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
        if c+1 < len(X) and cmp(X[c+1], X[c]):
            c += 1
        if cmp(X[c], X[p]):
            X[p], X[c] = X[c], X[p]
        else:
            break
        p, c = c, c*2

    return root


def push(n, cmp, H):
    # min/max heap을 유지하며 push
    c = len(N)
    H.append(n)
    p = c//2
    while p > 0:
        if c+1 < len(H) and cmp(H[c+1],  H[c]):
            c += 1
        if cmp(H[c], H[p]):
            H[c], H[p] = H[p], H[c]
        else:
            break
        c, p = p, p//2
    print(H)


def command(n, k):  # 어느 힙에 push할지 정하기
    # 최소힙, 최대힙 순으로 삽입
    push(n, mincmp, N)
    push(k, maxcmp, X)

    # 만약 최대힙의 루트가 최소힙의 루트보다 크면 swap
    if X[1] > N[1]:
        minroot = pop(mincmp, N)
        maxroot = pop(maxcmp, X)


arr = [5, 1, 3, 2, 6, 8, 9]

push(arr[0], maxcmp, X)
command(arr[1], arr[2])
command(arr[3], arr[4])
command(arr[5], arr[6])

print("max heap: ", X)
print("min heap: ", N)
