from dataclasses import dataclass
from functools import total_ordering
from typing import List, Self, Tuple
from sys import stdin

STUB_START = int(-2e9)
STUB_END = int(2e9)


@dataclass
@total_ordering
class Circle:
    x: int  # 중심점
    r: int  # 반지름

    @classmethod
    def from_pq(cls, p: int, q: int) -> Self:
        """start, end포인트로 새 원을 생성한다."""
        if p > q:
            p, q = q, p
        x = (p + q) // 2
        r = (q - p) // 2
        return Circle(x, r)

    def get_pq(self) -> Tuple[int, int]:
        x = self.x
        r = self.r
        return x - r, x + r

    def get_start(self) -> int:
        return self.x - self.r

    def get_end(self) -> int:
        return self.x + self.r

    def is_overlap(self, other: Self) -> bool:
        """내 안에 other가 들어가는지."""
        p, q = self.get_pq()
        return p <= other.x <= q and other.r <= self.r

    def __lt__(self, other: Self) -> bool:
        """원의 왼쪽 끝점을 가지고 비교한다."""
        return self.x - self.r < other.x - other.r

    def __eq__(self, other: Self) -> bool:
        return self.x == other.x and self.r == other.r


g_arr: List[Circle] = []


def r_sol(circle: Circle) -> int:
    """[start, end] 구간 안에 들어있는 가장 큰 원들을 식별하고 재귀를 돌린다."""
    stack: List[Circle] = []
    sum_ = 1
    for cur in g_arr:
        if circle == cur:
            continue
        if not circle.is_overlap(cur):
            continue
        if len(stack) > 0 and stack[-1].is_overlap(cur):
            # top원이 새로운 원을 감싸는 경우 넣지 말아야 한다.
            continue
        while len(stack) > 0 and cur.is_overlap(stack[-1]):
            # 새로운 원이 top원을 감싸는 경우 stack을 교체하여야 한다.
            stack.pop()
        stack.append(cur)
    if len(stack) == 0:
        # 애초에 비어있던 원이므로 중단조건에 해당한다.
        return 1
    if sum([c.r for c in stack]) == circle.r:
        # 내부에 있는 원이 현재 원을 가득 채우기 때문에 영역이 한개 더 생긴다.
        sum_ += 1

    for child_circle in stack:
        sum_ += r_sol(child_circle)

    return sum_


if __name__ == "__main__":
    n = int(stdin.readline().strip())
    for _ in range(n):
        x, r = [int(y) for y in stdin.readline().strip().split()]
        g_arr.append(Circle(x, r))

    # 가상의 가장 큰 원을 기준으로 재귀를 돌린다
    stub = Circle.from_pq(STUB_START, STUB_END)

    print(r_sol(stub))
