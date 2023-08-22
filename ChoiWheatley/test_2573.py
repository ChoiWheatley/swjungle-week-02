from ChoiWheatley.p2573 import Glaciers, sol
from unittest import TestCase
from timeout_decorator import TimeoutError, timeout


class Timeout(TimeoutError):
    pass


class Test(TestCase):
    MAX = 300

    # @timeout(1, timeout_exception=Timeout)
    def test_1(self):
        ice = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 2, 4, 5, 3, 0, 0],
            [0, 3, 0, 2, 5, 2, 0],
            [0, 7, 6, 2, 4, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ]
        answer = 2

        gla = Glaciers(ice)
        self.assertEqual(answer, sol(gla))

    @timeout(2, timeout_exception=Timeout)
    def test_timeout(self):
        """1 이상의 정수가 들어가는 칸의 개수는 1000개 이하이다"""
        ice = [[0 for _ in range(self.MAX)] for _ in range(self.MAX)]
        for i in range(1, min(self.MAX - 1, 99)):
            for j in range(1, min(self.MAX - 1, 99)):
                ice[i][j] = 10

        answer = 0

        gla = Glaciers(ice)
        self.assertEqual(answer, sol(gla))
