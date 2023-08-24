'''
서로 다른 경로의 수
실내 - 실외 - 실외 - ... - 실외 - 실내
'''
from collections import deque
import sys


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.link = None


def get_adj(v: int):  # 인접 노드를 구합니다
    arr = []
    next: Node = adj[v].link
    while next != None:
        if not vis[next.data]:
            # 방문하지 않았으면 방문할 정점으로 추가, 실내/외 정보 저장
            arr.append((next.data, A[next.data]))
        next = next.link
    return arr


def dfs(s):  # dfs 탐색을 하며 s노드에서 시작하여 갈 수 있는 경로 수를 체크
    stack = deque()
    cnt = 0  # in-out-in으로 이어지는 경로 수
    stack.append((s, A[s]))  # 시작점은 항상 실내여야 합니다
    while stack:
        node, is_in = stack.pop()
        if node != s and is_in == 1:
            cnt += 1
            continue
        if vis[node] == 0:
            vis[node] = 1
            arr = get_adj(node)  # 인접 노드
            for a in arr:
                stack.append(a)
    return cnt


N = int(input())
A = list(map(int, input()))
adj = [Node(i) for i in range(N)]
vis = [0 for _ in range(N)]

# 인접 리스트 자료구조
for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    u_node = Node(u-1)
    v_node = Node(v-1)

    if adj[u-1].link != None:
        tmp = adj[u-1].link
        v_node.link = tmp

    if adj[v-1].link != None:
        tmp = adj[v-1].link
        u_node.link = tmp

    adj[u-1].link = v_node
    adj[v-1].link = u_node

# 탐색 실행
# 모든 실내 점마다 dfs를 돌린다
cnt = 0
for i in range(N):
    if A[i] == 1:
        cnt += dfs(i)
        vis = [0 for _ in range(N)]

print(cnt)
