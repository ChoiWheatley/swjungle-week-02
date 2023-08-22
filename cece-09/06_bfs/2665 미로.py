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


# def find_white(i, j):
#     # (i, j)에서 가장 가까이에 있는 흰 방을 찾음
#     black_cnt = 0
#     queue = deque()
#     queue.append((i, j))
#     dist2[i][j] = 0
#     while queue:
#         fi, fj = queue.popleft()

#         if (fi != i or fj != j) and maze[fi][fj] == 1:
#             print(fi, fj, ":", dist2[fi][fj])
#             break

#         for dir in direct:
#             di, dj = fi+dir[0], fj+dir[1]
#             if 0 <= di < N and 0 <= dj < N:
#                 if dist2[di][dj] == inf:
#                     queue.append((di, dj))
#                 dist2[di][dj] = min(dist2[di][dj], dist2[fi][fj]+1)
#                 # if (di != i or dj != j) and maze[fi][fj] == 1:
#                 #     print(di, dj)
#                 #     return


def bfs(i, j):
    pq = []
    heappush(pq, (-1, i, j))
    dist[i][j] = 0
    # 검색하면서 최대로 갈 수 있는 좌표를 저장
    max_dist_coord = (0, 0)
    max_dist = 0

    # 방문 순서
    cnt = 0
    while pq:
        col, fi, fj = heappop(pq)
        order[fi][fj] = cnt
        cnt += 1
        print(f"({fi}, {fj}) : {'white' if col < 0 else 'black'}")

        if dist[fi][fj] > max_dist:
            max_dist_coord = (fi, fj)
            max_dist = dist[fi][fj]

        for dir in direct:
            di, dj = fi+dir[0], fj+dir[1]
            if 0 <= di < N and 0 <= dj < N:
                color = maze[di][dj]
                if dist[di][dj] == inf:
                    heappush(pq, (-color, di, dj))
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
# find_white(4, 1)
print_mtx(order)
