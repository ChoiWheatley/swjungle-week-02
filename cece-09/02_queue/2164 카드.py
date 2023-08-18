from collections import deque

N = int(input())
dq = deque([i+1 for i in range(N)])

while len(dq) > 1:
    dq.popleft()
    v = dq.popleft()
    dq.append(v)

print(dq[0])
