import sys

# Kruskal's

V, E = map(int, sys.stdin.readline().split())
edge = [tuple(map(int, sys.stdin.readline().split())) for _ in range(E)]
edge.sort(key=lambda e: e[2])  # cost 기준 sort

mst = []
parent = [i for i in range(V)]
total_cost = 0


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])  # 가장 parent인 조상을 찾아 연결
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    parent[b] = a


for i in range(E):
    vf, vr, cost = edge[i]
    vf, vr = vf-1, vr-1

    is_cycle = find(vf) == find(vr)

    if not is_cycle:
        mst.append(edge[i])
        total_cost += edge[i][2]
        union(vf, vr)

print(total_cost)
