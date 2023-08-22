import sys
from collections import deque
from heapq import heappop, heappush

# ! 아직 못 푼 문제

inf = float('inf')

N = int(input())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
dist = [[inf for _ in range(N)] for _ in range(N)]
order = [[0 for _ in range(N)] for _ in range(N)]
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(i, j):
    pq = []
    heappush(pq, (-1, i, j))
    dist[i][j] = 0

    # 방문 순서
    cnt = 0
    while pq:
        col, fi, fj = heappop(pq)
        order[fi][fj] = cnt
        cnt += 1
        print(f"({fi}, {fj}) : {'white' if col < 0 else 'black'}")

        if fi == N-1 and fj == N-1:
            break

        for dir in direct:
            di, dj = fi+dir[0], fj+dir[1]
            if 0 <= di < N and 0 <= dj < N:
                color = maze[di][dj]
                if dist[di][dj] == inf:
                    heappush(pq, (-color, di, dj))
                    maze[di][dj] = -1
                dist[di][dj] = min(dist[di][dj], dist[fi][fj]+1)


def print_mtx(mtx):
    for i in range(N):
        for j in range(N):
            print(f"{mtx[i][j]:3}", end=' ')
        print()


bfs(0, 0)
print_mtx(order)
