
def floyd_warshall(dist):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

    for i in range(N):
        for j in range(N):
            if dist[i][j] == inf:
                dist[i][j] = 0
            else:
                dist[i][j] = 1  # 갈 수 있다


N, M = map(int, input().split())

inf = float('inf')
X = [[inf for _ in range(N)] for _ in range(N)]
Y = [[inf for _ in range(N)] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    X[u-1][v-1] = 1  # u > v
    Y[v-1][u-1] = 1  # v < u


floyd_warshall(X)
floyd_warshall(Y)

ans = set()
for i in range(N):
    if sum(X[i]) > N//2:  # 왜 반을 초과?
        ans.add(i)
    if sum(Y[i]) > N//2:
        ans.add(i)

# print(ans)
print(len(ans))
