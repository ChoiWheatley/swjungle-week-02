from collections import deque


def mincmp(x, y):
    return x < y  # 비교함수


def maxcmp(x, y):
    return x > y


def pop(cmp, H: list):
    if len(H) == 1:
        return 0

    root = H[1]
    last = H.pop()

    if len(H) == 1:  # 루트를 pop함
        return root

    H[1] = last  # 마지막 원소를 루트로
    p = 1
    c = p*2
    # 루트를 자식과 비교하여 swap
    while c < len(H):
        if c+1 < len(H) and cmp(H[c+1], H[c]):
            c += 1
        if cmp(H[c], H[p]):
            H[p], H[c] = H[c], H[p]
        else:
            break
        p, c = c, c*2

    return root


def push(n, cmp, H: list):
    # min/max heap을 유지하며 push
    c = len(H)
    H.append(n)
    p = c//2
    while p > 0:
        if cmp(H[c], H[p]):
            H[c], H[p] = H[p], H[c]
        else:
            break
        c, p = p, p//2
