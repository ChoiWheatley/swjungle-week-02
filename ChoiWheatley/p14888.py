"""
연산자 끼워넣기 전에 풀었지만 이번엔 DFS를 사용하여 결정트리를 순회하는 것으로 보인다.

"""

from enum import Enum
from typing import List


class Op(Enum):
    Add = 0
    Sub = 1
    Mul = 2
    Div = 3

    def __call__(self, lhs: int, rhs: int) -> int:
        match self:
            case Op.Add:
                return lhs + rhs
            case Op.Sub:
                return lhs - rhs
            case Op.Mul:
                return lhs * rhs
            case Op.Div:
                if lhs < 0 and rhs > 0:
                    return -(-lhs // rhs)
                return lhs // rhs


g_operation_cnt: List[int] = [0, 0, 0, 0]
g_max = -(1 << 31)
g_min = 1 << 31
g_list = []
N = 11


def r_sol(idx: int, acc: int):
    global g_max, g_min
    if idx >= N - 1:
        g_max = max(g_max, acc)
        g_min = min(g_min, acc)
        return

    for i, cnt in enumerate(g_operation_cnt):
        if cnt > 0:
            g_operation_cnt[i] -= 1
            r_sol(idx + 1, Op(i)(acc, g_list[idx + 1]))
            g_operation_cnt[i] += 1


if __name__ == "__main__":
    N = int(input())
    g_list = [int(x) for x in input().split()]
    g_operation_cnt = [int(x) for x in input().split()]

    r_sol(0, g_list[0])

    print(g_max)
    print(g_min)
