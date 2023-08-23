'''
집과 사무실의 위치 모두 철로 선분에 포함되는 사람들의 수를 최대로
'''

import sys
from heapq import heapify, heappush, heappop


N = int(input())
vtx = [sorted(list(map(int, sys.stdin.readline().split()))) for _ in range(N)]
D = int(input())
vtx.sort(key=lambda v: v[1])  # end를 기준으로 정렬

max_cnt = 0
pq = []
for i in range(N):
    # 가장 시작점이 작은 구간부터 검사
    heappush(pq, vtx[i])
    while pq and pq[0][0] < vtx[i][1]-D:  # 시작점이 끝점-D보다 작으면
        heappop(pq)
    max_cnt = max(max_cnt, len(pq))

print(max_cnt)
