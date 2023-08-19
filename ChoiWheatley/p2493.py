"""막대 문제와 완전히 일치, but 인덱스를 같이 저장할 필요가 있음 (idx, height)"""

from typing import List, Tuple


def solve(ls: List[int]) -> List[int]:
    stack: List[Tuple[int, int]] = []
    ret: List[int] = []
    for idx, height in enumerate(ls):
        while len(stack) > 0 and stack[-1][1] <= height:
            stack.pop()
        if len(stack) == 0:
            ret.append(-1)
        else:
            ret.append(stack[-1][0])
        stack.append((idx, height))
    return ret


n = int(input())
ls = [int(x) for x in input().split()]
print(" ".join([str(i + 1) for i in solve(ls)]))
