"""뱀"""
from collections import deque
from enum import Enum
from itertools import islice
from typing import Iterable, List, Self, Set, Tuple

INF = 100000


def int2tuple(i: int, side: int) -> Tuple[int, int]:
    """side X side 보드의 위치 id가 주어졌을 때, 정확한 위치 (r, c)를 반환한다."""
    return i // side, i % side


def tuple2int(rc: Tuple[int, int], side: int):
    """side X side 보드의 위치 (r, c)가 주어졌을 때, 아이디를 반환한다."""
    return rc[0] * side + rc[1]


class Rotation(Enum):
    CCW = "L"
    CW = "D"


class Ori(Enum):
    N = 0
    E = 1
    S = 2
    W = 3

    def rotate(self, to: Rotation) -> Self:
        if to == Rotation.CCW:
            return Ori((self.value + 3) % 4)
        else:
            return Ori((self.value + 1) % 4)


class Snake:
    queue: deque[int]
    orientation: Ori
    side: int

    def __init__(self, side: int):
        self.queue = deque([0])
        self.orientation = Ori.E
        self.side = side

    @property
    def ahead(self) -> int:
        """뱀 머리가 바라보는 방향 한 칸 앞을 리턴"""
        head = self.head
        match self.orientation:
            case Ori.N:
                return head - self.side
            case Ori.E:
                return head + 1
            case Ori.S:
                return head + self.side
            case Ori.W:
                return head - 1

    @property
    def head(self) -> int:
        """뱀 머리 맨날 self.queue[-1] 하기 싫잖아"""
        return self.queue[-1]

    @property
    def body(self) -> Iterable[int]:
        return islice(self.queue, len(self.queue) - 1)

    def move_forward(self, tail=False):
        """
        - tail: tail을 그대로 둘 것인지(T), 잘라버릴 것인지 결정(F)
        """
        self.queue.append(self.ahead)
        if not tail:
            self.queue.popleft()

    def rotate(self, to: Rotation):
        self.orientation = self.orientation.rotate(to)


class GameController:
    class GameOver(Exception):
        time: int

        def __init__(self, time: int):
            super().__init__("")
            self.time = time

    snake: Snake
    apples: Set[int]
    side: int
    timestamp: int

    def __init__(self, side: int, apples: List[Tuple[int, int]]):
        self.snake = Snake(side)
        self.side = side
        self.apples = {tuple2int(tup, side) for tup in apples}
        self.timestamp = 0

    def order(self, time: int, rotation: Rotation):
        """
        ## 백준 문제 요구사항의 인터페이스

        - time: 게임시작 시간으로부터 지난 초 (해당 초가 끝난 시점)
        - rotation: time 초가 끝난 뒤에 왼쪽 혹은 오른쪽으로 90도 방향을 회전시킨다.
        """
        _s = self.snake
        time_delta = time - self.timestamp

        for t in range(time_delta):
            tail = False
            ahead = _s.ahead

            if _s.ahead in self.apples:
                tail = True
                self.apples.remove(ahead)

            if not all(0 <= l < self.side for l in int2tuple(ahead, self.side)):
                # FIXME - ahead가 우측 경계면에 닿지 않고 다음 줄 0번째 열로 점프하는 문제 발생
                # 행, 열 하나라도 경계에 닿거나 벗어나게 되면
                raise GameController.GameOver(time=self.timestamp + t + 1)

            for bodypart in _s.body:
                if ahead == bodypart:
                    raise GameController.GameOver(time=self.timestamp + t + 1)

            _s.move_forward(tail)

        _s.rotate(rotation)
        self.timestamp = time


if __name__ == "__main__":
    side = int(input())
    k = int(input())
    apples = []
    for _ in range(k):
        r, c = [int(x) for x in input().split()]
        apples.append((r - 1, c - 1))
    controller = GameController(side, apples)
    l = int(input())
    orders = [input().split() for _ in range(l)]
    try:
        for time, rotation in orders:
            time = int(time)
            rotation = Rotation(rotation)

            controller.order(time, rotation)

        while True:
            # 게임오버가 나올때까지 직진
            controller.order(INF, Rotation.CW)

    except GameController.GameOver as e:
        print(e.time)
