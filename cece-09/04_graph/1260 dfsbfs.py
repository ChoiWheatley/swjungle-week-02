import sys
from collections import deque


class Node:
    def __init__(self) -> None:
        self.fh = None  # 이 vertex로 시작하는 마지막 edge index
        self.rh = None  # 이 vertex로 끝나는 마지막 edge index


class Edge:
    def __init__(self, vf, vr) -> None:
        self.vf = vf  # 시작 vertex index
        self.vr = vr  # 종료 vertex index
        self.fp = None  # vf 가 같은 연결된 에지
        self.rp = None  # vr 가 같은 연결된 에지


def dfs(v):
    global vtx, edg
    visit[v] = 1  # 시작노드 방문
    # cnt = 0

    # front side
    node = vtx[v]
    edge = edg[node.fh]
    while edge != None:
        vf = edge.vf
        if vf != None and visit[vf] == 0:
            visit[vf] = 1
            print(vf)
            edge = vtx[vf].fh


N, M, V = map(int, input().split())

vtx: list[Node] = []
edg: list[Edge] = []
visit = [0 for _ in range(N)]

# data structure
for v in range(N):
    node = Node()
    vtx.append(node)

for i in range(M):
    vf, vr = map(int, sys.stdin.readline().split())

    edge = Edge(vf-1, vr-1)  # index 0부터

    if vtx[vf-1].fh != None:
        edge.fp = vtx[vf-1].fh
    if vtx[vr-1].rh != None:
        edge.rp = vtx[vr-1].rh

    vtx[vf-1].fh = i
    vtx[vr-1].rh = i
    edg.append(edge)


dfs(V-1)
