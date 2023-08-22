import sys
from collections import deque

inf = float('inf')
N = int(input())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
dist = [[inf for _ in range(N)] for _ in range(N)]
dist2 = [[inf for _ in range(N)] for _ in range(N)]
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def find_white(i, j):
    # (i, j)에서 가장 가까이에 있는 흰 방을 찾음
    black_cnt = 0
    queue = deque()
    queue.append((i, j))
    while queue:
        fi, fj = queue.popleft()

        if (fi != i or fj != j) and maze[fi][fj] == 1:
            break

        for dir in direct:
            di, dj = fi+dir[0], fj+dir[1]
            if 0 <= di < N and 0 <= dj < N:
                if dist2[di][dj] == inf:
                    queue.append((di, dj))
                dist2[di][dj] = min(dist2[di][dj], dist2[fi][fj]+1)


def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    dist[i][j] = 0
    # 검색하면서 최대로 갈 수 있는 좌표를 저장
    max_dist_coord = (0, 0)
    max_dist = 0
    while queue:
        fi, fj = queue.popleft()

        if dist[fi][fj] > max_dist:
            max_dist_coord = (fi, fj)
            max_dist = dist[fi][fj]

        for dir in direct:
            di, dj = fi+dir[0], fj+dir[1]
            if 0 <= di < N and 0 <= dj < N and maze[di][dj] == 1:
                if dist[di][dj] == inf:
                    queue.append((di, dj))
                dist[di][dj] = min(dist[di][dj], dist[fi][fj]+1)

    print(max_dist_coord, ":", max_dist)
    return max_dist_coord


def print_mtx(mtx):
    for i in range(N):
        for j in range(N):
            print(f"{mtx[i][j]:3}", end=' ')
        print()


# print_mtx(maze)
bfs(0, 0)
print_mtx(dist)
