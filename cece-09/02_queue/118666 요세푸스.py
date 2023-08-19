from collections import deque

N, K = map(int, input().split())
queue = deque([i+1 for i in range(N)])
R = []

i, cnt = 0, 0

while queue:
    if cnt == K-1:
        kill = queue.popleft()
        R.append(kill)
        cnt = 0  # 다시 0부터 k-1까지 센다
    else:
        front = queue.popleft()
        queue.append(front)
        cnt += 1

print("<"+", ".join(list(map(str, R))) + ">")
