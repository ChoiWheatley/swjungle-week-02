import sys
from collections import deque
from heapq import heappop, heappush

N = int(input())
mtx = [list(map(int, sys.stdin.readline().strip()))for _ in range(N)]
indg = [0 for _ in range(N)]
ans = []


def print_mtx(m):
    for i in range(N):
        for j in range(N):
            print(f"{m[i][j]:4}", end='')
        print()


for i in range(N):
    for j in range(N):
        if mtx[i][j] == 1:
            indg[i] += 1  # 역방향 정렬

queue = []
for i in range(N):
    if indg[i] == 0:
        heappush(queue, -i)

new_order = N-1
while queue:
    curr = -heappop(queue)
    ans.append((curr, new_order))
    new_order -= 1  # 마지막부터 채워 준다

    for i in range(N):
        if mtx[i][curr] == 1:
            indg[i] -= 1
            if indg[i] == 0:
                heappush(queue, -i)

# 정렬될 수 없으면 -1
if sum(indg) > 0:
    print(-1)
    exit()

# 현재 순으로 정렬하고
ans.sort(key=lambda a: a[0])
for a in ans:  # 새로운 순서 수열 출력
    print(a[1]+1, end=' ')
print()
