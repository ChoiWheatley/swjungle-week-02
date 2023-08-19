"""
가운데를 말해요
이거 swea에서 중간값 찾기와 완전 똑같은 문제임
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV-fO0s6ARoDFAXT
두 힙을 붙여넣고 새로운 값이 추가될 때마다 중간값을 바꾸면 되는 문제. 이때 두가지 조건을 잘 지켜야 하는데,

1. maxheap.size == minheap.size
2. maxheap.peek() < mid < minheap.peek()
"""
from bisect import bisect_left
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
    mids = []  # 짝수일 때는 두개, 홀수일 때는 하나
    mids.append(int(stdin.readline().strip()))
    print(mids[0])

    minheap = Heap(MinHeap)
    maxheap = Heap(MaxHeap)

    for count in range(2, n + 1):
        new = int(stdin.readline().strip())
        if count % 2 == 0:
            # 짝수개일 경우 두개의 중앙값 중 작은 놈을 출력한다.
            if mids[0] < new:
                minheap.insert(MinHeap(new))
                mids.append(minheap.peek().value)
                minheap.pop()  # minheap 개수가 하나 더 많아졌으므로
            else:
                maxheap.insert(MaxHeap(new))
                mids.insert(0, maxheap.peek().value)
                maxheap.pop()  # maxheap 개수가 하나 더 많아졌으므로

        else:
            # 홀수개일 경우 len(mids) = 3으로 만든 뒤에 가운데 값을 제외한
            # 나머지를 두 힙에 추가한다.
            mids.insert(bisect_left(mids, new), new)
            maxheap.insert(MaxHeap(mids[0]))
            minheap.insert(MinHeap(mids[2]))
            mids = [mids[1]]

        print(mids[0])
