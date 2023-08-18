from collections import deque
from sys import stdin

n = int(stdin.readline().strip())
ops = [stdin.readline().strip().split() for _ in range(n)]
queue = deque(maxlen=2_000_000)

for args in ops:
    match args[0]:
        case "push":
            queue.append(int(args[1]))
        case "pop":
            if len(queue) <= 0:
                print(-1)
            else:
                print(queue[0])
                queue.popleft()
        case "size":
            print(len(queue))
        case "empty":
            print(1 if len(queue) <= 0 else 0)
        case "front":
            if len(queue) <= 0:
                print(-1)
            else:
                print(queue[0])
        case "back":
            if len(queue) <= 0:
                print(-1)
            else:
                print(queue[-1])
