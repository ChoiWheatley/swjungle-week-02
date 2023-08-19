"""
가운데를 말해요
이거 swea에서 중간값 찾기와 완전 똑같은 문제임
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV-fO0s6ARoDFAXT
두 힙을 붙여넣고 새로운 값이 추가될 때마다 중간값을 바꾸면 되는 문제. 이때 두가지 조건을 잘 지켜야 하는데,

1. maxheap.size == minheap.size
2. maxheap.peek() < mid < minheap.peek()
"""
from typing import Any
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


if __name__ == "__main__":
    n = int(stdin.readline().strip())
    mid = int(stdin.readline().strip())
    print(mid)
    n -= 1  # 이미 하나를 셌으니까
    minheap = Heap(MinHeap)
    maxheap = Heap(MaxHeap)

    for _ in range(n):
        new = int(stdin.readline().strip())
        if mid < new:
            minheap.insert(MinHeap(new))
        else:
            maxheap.insert(MaxHeap(new))

        # 그리고 두 힙의 개수를 맞춤과 동시에 mid 결정
        while len(minheap) < len(maxheap):
            minheap.insert(MinHeap(mid))
            tmp = maxheap.peek()
            if tmp is not None:
                mid = tmp.value
                maxheap.pop()
        while len(maxheap) < len(minheap):
            maxheap.insert(MaxHeap(mid))
            tmp = minheap.peek()
            if tmp is not None:
                mid = tmp.value
                minheap.pop()

        print(mid)
