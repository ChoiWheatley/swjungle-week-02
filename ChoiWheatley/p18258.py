from collections import deque

n = int(input())
ops = [input().split() for _ in range(n)]
queue = deque()

for args in ops:
    match args[0]:
        case "push":
            queue.append(int(args[1]))
        case "pop":
            try:
                print(queue[0])
                queue.popleft()
            except IndexError:
                print(-1)
        case "size":
            print(len(queue))
        case "empty":
            print(1 if len(queue) <= 0 else 0)
        case "front":
            try:
                print(queue[0])
            except IndexError:
                print(-1)
        case "back":
            try:
                print(queue[-1])
            except IndexError:
                print(-1)
