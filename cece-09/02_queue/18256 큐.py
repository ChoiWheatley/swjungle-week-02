import sys
from collections import deque
N = int(input())
queue = deque()

for i in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        queue.append(cmd[1])
    if cmd[0] == "pop":
        front = -1 if len(queue) == 0 else queue.popleft()
        print(front)
    if cmd[0] == "size":
        size = len(queue)
        print(size)
    if cmd[0] == "empty":
        empty = 1 if len(queue) == 0 else 0
        print(empty)
    if cmd[0] == "front":
        front = -1 if len(queue) == 0 else queue[0]
        print(front)
    if cmd[0] == "back":
        rear = -1 if len(queue) == 0 else queue[-1]
        print(rear)
