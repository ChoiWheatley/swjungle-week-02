from dataclasses import dataclass
from sys import stdin
from typing import Self


@dataclass
class Circle:
    end: int
    diameter: int

    @property
    def x(self) -> int:
        return self.end - self.r

    @property
    def r(self) -> int:
        return self.diameter // 2

    @property
    def start(self) -> int:
        return self.end - self.diameter

    @classmethod
    def from_xr(cls, x: int, r: int) -> Self:
        end = x + r
        diameter = r * 2
        return Circle(end, diameter)

    def __lt__(self, other: Self) -> bool:
        """end, diameter를 기준으로 내림차순 정렬"""
        if self.end == other.end:
            return self.diameter < other.diameter
        return self.end < other.end


def sol(circles: list[Circle]) -> int:
    """원들이 만들어내는 영역의 개수를 계산하세요"""
    stack: list[Circle] = []
    result = 1

    for cur in circles:
        last_end = cur.end

        while stack:
            prev = stack.pop()
            if prev.start >= cur.start and prev.end == last_end:
                # prev가 cur의 내부에 있다. end, diameter 순으로 정렬을 했기 때문에
                # prev.start < cur.start인 경우는 cur 밖에 있게된다.
                # cur.end서부터 연속적으로 내부 원들이 서로 내접해 있는경우
                last_end = prev.start
            elif prev.start < cur.start:
                # prev가 cur의 외부에 있다 => 검사를 포기하되, 스택을 다시 돌려놓자
                stack.append(prev)
                break

        stack.append(cur)

        if last_end == cur.start:
            # 내부 원들이 외부 원을 가득 메운다.
            result += 1
        result += 1
    return result


if __name__ == "__main__":
    n = int(stdin.readline().strip())
    circles: list[Circle] = []

    for _ in range(n):
        x, r = [int(x) for x in stdin.readline().split()]
        circles.append(Circle.from_xr(x, r))

    # 끝점 기준으로 정렬, 같다면 지름이 작은 놈 기준으로 정렬
    circles.sort()
    print(sol(circles))
