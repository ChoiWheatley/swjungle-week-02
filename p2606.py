"""disjoint set 찾는문제"""


def find(parent, a):
    """재귀적으로 자신이 속한 집합의 루트를 찾아 갱신까지 해준다."""
    if a == parent[a]:
        return a
    parent[a] = find(parent, parent[a])
    return parent[a]


def union(parent, a, b):
    """a, b 중 루트의 크기가 작은 서로소 집합으로 합병한다."""
    a = find(parent, a)
    b = find(parent, b)
    if a > b:
        a, b = b, a
    parent[b] = a


if __name__ == "__main__":
    N = int(input())
    E = int(input())
    parent = [i for i in range(N + 1)]  # 1부터
    for u, v in ((int(x) for x in input().split()) for _ in range(E)):
        union(parent, u, v)

    # refresh parent

    for i in range(N + 1):
        parent[i] = find(parent, i)

    print(len([e for e in parent if e == 1]) - 1)
