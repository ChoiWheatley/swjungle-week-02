"""
미로탐색

BFS 탐색과 메모이제이션?

"""

from collections import deque
from typing import Deque, List, Tuple
from sys import stdin


MAXN = 100
BUCKET_BITS = 32
MAX_BUCKET_SIZE = (MAXN * MAXN) // BUCKET_BITS + 1


def bucket_no(idx: int) -> int:
    return idx // BUCKET_BITS


def bucket_offset(idx: int) -> int:
    return idx % BUCKET_BITS


def bs_get(bs: List[int], idx: int) -> bool:
    return bs[bucket_no(idx)] >> bucket_offset(idx) & 1 == 1


def bs_set(bs: List[int], idx: int, to: bool = True):
    if to:
        bs[bucket_no(idx)] |= 1 << bucket_offset(idx)
    else:
        bs[bucket_no(idx)] ^= 1 << bucket_offset(idx)


def bs_2d_get(bs: List[int], row: int, col: int, M: int) -> bool:
    idx = row * M + col
    return bs_get(bs, idx)


def bs_2d_set(bs: List[int], row: int, col: int, M: int, to: bool = True):
    idx = row * M + col
    bs_set(bs, idx, to)


g_delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # S, E, N, W


def sol(maze: List[int], N: int, M: int) -> int:
    """
    - maze: flatten 2-d bitset array"""
    w_tbl = [[0 for _ in range(M)] for _ in range(N)]

    queue: Deque[Tuple[int, int]] = deque([(0, 0)])
    w_tbl[0][0] = 1

    while queue:
        i, j = queue.popleft()
        w_cur = w_tbl[i][j]

        for dy, dx in g_delta:
            i_ = i + dy
            j_ = j + dx
            if not (0 <= i_ < N and 0 <= j_ < M and bs_2d_get(maze, i_, j_, M)):
                continue

            is_visited = w_tbl[i_][j_] > 0
            if is_visited:
                continue

            # visit adjacent node
            w_tbl[i_][j_] = w_cur + 1
            queue.append((i_, j_))

    return w_tbl[N - 1][M - 1]


def str2maze(lines: List[str], N: int, M: int) -> List[int]:
    ret = [0 for _ in range(MAX_BUCKET_SIZE + 1)]

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "1":
                bs_2d_set(ret, i, j, M)

    return ret


input = stdin.readline

if __name__ == "__main__":
    N, M = [int(x) for x in input().split()]
    lines = [input().strip() for _ in range(N)]
    maze = str2maze(lines, N, M)
    print(sol(maze, N, M))
