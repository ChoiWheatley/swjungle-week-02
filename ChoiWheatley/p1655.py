"""
가운데를 말해요
이거 swea에서 중간값 찾기와 완전 똑같은 문제임
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV-fO0s6ARoDFAXT
두 힙을 붙여넣고 새로운 값이 추가될 때마다 중간값을 바꾸면 되는 문제. 이때 두가지 조건을 잘 지켜야 하는데,

1. maxheap.size == minheap.size
2. maxheap.peek() < mid < minheap.peek()
"""
from typing import Any, Generator, Iterable, List
from sys import stdin, stdout
from heapq import heappush, heappop


class MinHeap:
    def __init__(self, n=0):
        super().__init__()
        self.value = n

    def __lt__(self, other: Any) -> bool:
        return self.value < other.value


class MaxHeap:
    def __init__(self, n=0):
        super().__init__()
        self.value = n

    def __lt__(self, other: Any) -> bool:
        return self.value > other.value


def solve(seq: Iterable[int]) -> Generator[int, Any, Any]:
    it = iter(seq)
    leftheap: List[MaxHeap] = []
    rightheap: List[MinHeap] = []
    mid = it.__next__()
    yield mid

    for count, new in enumerate(it, start=2):
        if count % 2 == 0:
            # mid 변수에 new를 할당하지 않는다.
            # 두 중앙값은 두 힙의 루트에 존재
            if mid < new:
                heappush(rightheap, MinHeap(new))
                heappush(leftheap, MaxHeap(mid))
            else:
                heappush(leftheap, MaxHeap(new))
                heappush(rightheap, MinHeap(mid))
            mid = leftheap[0].value

        else:
            # mid 변수에 new를 할당한다. 다만, new의 위치에 따라서
            # 다양한 케이스가 존재
            if new < leftheap[0].value:
                # new go left, root of leftheap become mid
                mid = leftheap[0].value
                heappop(leftheap)
                heappush(leftheap, MaxHeap(new))
            elif rightheap[0].value < new:
                # new go right, root of rightheap become mid
                mid = rightheap[0].value
                heappop(rightheap)
                heappush(rightheap, MinHeap(new))
            else:
                mid = new

        yield mid


if __name__ == "__main__":
    n = int(stdin.readline().strip())
    gen = (int(stdin.readline().strip()) for _ in range(n))

    for i in solve(gen):
        stdout.write(str(i) + "\n")
