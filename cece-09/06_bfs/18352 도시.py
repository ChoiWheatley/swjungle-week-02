from collections import deque


class Node:
    def __init__(self, idx) -> None:
        self.idx = idx
        self.link = None


N, M, K, X = map(int, input().split())
vtx = [Node(i) for i in range(N)]
dist = [-1 for _ in range(N)]  # -1은 방문하지 않음, 이후로는 길이를 저장


def bfs(s):
    queue = deque()
    queue.append(s)
    dist[s] = 0  # 시작 노드
    while queue:
        fr = queue.popleft()

        next = vtx[fr].link
        while next != None:
            v = next.idx
            if dist[v] == -1:
                dist[v] = dist[fr]+1
                queue.append(v)
            elif dist[v] < dist[fr]:
                next = next.link
                # min(dist[v], dist[fr]+1) 로 하면 시간초과 뜸.
                # 그럴 필요가 없는 경우 pass하는 쪽으로 구현할 것
                continue
            next = next.link


for i in range(M):  # adjacency list
    u, v = map(int, input().split())
    node = Node(v-1)
    if vtx[u-1].link != None:
        tmp = vtx[u-1].link
        node.link = tmp
    vtx[u-1].link = node

bfs(X-1)

# print answer
is_K = 0
for i in range(N):
    if dist[i] == K:
        print(i+1)
        is_K = 1
if not is_K:
    print(-1)
