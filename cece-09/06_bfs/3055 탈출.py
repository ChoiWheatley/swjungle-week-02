import sys
from collections import deque


def move(path: deque):  # 1분간 갈 수 있는 모든 좌표를 큐에 넣고 반환
    new_path = deque()
    while path:
        a, b = path.popleft()
        for dir in direct:
            x, y = a+dir[0], b+dir[1]
            if 0 <= x < R and 0 <= y < C:
                if mtx[x][y] == '.':
                    mtx[x][y] = 'S'
                    new_path.append((x, y))
                if mtx[x][y] == 'D':
                    return True  # 도착함

    return new_path


def flood(water: deque):  # 1분간 물에 잠기는 모든 새로운 좌표를 큐에 넣고 반환
    new_water = deque()
    while water:
        a, b = water.popleft()

        for dir in direct:
            x, y = a+dir[0], b+dir[1]
            if 0 <= x < R and 0 <= y < C:
                if mtx[x][y] == '.' or mtx[x][y] == 'S':
                    mtx[x][y] = '*'
                    new_water.append((x, y))
    return new_water


R, C = map(int, input().split())
mtx = [['.' for _ in range(C)] for _ in range(R)]
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 입력 받기
S, D = (0, 0), (0, 0)
water = deque()
movin = deque()
for i in range(R):
    j = 0
    for stat in sys.stdin.readline().strip():
        if stat == '*':
            water.append((i, j))  # 물이 있는 곳만 조사
        if stat == 'S':
            S = (i, j)
            movin.append((i, j))  # 고슴도치의 경로 조사
        if stat == 'D':
            D = (i, j)

        mtx[i][j] = stat
        j += 1


minute = 0
while water or movin:  # 물이 있는 경우
    water = flood(water)  # 물이 먼저 가고

    minute += 1
    movin = move(movin)  # 고슴도치가 간다

    if movin == True:
        print(minute)
        exit()

    if not movin and mtx[D[0]][D[1]] == 'D':
        print('KAKTUS')
        exit()
