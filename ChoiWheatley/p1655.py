"""
가운데를 말해요
이거 swea에서 중간값 찾기와 완전 똑같은 문제임
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV-fO0s6ARoDFAXT
두 힙을 붙여넣고 새로운 값이 추가될 때마다 중간값을 바꾸면 되는 문제. 이때 두가지 조건을 잘 지켜야 하는데,

1. maxheap.size == minheap.size
2. maxheap.peek() < mid < minheap.peek()
"""
from typing import Any, Generator, Iterable
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


def solve(seq: Iterable[int]) -> Generator[int, Any, Any]:
    it = iter(seq)
    minheap = Heap(MinHeap)
    maxheap = Heap(MaxHeap)
    mid = it.__next__()
    yield mid

    for count, new in enumerate(it, start=2):
        if count % 2 == 0:
            # 짝수인 경우 mid를 사용하지 않는다. 대신 두 힙의 루트가 곧 중앙값이
            # 되게 만든다.
            if mid < new:
                minheap.insert(MinHeap(new))
                maxheap.insert(MaxHeap(mid))
            else:
                maxheap.insert(MaxHeap(new))
                minheap.insert(MinHeap(mid))
            mid = maxheap.peek().value  # 중앙값 두개 중 작은 것을 리턴하라고 했으므로

        else:
            # 홀수개일 경우 mid 변수에 중앙값을 추가한다.
            # 나머지를 두 힙에 추가한다.
            if new < maxheap.peek().value:
                mid = maxheap.peek().value
                maxheap.pop()
                maxheap.insert(MaxHeap(new))
            elif minheap.peek().value < new:
                mid = minheap.peek().value
                minheap.pop()
                minheap.insert(MinHeap(new))
            else:
                mid = new

        yield mid


if __name__ == "__main__":
    n = int(stdin.readline().strip())
    gen = (int(stdin.readline().strip()) for _ in range(n))

    for i in solve(gen):
        stdout.write(str(i) + "\n")
