import sys

N = int(input())
CM = [list(sys.stdin.readline().split()) for _ in range(N)]
ST = []
for i in range(N):
    cmd = CM[i]
    if cmd[0] == "push":
        num = int(cmd[1])
        ST.append(num)
    if cmd[0] == "pop":
        if len(ST) == 0:
            print(-1)
        else:
            top = ST.pop()
            print(top)
    if cmd[0] == "size":
        size = len(ST)
        print(size)
    if cmd[0] == "empty":
        empty = len(ST) == 0
        print(1 if empty else 0)
    if cmd[0] == "top":
        if len(ST) == 0:
            print(-1)
        else:
            print(ST[-1])
