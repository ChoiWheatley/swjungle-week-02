import sys
from collections import deque


def tomato(ripen: deque):  # 토마토를 1일간 익힌다
    news = deque()
    while ripen:  # 익은 토마토를 중심으로 검색하며 익을 토마토를 news 큐에 넣음
        a, b, c = ripen.popleft()

        for dir in direct:
            dx, dy, dz = a+dir[0], b+dir[1], c+dir[2]

            if 0 <= dx < H and 0 <= dy < N and 0 <= dz < M:
                if box[dx][dy][dz] == 0:
                    news.append((dx, dy, dz))
                    box[dx][dy][dz] = 1
    return news


M, N, H = map(int, input().split())

box = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
direct = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
queue = deque()

# 입력 받으면서 익은 토마토를 큐에 넣는다
z, p, n = 0, 0, 0
for i in range(H):
    for j in range(N):
        k = 0
        for status in list(map(int, sys.stdin.readline().split())):
            if status == 0:
                z += 1
            elif status == 1:
                p += 1
                queue.append((i, j, k))
            else:
                n += 1
            box[i][j][k] = status
            k += 1

if len(queue) == 0:
    # 토마토가 없음
    print(-1)
    exit()

if len(queue) == H*N*M-n:
    print(0)
    exit()


year = 0
while queue:
    news = tomato(queue)
    prev = p
    p += len(news)
    year += 1

    if p >= (H*N*M-n):  # 모두 익음
        print(year)
        exit()

    elif prev == p:  # 모두 익을 수 없음
        print(-1)
        exit()

    queue = news
