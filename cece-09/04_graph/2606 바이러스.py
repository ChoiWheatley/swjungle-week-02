'''
1번 컴퓨터와 조상이 같은 정점의 수 출력
'''

import sys


def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])  # top top 조상
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    parent[b] = a


N = int(input())
E = int(input())
parent = [i for i in range(N)]

for _ in range(E):
    u, v = map(int, sys.stdin.readline().split())
    union(u-1, v-1)

virus = find(0)  # 1번 컴퓨터의 조상
cnt = 0

for i in range(1, N):
    if find(i) == virus:
        cnt += 1
print(cnt)
