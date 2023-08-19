import sys
import heapq


N = int(input())
X = [int(sys.stdin.readline()) for _ in range(N)]
minH = []
maxH = []


for i in range(N):
    n = X[i]
    if i == 0:
        heapq.heappush(maxH, -n)  # max heap
        print(-maxH[0])
        continue

    elif len(minH) == len(maxH):
        heapq.heappush(maxH, -n)

    else:
        heapq.heappush(minH, n)

    if -maxH[0] > minH[0]:
        minroot = heapq.heappop(minH)
        heapq.heappush(maxH, -minroot)
        maxroot = heapq.heappop(maxH)
        heapq.heappush(minH, -maxroot)

    print(-maxH[0])
