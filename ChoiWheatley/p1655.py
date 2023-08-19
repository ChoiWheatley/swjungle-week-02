"""
가운데를 말해요
이거 swea에서 중간값 찾기와 완전 똑같은 문제임
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV-fO0s6ARoDFAXT
두 힙을 붙여넣고 새로운 값이 추가될 때마다 중간값을 바꾸면 되는 문제. 이때 두가지 조건을 잘 지켜야 하는데,

1. maxheap.size == minheap.size
2. maxheap.peek() < mid < minheap.peek()
"""
from bisect import bisect_left
from typing import Any, Iterable, List
from heap import Heap, Comparable
from sys import stdin, stdout


class MinHeap(Comparable):
    def __init__(self, n=0):
        super().__init__()
        self.value = n

    def __lt__(self, other: Any) -> bool:
        return self.value < other.value


class MaxHeap(Comparable):
    def __init__(self, n=0):
        super().__init__()
        self.value = n

    def __lt__(self, other: Any) -> bool:
        return self.value > other.value


def solve(seq: Iterable[int]) -> List[int]:
    it = iter(seq)
    mid = [it.__next__()]
    minheap = Heap(MinHeap)
    maxheap = Heap(MaxHeap)
    ret = [mid[0]]

    for count, new in enumerate(it, start=2):
        if count % 2 == 0:
            if mid[0] < new:
                minheap.insert(MinHeap(new))
                mid.append(minheap.peek().value)
                minheap.pop()
            else:
                maxheap.insert(MaxHeap(new))
                mid.insert(0, maxheap.peek().value)
                maxheap.pop()  # maxheap 개수가 하나 더 많아졌으므로

        else:
            # 홀수개일 경우 len(mids) = 3으로 만든 뒤에 가운데 값을 제외한
            # 나머지를 두 힙에 추가한다.
            mid.insert(bisect_left(mid, new), new)
            maxheap.insert(MaxHeap(mid[0]))
            minheap.insert(MinHeap(mid[2]))
            mid = [mid[1]]

        ret.append(mid[0])
    return ret


if __name__ == "__main__":
    n = int(stdin.readline().strip())
    gen = (int(stdin.readline().strip()) for _ in range(n))

    for i in solve(gen):
        stdout.write(str(i) + "\n")
