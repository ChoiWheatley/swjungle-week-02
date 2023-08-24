import sys


class Node:
    def __init__(self) -> None:
        self.fh = None  # 이 vertex로 시작하는 마지막 edge index
        self.rh = None  # 이 vertex로 끝나는 마지막 edge index


class Edge:
    def __init__(self, vf, vr, c) -> None:
        self.vf = vf  # 시작 vertex index
        self.vr = vr  # 종료 vertex index
        self.fp = None  # vf 가 같은 연결된 에지
        self.rp = None  # vr 가 같은 연결된 에지
        self.cost = c  # 에지 코스트


V, E = map(int, input().split())
vtx: list[Node] = []
edg: list[Edge] = []

# data structure
for v in range(V):
    node = Node()
    vtx.append(node)

for i in range(E):
    vf, vr, c = map(int, sys.stdin.readline().split())

    edge = Edge(vf-1, vr-1, c)  # index 0부터

    if vtx[vf-1].fh != None:
        edge.fp = vtx[vf-1].fh
    if vtx[vr-1].rh != None:
        edge.rp = vtx[vr-1].rh

    vtx[vf-1].fh = i
    vtx[vr-1].rh = i
    edg.append(edge)
