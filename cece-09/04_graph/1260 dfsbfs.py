import sys
from collections import deque
from heapq import heappush, heappop


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


def get_adjacents(v: int):
    global vtx, edg
    adj = []
    # front
    if vtx[v].fh != None:
        e = vtx[v].fh  # front edge index
        while e != None:
            vf, vr = edg[e].vf, edg[e].vr  # v1 - v2
            if visit[vr] == 0:
                heappush(adj, vr)
            e = edg[e].fp  # v와 연결된 다른 에지 검색

    # rear
    if vtx[v].rh != None:
        e = vtx[v].rh  # rear edge index
        while e != None:
            vf, vr = edg[e].vf, edg[e].vr   # v1 - v2
            if visit[vf] == 0:
                heappush(adj, vf)
            e = edg[e].rp  # v와 연결된 다른 에지 검색

    rtn = []  # 더 작은 정점
    for _ in range(len(adj)):
        v = heappop(adj)
        rtn.append(v)
    return rtn


def bfs(s):
    queue = deque([])

    queue.append(s)  # 시작노드 방문
    while queue:
        v = queue.popleft()

        if visit[v] == 0:
            visit[v] = 1
            print(v+1, end=' ')

        adj = get_adjacents(v)

        for a in adj:  # 인접 정점을 queue
            queue.append(a)


def dfs(s, cnt):
    global visit

    visit[s] = 1
    print(s+1, end=' ')

    if cnt == N:
        return

    adj = get_adjacents(s)
    for a in adj:
        if visit[a] == 0:
            dfs(a, cnt+1)


# main
N, M, V = map(int, input().split())

vtx = []
edg = []
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

# search
dfs(V-1, 0)
print()

# visit 배열 초기화
for i in range(N):
    visit[i] = 0

bfs(V-1)
print()
