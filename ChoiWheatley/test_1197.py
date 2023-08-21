from typing import List, Tuple
from unittest import TestCase
from ChoiWheatley.p1197 import sol


class Test(TestCase):
    def test_1(self):
        self.assertEqual(3, sol([(1, 2, 1), (2, 3, 2), (1, 3, 3)]))

    def test_2(self):
        self.assertEqual(6, sol([(1, 2, 2), (2, 4, 1), (4, 3, 4), (3, 1, 3)]))

    def test_3(self):
        self.assertEqual(
            24,
            sol(
                [
                    (1, 2, 2),
                    (2, 3, 3),
                    (3, 4, 1),
                    (1, 5, 3),
                    (2, 6, 1),
                    (3, 7, 2),
                    (4, 8, 5),
                    (5, 6, 4),
                    (6, 7, 3),
                    (7, 8, 3),
                    (5, 9, 4),
                    (6, 10, 2),
                    (7, 11, 4),
                    (8, 12, 3),
                    (9, 10, 3),
                    (10, 11, 3),
                    (11, 12, 1),
                ]
            ),
        )
