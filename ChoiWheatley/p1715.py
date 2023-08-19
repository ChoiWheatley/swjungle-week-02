"""
카드 정렬하기

수열을 더하는데 괄호를 어디에 배치하느냐에 따라 달라지는 결과값 중 최소를 구하는 문제인듯
"""

### 가설: 작은놈들부터 묶으면 비교횟수가 줄어든다

from typing import List
from heapq import heapify, heappush, heappop
from sys import stdin


def sol1(ls: List[int]) -> int:
    heapify(ls)
    res = 0
    while len(ls) > 0:
        pack1 = ls[0]
        heappop(ls)
        if len(ls) == 0:
            break
        pack2 = ls[0]
        heappop(ls)
        newpack = pack1 + pack2
        res += newpack
        heappush(ls, newpack)

    return res


if __name__ == "__main__":
    n = int(stdin.readline().strip())
    ls = [int(stdin.readline().strip()) for _ in range(n)]
    print(sol1(ls))
