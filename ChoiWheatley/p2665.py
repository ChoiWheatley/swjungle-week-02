"""
미로만들기

막혀있는 미로를 최소한으로 뚫어 연결된 미로를 만들고자 할 때 뚫어야 할 최소한의 방의 수

하얀방의 비용 = 0, 검은방의 비용 = 1로 놓고 다익스트라
"""

from dataclasses import dataclass, field
from heapq import heappop, heappush
from sys import maxsize
from typing import Self

MAXN = 50
BUCKET_BITS = 32
MAX_BUCKET_SIZE = (MAXN * MAXN) // BUCKET_BITS + 1

INF = maxsize


@dataclass(order=True)
class Pos:
    r: int
    c: int

    def __add__(self, rhs: Self) -> Self:
        return Pos(self.r + rhs.r, self.c + rhs.c)

    def __eq__(self, other: Self) -> bool:
        return self.r == other.r and self.c == other.c

    def __hash__(self) -> int:
        return self.r * MAXN + self.c


class Bitset2D:
    bs: list[int]

    def __init__(self) -> None:
        self.bs = [0 for _ in range(MAX_BUCKET_SIZE)]

    @classmethod
    def bucket_no(cls, idx: int) -> int:
        return idx // BUCKET_BITS

    @classmethod
    def bucket_offset(cls, idx: int) -> int:
        return idx % BUCKET_BITS

    def get(self, idx: int) -> bool:
        return self.bs[self.bucket_no(idx)] >> self.bucket_offset(idx) & 1 == 1

    def set(self, idx: int, to: bool = True):
        if to:
            self.bs[self.bucket_no(idx)] |= 1 << self.bucket_offset(idx)
        else:
            self.bs[self.bucket_no(idx)] ^= 1 << self.bucket_offset(idx)

    def get2d(self, row: int, col: int, M: int) -> bool:
        idx = row * M + col
        return self.get(idx)

    def set2d(self, row: int, col: int, M: int, to: bool = True):
        idx = row * M + col
        self.set(idx, to)


@dataclass(order=True)
class Key:
    pos: Pos = field(compare=False)
    weight: int


g_delta = (Pos(0, 1), Pos(1, 0), Pos(0, -1), Pos(-1, 0))


def sol(start: Pos, end: Pos, MAZE: Bitset2D, N: int) -> int:
    """
    start에서 end로 갈 수 있는 최소비용을 리턴한다.

    그래프의 모양은 단순히 인접해 있기만 하면 연결되어있는 것
    """
    dist: list[list[int | None]] = [[None for _ in range(N)] for _ in range(N)]
    queue: list[Key] = [Key(start, 0)]

    while queue:
        cur = heappop(queue)

        # 최단거리를 찾았다.
        dist[cur.pos.r][cur.pos.c] = cur.weight

        for d in g_delta:
            adj = cur.pos + d

            if not (0 <= adj.r < N and 0 <= adj.c < N):
                continue
            if dist[adj.r][adj.c] != None:
                continue

            # 검은방(0)인 경우 비용이 1, 하얀방(1)인 경우 비용이 0
            adj_w = cur.weight + (0 if MAZE.get2d(adj.r, adj.c, N) else 1)
            heappush(queue, Key(adj, adj_w))

    ret = dist[end.r][end.c]
    if ret:
        return ret
    return maxsize


def from_str2d(lines: list[str], COL: int) -> Bitset2D:
    ret = Bitset2D()

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "1":
                ret.set2d(i, j, COL)

    return ret


if __name__ == "__main__":
    n = int(input())
    lines = [input() for _ in range(n)]
    graph = from_str2d(lines, n)

    print(sol(Pos(0, 0), Pos(n - 1, n - 1), graph, n))
