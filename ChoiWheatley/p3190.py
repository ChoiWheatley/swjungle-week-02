"""뱀"""
from collections import deque
from enum import Enum
from typing import List, Set, Tuple


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

    def rotate(self, to: Rotation):
        if to == Rotation.CCW:
            self.value = (self.value + 3) % 4
        else:
            self.value = (self.value + 1) % 4


class Snake:
    queue: deque[int]
    orientation: Ori
    side: int

    def __init__(self, side: int):
        self.queue = deque([0])
        self.orientation = Ori.E
        self.side = side

    def ahead(self) -> int:
        """뱀 머리가 바라보는 방향 한 칸 앞을 리턴"""
        head = self.head()
        match self.orientation:
            case Ori.N:
                return head - self.side
            case Ori.E:
                return head + 1
            case Ori.S:
                return head + self.side
            case Ori.W:
                return head - 1

    def head(self) -> int:
        """뱀 머리 맨날 self.queue[-1] 하기 싫잖아"""
        return self.queue[-1]

    def move_forward(self, tail=False):
        """
        - tail: tail을 그대로 둘 것인지(T), 잘라버릴 것인지 결정(F)
        """
        self.queue.append(self.ahead())
        if not tail:
            self.queue.popleft()

    def rotate(self, to: Rotation):
        self.orientation.rotate(to)


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
        time_delta = time - self.timestamp

        for t in range(time_delta):
            tail = False
            ahead = self.snake.ahead()
            if self.snake.ahead() in self.apples:
                tail = True
            if not all(0 <= l < self.side for l in int2tuple(ahead, self.side)):
                # 행, 열 하나라도 경계에 닿거나 벗어나게 되면
                raise GameController.GameOver(time=self.timestamp + t)

            self.snake.move_forward(tail)

        self.snake.rotate(rotation)
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
    try:
        for _ in range(k):
            time, rotation = input().split()
            time = int(time)
            rotation = Rotation(rotation)

            controller.order(time, rotation)
    except GameController.GameOver as e:
        print(e.time)
