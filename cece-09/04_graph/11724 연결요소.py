'''
Connected Componenet의 개수 구하기
disjoint set
union & find 
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


N, M = map(int, input().split())
parent = [i for i in range(N)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    union(u-1, v-1)

# 조상이 다른 수를 탐색
T = set()
for i in range(N):
    p = find(i)
    if not p in T:
        T.add(p)


print(len(T))
