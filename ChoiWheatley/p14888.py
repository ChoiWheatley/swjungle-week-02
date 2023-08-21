"""
연산자 끼워넣기 전에 풀었지만 이번엔 DFS를 사용하여 결정트리를 순회하는 것으로 보인다.

"""

from enum import Enum
from typing import Any, Callable, Generator, List, Tuple


class Op(Enum):
    Add = 0
    Del = 1
    Mul = 2
    Div = 3

    def __call__(self, lhs: int, rhs: int) -> int:
        match self:
            case Op.Add:
                return lhs + rhs
            case Op.Del:
                return lhs - rhs
            case Op.Mul:
                return lhs * rhs
            case Op.Div:
                return lhs // rhs


g_num: List[int] = []

def r_decision_tree(rem: List[int]) -> Generator[Op, Any, Any]:
    """
    - rem: 남은 연산자의 개수를 +-*/ 순으로 나열
    """
    if all(x == 0 for x in rem):
        return acc

