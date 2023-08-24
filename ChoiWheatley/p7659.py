"""
도마도
"""

from collections import deque
from sys import stdin
from typing import List


class Domado:
    status: List[List[List[int]]]
    R: int
    C: int
    H: int
    day: int
    unriped: set[tuple[int, int, int]]  # 익지 않은 도마도를 저장
    queue: deque[tuple[int, int, int]]  # 곧 익을 도마도를 저장
    cnt_empty: int

    DELTA = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

    def __init__(self, status: List[List[List[int]]]):
        self.status = status
        self.H = len(status)
        self.R = len(status[0])
        self.C = len(status[0][0])
        self.day = 0
        self.unriped = set()
        self.queue = deque()
        self.cnt_empty = 0

        for h in range(self.H):
            for r in range(self.R):
                for c in range(self.C):
                    if self.status[h][r][c] > 0:
                        self.queue.append((h, r, c))
                    elif self.status[h][r][c] == 0:
                        self.unriped.add((h, r, c))
                    else:
                        self.cnt_empty += 1

    def next_day(self) -> deque[tuple[int, int, int]]:
        """도마도를 1일간 익힌다"""
        tmp_riped = deque()  # 하루동안 숙성된 토마토를 저장하는 배열
        while self.queue:
            h, r, c = self.queue.popleft()

            for dh, dr, dc in self.DELTA:
                h_ = h + dh
                r_ = r + dr
                c_ = c + dc
                if not (0 <= h_ < self.H and 0 <= r_ < self.R and 0 <= c_ < self.C):
                    continue
                if self.status[h_][r_][c_] != 0:
                    continue
                if (h_, r_, c_) in self.unriped:
                    tmp_riped.append((h_, r_, c_))
                    self.unriped.remove((h_, r_, c_))
                    self.status[h_][r_][c_] = 1
        self.day += 1
        return tmp_riped

    def solve(self) -> int:
        """완숙 도마도가 상하좌우앞뒤 여섯 방향으로 안 익은 도마도에게 영향을 준다.
        이때 토마토가 모두 익거나 더 이상 익힐 토마토가 없을때까지 걸리는 시간을 리턴한다."""
        if len(self.queue) == 0:
            # 처음부터 익은 토마토가 없음
            return -1
        if len(self.unriped) == 0:
            # 처음부터 익은 토마토만 있음
            return 0

        while self.queue:
            cnt_before = len(self.unriped)
            self.queue = self.next_day()
            cnt_after = len(self.unriped)

            if cnt_before == cnt_after:
                return -1
            if len(self.unriped) == 0:
                return self.day
        # 토마토가 다 익지 못하는 위치에 있음
        return -1


if __name__ == "__main__":
    m, n, h = [int(x) for x in stdin.readline().split()]
    status = [[[] for _ in range(n)] for _ in range(h)]

    for height in range(h):
        for row in range(n):
            status[height][row].extend([int(x) for x in stdin.readline().split()])

    print(Domado(status).solve())
