"""철로

끝점으로 정렬, 시작점을 기준으로 minheap에 추가하며 heap_top이 D를 초과하지는 않는지 검사하고 그때그때 이동하면서 D 길이를 초과하는 선분들을 빼준다.
"""

from heapq import heappop, heappush
from sys import maxsize, stdin
from typing import Iterable, Self


class Line:
    start: int
    end: int
    orderby_end: bool = True

    def __init__(self, start: int, end, orderby_end=True) -> None:
        if start > end:
            start, end = end, start
        self.start = start
        self.end = end
        self.orderby_end = orderby_end

    def __lt__(self, other: Self) -> bool:
        if self.orderby_end:
            if self.end == other.end:
                return self.start < other.start
            return self.end < other.end
        if self.start == other.start:
            return self.end < other.end
        return self.start < other.start


def sol(lines: Iterable[tuple[int, int]], D: int) -> int:
    """D 길이의 철로를 설치해 가장 많은 사람들의 집과 사무실을 모두 포함할 수 있게 만들어주세요"""
    queue: list[Line] = []
    maxcnt = -maxsize

    for line in sorted(Line(s, e, orderby_end=True) for s, e in lines):
        line.orderby_end = False
        heappush(queue, line)

        while queue and queue[0].start < line.end - D:
            heappop(queue)

        maxcnt = max(maxcnt, len(queue))

    return maxcnt


if __name__ == "__main__":
    n = int(stdin.readline().strip())
    lines = [tuple(int(x) for x in stdin.readline().split()) for _ in range(n)]
    d = int(stdin.readline().strip())

    print(sol(lines, d))
