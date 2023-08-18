import p2812
from unittest import TestCase


class MyTest(TestCase):
    def do_test(self, k, n, answer):
        self.assertEqual(answer, p2812.sol(n, k))

    def test1(self):
        self.do_test(4, "7898111101", 981111)

    def test2(self):
        self.do_test(5, "9993333932", 99993)

    def test3(self):
        self.do_test(5, "9993333912", 99992)
