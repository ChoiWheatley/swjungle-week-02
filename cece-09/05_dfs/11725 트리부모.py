import sys
from collections import deque


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.link = None


def get_adj(v: int):  # 인접 노드를 구합니다
    arr = []
    next: Node = adj[v].link
    while next != None:
        if not vis[next.data]:
            arr.append(next.data)  # 방문하지 않았으면 방문할 정점으로 추가
        next = next.link
    return arr


def dfs(s):  # dfs 탐색을 하며 부모 노드를 정합니다
    stack = deque()

    stack.append(s)
    while stack:
        node = stack.pop()
        if vis[node] == 0:
            vis[node] = 1
            arr = get_adj(node)  # 인접 노드
            for a in arr:
                parent[a] = node
                stack.append(a)


N = int(input())
adj = [Node(i) for i in range(N)]  # vertex 배열
vis = [0 for _ in range(N)]
parent = [i for i in range(N)]

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


dfs(0)


for i in range(1, N):
    print(parent[i] + 1)
