
import sys

N, M = map(int, input().split())  # N행 M열
sea = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우


def melt():  # 한 번 녹임
    melt_cnt = 0
    delete = []

    for i in range(N):
        for j in range(M):
            sea_cnt = 0  # 상하좌우에 바다가 얼마나 있는지
            if sea[i][j] > 0:
                for dir in direct:
                    si, sj = i+dir[0], j+dir[1]
                    if 0 <= si < N and 0 <= sj < M and sea[si][sj] == 0:
                        sea_cnt += 1
                delete.append((i, j, sea_cnt))

    while delete:  # sea배열 반영은 한번에 처리
        i, j, c = delete.pop()
        if sea[i][j] <= c:
            sea[i][j] = 0
            melt_cnt += 1
        else:
            sea[i][j] -= c

    return melt_cnt


def dfs(i, j):
    global visit

    cnt = 0
    stack = []
    stack.append((i, j))
    visit[i][j] = 1

    while stack:
        p, q = stack.pop()
        cnt += 1
        for dir in direct:
            ai, aj = p+dir[0], q+dir[1]
            if 0 <= ai < N and 0 <= aj < M and sea[ai][aj] > 0 and visit[ai][aj] == 0:
                stack.append((ai, aj))
                visit[ai][aj] = 1
    return cnt


def do_dfs(visit):  # 탐색 결과 방문한 노드 수 반환, 노드가 없으면 0
    for i in range(N):
        for j in range(M):
            if sea[i][j] > 0:
                return dfs(i, j)
    return 0


# 탐색
visit = [[0 for _ in range(M)] for _ in range(N)]
remain = do_dfs(visit)
answer = 0

while remain > 0:
    visit = [[0 for _ in range(M)] for _ in range(N)]  # visit 초기화

    remain -= melt()
    answer += 1
    visited_cnt = do_dfs(visit)

    if visited_cnt == 0:
        print(0)
        break
    if visited_cnt < remain:
        print(answer)
        break
