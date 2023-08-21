'''
만약 connected 가 아니면 break
그래프의 절단점이 될 수 있는 점을 찾는다
1. spt를 만듦
2. non-tree edge를 통해 하부노드에서 상부노드로 갈 수 있으면 절단점 X
'''
import sys
from collections import deque


class Node:
    def __init__(self, i, j, h) -> None:
        self.i = i
        self.j = j
        self.h = h
        self.link = None


def print_vtx():
    for v in range(V):
        print(f"[{v:2} ({vtx[v].i}, {vtx[v].j}, {vtx[v].h})]", end=' ')
        next = vtx[v].link
        while next != None:
            print(f"- ({next.i}, {next.j}, {next.h})", end=' ')
            next = next.link
        print()


def get_adj(v: int):  # 인접 노드를 구합니다
    global vtx
    arr = []
    low = V  # 인접한 정점 중 최소의 방문 순서 (가장 빨리 방문)
    next: Node = vtx[v].link

    while next != None:
        next_key = sea[next.i][next.j]
        if not vis[next_key]:
            arr.append(next_key)  # 방문하지 않았으면 방문할 정점으로 추가
        else:
            low = min(low, vis[next_key])
        next = next.link
    return arr, low


def dfs_cut(s):  # 절단점 찾기
    global vtx
    stack = deque()

    stack.append(s)
    order = 1
    while stack:
        node = stack.pop()
        if vis[node] == 0:
            vis[node] = order

            print(node, end=' ')
            arr, low = get_adj(node)  # 인접 노드
            if order <= low:
                # 서브트리에 상위 노드와 연결된 노드가 없다
                cut.append(node)
            for a in arr:
                stack.append(a)
            order += 1
    print()


N, M = map(int, input().split())  # N행 M열
sea = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


# 자료구조 구성
vtx: list[Node] = []
cnt = 0
for i in range(N):
    for j in range(M):
        if sea[i][j] > 0:
            node = Node(i, j, sea[i][j])
            vtx.append(node)
            sea[i][j] = cnt  # 배열에는 정점 번호를 저장
            cnt += 1

V = len(vtx)
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
for v in range(V):
    i, j = vtx[v].i, vtx[v].j
    node = vtx[v]

    for dir in direct:
        si, sj = i+dir[0], j+dir[1]
        if 0 <= si < N and 0 <= sj < M and sea[si][sj] > 0:
            # 상하좌우에 빙산이 있으면
            new_node = Node(si, sj, sea[si][sj])
            node.link = new_node
            node = new_node

# 탐색
vis = [0 for _ in range(V)]
cut = []
dfs_cut(0)
print(vis)
print(cut)
