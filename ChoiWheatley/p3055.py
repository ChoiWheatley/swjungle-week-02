"""
탈출

물: 확장할게
고슴도치: 도망칠게
"""

from collections import deque
from dataclasses import dataclass
from enum import Enum, auto
from typing import Any, Callable, Self


@dataclass
class Pos:
    r: int
    c: int

    def __add__(self, other: Any) -> Self:
        if isinstance(other, Pos):
            return Pos(self.r + other.r, self.c + other.c)
        if isinstance(other, tuple):
            return Pos(self.r + other[0], self.c + other[1])
        raise NotImplemented()

    def __neg__(self) -> Self:
        return Pos(-self.r, -self.c)

    def as_tuple(self) -> tuple[int, int]:
        return self.r, self.c


class Cell(Enum):
    Empty = "."
    Water = "*"
    Rock = "X"
    Sonic = "S"
    Biever = "D"


g_delta: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Forest:
    sonic_q: deque[Pos]  # 소닉이도 일종의 구역으로 취급하자.
    biever: Pos  # 목적지
    flood_q: deque[Pos]  # bfs 돌면서 확장할 구역들
    map: list[list[Cell]]  # 공터, 물, 돌을 저장함
    turn_no: int  # 경과시간
    ROW: int
    COL: int

    def __init__(self, map: list[str], ROW: int, COL: int) -> None:
        self.sonic_q = deque()
        self.flood_q = deque()

        # init map, sonic, flood, biever
        self.map = [[Cell.Empty for _ in range(COL)] for _ in range(ROW)]
        for i in range(ROW):
            for j in range(COL):
                cell = Cell(map[i][j])
                self.map[i][j] = cell
                match cell:
                    case Cell.Sonic:
                        self.sonic_q.append(Pos(i, j))
                    case Cell.Water:
                        self.flood_q.append(Pos(i, j))
                    case Cell.Biever:
                        self.biever = Pos(i, j)

        self.turn_no = 0
        self.ROW = ROW
        self.COL = COL

    def bfs(
        self, queue: deque[Pos], propagation_policy: Callable[[Pos], bool], cell: Cell
    ) -> deque[Pos]:
        """딱 한턴동안 obj의 구역을 확장한다. 마치 지난번 [[도마도]] 문제처럼.
        그래서 그 결과값을 다시 본래변수에 되먹이는 작업이 필요한데, 메모리를 오지게 많이
        쓰게 된다. 더 좋은 방법은 없을까?

        - obj: 소닉이던, 물이던 똑같이 취급할 수 있게 되었다.
        - propagation_policy: 영역을 확장할 수 있는가?
        - cell: map을 업데이트 할 때 쓸 녀석
        """
        tmp_q: deque[Pos] = deque()
        while queue:
            cur = queue.popleft()

            if not propagation_policy(cur):
                continue
            self.map[cur.r][cur.c] = cell

            # 인접 노드들 순회
            for d in g_delta:
                adj = cur + d
                if not (0 <= adj.r < self.ROW and 0 <= adj.c < self.COL):
                    continue
                if not propagation_policy(adj):
                    continue
                if self.map[adj.r][adj.c] == cell:
                    # duplicate
                    continue
                # do push and update
                tmp_q.append(adj)
                self.map[adj.r][adj.c] = cell

        return tmp_q


class GameController:
    forest: Forest

    AFFECTED_BY_FLOOD = (Cell.Empty, Cell.Sonic, Cell.Water)
    AFFECTED_BY_SONIC = (Cell.Empty, Cell.Biever, Cell.Sonic)

    class Status(Enum):
        Drown = auto()
        Safe = auto()
        Other = auto()

    def __init__(self, forest: Forest) -> None:
        self.forest = forest

    def propagate_sonic(self) -> None:
        f = self.forest
        sonic_policy: Callable[[Pos], bool] = lambda pos: any(
            f.map[pos.r][pos.c] == x for x in GameController.AFFECTED_BY_SONIC
        )
        f.sonic_q = f.bfs(f.sonic_q, sonic_policy, Cell.Sonic)

    def propagate_flood(self) -> None:
        f = self.forest
        flood_policy: Callable[[Pos], bool] = lambda pos: any(
            f.map[pos.r][pos.c] == x for x in GameController.AFFECTED_BY_FLOOD
        )
        f.flood_q = f.bfs(f.flood_q, flood_policy, Cell.Water)

    def next_turn(self) -> None:
        """한 턴을 시뮬레이션 한다. 순서대로
        1. 물을 범람시킨다.
        2. 소닉이의 영역을 확장한다.
        """
        self.propagate_sonic()
        self.forest.turn_no += 1

        if self.get_game_status() is not self.Status.Other:
            return

        self.propagate_flood()

    def get_game_status(self) -> Status:
        f = self.forest
        # 소닉이가 비버의 집에 닿았는가?
        if f.map[f.biever.r][f.biever.c] == Cell.Sonic:
            return GameController.Status.Safe

        # 소닉이가 물에 잠겼는가?
        if len(f.sonic_q) == 0:
            return GameController.Status.Drown

        return GameController.Status.Other


if __name__ == "__main__":
    r, c = [int(x) for x in input().split()]
    lines = [input() for _ in range(r)]
    forest = Forest(lines, r, c)
    gc = GameController(forest)

    while gc.get_game_status() is GameController.Status.Other:
        gc.next_turn()

    match gc.get_game_status():
        case GameController.Status.Safe:
            print(gc.forest.turn_no)
        case GameController.Status.Drown:
            print("KAKTUS")
