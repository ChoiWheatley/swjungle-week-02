"""빙산

1. change status
2. find separation
"""

import sys
from typing import List, Tuple

sys.setrecursionlimit(15000)

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Glaciers:
    status: List[List[int]]
    yr: int
    N: int
    M: int

    def __init__(self, status: List[List[int]], N: int, M: int):
        self.status = status
        self.yr = 0
        self.N = N
        self.M = M

    def __count_zeros(self, r: int, c: int) -> int:
        """(r,c) 빙산 근처 바다의 수를 센다"""
        count = 0
        for d in delta:
            if self.status[r + d[0]][c + d[1]] <= 0:
                count += 1
        return count

    def next_year(self):
        """빙산이 분리, 동서남북 네 방향으로 붙어있는 0이 저장된 칸의 개수만큼 줄어든다"""
        diff = [[0 for _ in range(self.M)] for _ in range(self.N)]

        for i in range(self.N):
            for j in range(self.M):
                if self.status[i][j] > 0:
                    diff[i][j] += self.__count_zeros(i, j)

        # do subtraction
        for i in range(self.N):
            for j in range(self.M):
                self.status[i][j] -= diff[i][j]

        # change year
        self.yr += 1

    def is_separated(self) -> bool:
        """빙산이 적어도 두 조각 이상으로 분리되었는가?"""
        visited = [[True for _ in range(self.M)] for _ in range(self.N)]

        for i in range(self.N):
            for j in range(self.M):
                if self.status[i][j] > 0:
                    visited[i][j] = False

        alive = (0, 0)
        for i in range(self.N):
            for j in range(self.M):
                if self.status[i][j] > 0:
                    alive = i, j

        self.__r_walk(visited, *alive)

        if not all(all(elem for elem in line) for line in visited):
            return True
        return False

    def __r_walk(self, visited: List[List[bool]], r: int, c: int):
        """동서남북 네 방향으로 이동하며 덩어리를 모두 순회한다."""
        if visited[r][c]:
            return
        visited[r][c] = True
        for d in delta:
            r_ = r + d[0]
            c_ = c + d[1]
            if visited[r_][c_]:
                continue
            self.__r_walk(visited, r_, c_)


if __name__ == "__main__":
    n, m = [int(x) for x in input().split()]
    status = [[int(x) for x in input().split()] for _ in range(n)]

    glaciers = Glaciers(status, n, m)

    while not all(all(x <= 0 for x in row) for row in glaciers.status):
        if glaciers.is_separated():
            print(glaciers.yr)
            exit(0)
        glaciers.next_year()

    print(0)
