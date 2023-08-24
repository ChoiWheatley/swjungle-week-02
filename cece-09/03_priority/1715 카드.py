import sys
from heapq import heappop, heappush, heapify

N = int(input())
cards = [int(sys.stdin.readline()) for _ in range(N)]
heapify(cards)

sum = 0
cnt = 0
while len(cards) != 1:
    c1 = heappop(cards)
    c2 = heappop(cards)

    heappush(cards, c1+c2)
    sum += (c1+c2)
    cnt += 1

print(sum)
