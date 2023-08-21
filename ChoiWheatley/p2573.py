"""빙산

1. change status
2. find separation
"""

from collections import defaultdict
from sys import stdin
from typing import Dict, List, Set, Tuple

g_delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Glaciers:
    status: List[List[int]]
    yr: int
    N: int
    M: int
    lands: Dict[Tuple[int, int], int]  # 남은 살아있는 빙산들의 {(row, col): height}를 저장하는 배열

    def __init__(self, status: List[List[int]]):
        self.status = status
        self.yr = 0
        self.N = len(status)
        self.M = len(status[0])
        self.lands = defaultdict(int)

        for i in range(self.N):
            for j in range(self.M):
                if status[i][j] > 0:
                    self.lands[(i, j)] = status[i][j]

    def __count_zeros(self, r: int, c: int) -> int:
        """(r,c) 빙산 근처 바다의 수를 센다"""
        count = 0
        for d in g_delta:
            if self.status[r + d[0]][c + d[1]] <= 0:
                count += 1
        return count

    def next_year(self):
        """빙산이 분리, 동서남북 네 방향으로 붙어있는 0이 저장된 칸의 개수만큼 줄어든다"""
        melts: List[Tuple[int, int, int]] = []  # (r, c, amount)

        for i, j in self.lands:
            cnt = self.__count_zeros(i, j)
            if cnt > 0:
                melts.append((i, j, cnt))

        # do subtraction
        # 여기서 또 N * N을 돌지말고 줄일 놈만 따로 저장하는 방법을 고안하자.
        for i, j, amt in melts:
            if self.status[i][j] <= amt:
                self.status[i][j] = 0
                self.lands.pop((i, j))
            else:
                self.status[i][j] -= amt
                self.lands[(i, j)] = self.status[i][j]

        # change year
        self.yr += 1

    def is_separated(self) -> bool:
        """빙산이 적어도 두 조각 이상으로 분리되었는가?

        DFS를 사용하여 탐색하는 건 맞는데 좀 더 빠르게 빙산을 찾을 방법을 구해야 한다.

        visited를 만들지 말고 DFS 순회 하면서 카운트 한 개수가 전체 빙산 개수보다
        적으면 나뉘어진 것이다.
        """
        remain_cnt = len(self.lands)
        land = next(iter(self.lands))
        walk_cnt = self.__walk_dfs(*land)

        return walk_cnt < remain_cnt

    def __walk_dfs(self, r, c) -> int:
        """DFS 순회를 돌면서 단순히 방문한 노드의 개수만 리턴한다."""
        if self.lands.get((r, c)) is None:
            return 0

        visited: Set[Tuple[int, int]] = set()
        stack: List[Tuple[int, int]] = [(r, c)]
        cnt = 0

        while stack:
            r, c = stack.pop()
            is_visited = (r, c) in visited
            if is_visited:
                continue
            visited.add((r, c))

            cnt += 1
            for dy, dx in g_delta:
                r_ = r + dy
                c_ = c + dx

                is_ocean = self.status[r_][c_] == 0
                is_visited = (r_, c_) in visited
                if is_visited or is_ocean:
                    continue

                stack.append((r_, c_))

        return cnt


def sol(gla: Glaciers) -> int:
    # glaciers.remain을 활용하여 굳이 여기에서 또 N*N을 돌 필요 없게 만들어보자.
    while len(gla.lands) > 0:
        if gla.is_separated():
            return gla.yr
        gla.next_year()

    return 0


if __name__ == "__main__":
    n, m = [int(x) for x in stdin.readline().split()]
    status = [[int(x) for x in stdin.readline().split()] for _ in range(n)]
    glaciers = Glaciers(status)

    print(sol(glaciers))
