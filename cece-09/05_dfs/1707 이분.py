'''
What is Bipartite Graph?
인접한 정점끼리 서로 다른 색으로 칠하여 모든 정점을 두 가지 색으로만 칠할 수 있는 그래프
'''
import sys
from collections import deque


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.link = None


def check_bipartite(v: int, color: int):  # 인접 노드를 구합니다
    arr = []
    is_bipartite = True
    next: Node = adj[v].link
    while next != None:
        if not vis[next.data]:
            arr.append(next.data)  # 방문하지 않았으면 방문할 정점으로 추가
        if col[next.data] == color:
            is_bipartite = False  # 이분될 수 없으면
        else:
            col[next.data] = -color  # 이분
        next = next.link
    return arr, is_bipartite


def dfs(s):  # 하나의 connected component에 대해 dfs 탐색을 하며 이분 여부를 체크
    stack = deque()

    stack.append(s)
    col[s] = 1
    while stack:
        node = stack.pop()
        # print(node+1)
        if vis[node] == 0:
            vis[node] = 1
            arr, is_bipartite = check_bipartite(node, col[node])  # 인접 노드
            if not is_bipartite:
                return False
            for a in arr:
                stack.append(a)
    return True


K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    adj = [Node(i) for i in range(V)]
    vis = [0 for _ in range(V)]
    col = [0 for _ in range(V)]

    for _ in range(E):
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

    is_bipartite = True
    for i in range(V):  # 그래프가 모두 연결되어 있지 않은 경우를 고려해야 합니다.
        if vis[i] == 0:
            is_bipartite = dfs(i)
            if is_bipartite == False:
                # print("NO")
                break
    if is_bipartite:
        print("YES")
    else:
        print("NO")
