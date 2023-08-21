from collections import deque
N, M, K, X = map(int, input().split())
adj = [[0 for _ in range(N)] for _ in range(N)]
dist = [-1 for _ in range(N)]  # -1은 방문하지 않음, 이후로는 길이를 저장


def bfs(s):
    queue = deque()
    queue.append(s)
    dist[s] = 0  # 시작 노드
    while queue:
        fr = queue.popleft()
        for i in range(N):
            if adj[fr][i] > 0:
                if dist[i] == -1:
                    dist[i] = dist[fr]+1
                    queue.append(i)
                else:
                    dist[i] = min(dist[i], dist[fr]+1)


for i in range(M):
    u, v = map(int, input().split())
    adj[u-1][v-1] = 1  # directed

bfs(X-1)

# print answer
is_K = 0
for i in range(N):
    if dist[i] == K:
        print(i+1)
        is_K = 1
if not is_K:
    print(-1)
