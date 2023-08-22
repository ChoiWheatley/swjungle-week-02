from collections import deque

N, M = map(int, input().split())  # N행 M열
maze = [list(map(int, input())) for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]

# 인접 -> 상하좌우?

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(i, j):
    dist = 1
    queue = deque()
    queue.append((i, j))
    visit[i][j] = 1  # 시작 칸도 포함
    while queue:
        fi, fj = queue.popleft()

        if fi == N-1 and fj == M-1:  # 도착
            print(visit[fi][fj])
            break

        for dir in direct:
            si, sj = fi+dir[0], fj+dir[1]
            if 0 <= si < N and 0 <= sj < M and maze[si][sj] > 0 and visit[si][sj] == 0:
                if visit[si][sj] == 0:
                    visit[si][sj] = visit[fi][fj]+1  # 이전 노드의 길이에서 +1
                    queue.append((si, sj))
                else:
                    visit[si][sj] = min(
                        visit[si][sj], visit[fi][fj]+1)  # 현재까지 최소 길이를 저장


bfs(0, 0)
